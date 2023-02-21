from dominio.entidades.colecao import Colecao

class RepositorioColecao:

    
    def __init__(self):
        #atributos de teste, seriam tabelas sql
        #lista de (idUtilizador, idColecao) #PK id_colecao
        #lista de (id_colecao, categoria, idLivro ) #PK id_colecao_id_categoria
        self.__colecao_livros = [] 
        self.__livro_colecao = [] 
        self.__popular_repositorio()

    
    def adicionar_livro_colecao(self, id_livro, categoria, id_utilizador):

        colecao_livro = self.__obter_colecao(id_utilizador)
        if colecao_livro!=None:
            novo_livro_colecao = (colecao_livro[1], categoria, id_livro)
            self.__livro_colecao.append(novo_livro_colecao)
            return True
        
        else:
            return False


    def remover_livro_colecao(self, id_livro, categoria, id_utilizador):

        colecao_livro = self.__obter_colecao(id_utilizador)
        if colecao_livro!=None:
            for livro_colecao in self.__livro_colecao:
                if livro_colecao[0] == colecao_livro[0] and livro_colecao[1] == categoria and livro_colecao[2] == id_livro:
                    self.__livro_colecao.remove(livro_colecao)
                    return True

        else:
            return False


    def obter_colecao_utilizador(self, id_utilizador):
        
        col = Colecao(id_utilizador)
        colecao_livro = self.__obter_colecao(id_utilizador)
        if colecao_livro!=None:
            
            for livro_colecao in self.__livro_colecao:

                if livro_colecao[0] == colecao_livro[0]:

                    if livro_colecao[1] == 0:
                        col.adicionar_lista_ler(livro_colecao[2])

                    elif livro_colecao[1] ==1:
                         col.adicionar_lista_ja_leu(livro_colecao[2])

                    elif livro_colecao[1] ==2:
                        col.adicionar_lista_a_ler(livro_colecao[2])
        
        return col
    

    def __obter_colecao(self, id_utilizador):

        for i in self.__colecao_livros:
            if i[0] == id_utilizador:
                return i
        
        return None
    

    def __popular_repositorio(self):

        self.__colecao_livros = [(1,1),(2,2)] #lista de (idUtilizador, idColecao) #PK id_colecao
        self.__livro_colecao = [] #lista de (id_colecao, categoria, idLivro ) #PK id_colecao_id_categoria


    def print_dados(self):

        print("-------------- Colecao ---------------------------")
        for col in self.__colecao_livros:
            col_utl = self.obter_colecao_utilizador(col[1])
            print("id_colecao:", col[0], ", lista_ja_leu:", col_utl.lista_a_ler,", lista_ja_leu:", col_utl.lista_ja_leu,
            ", lista_ja_leu:", col_utl.lista_ler)



    
    def obter__colecao_livros(self):
        return self.__colecao_livros
    
    def obter__livro_colecao(self):
        return self.__livro_colecao
    
    


    


