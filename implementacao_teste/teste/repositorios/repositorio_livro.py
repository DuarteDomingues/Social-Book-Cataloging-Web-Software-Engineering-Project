from dominio.entidades.livro import Livro

class RepositorioLivro():

    def __init__(self):
        
        #atributos de teste, seria acedido da API Google Books
       # self.__livros = [(1,"O Processo", "Franz Kafka", "Romance", "4", 200, "Lorem  dolor sit amet,consectetur adipiscing elit. Aliquam quis varius orci.","foto"),
       # (2,"No Longer Human", "Osamu Dazai","Ficção", "4.5",240,"Vestibulum sollicitudin lectus id enim pretium maximus. ","foto")]
        self.__livros = []
        self.__popular_repositorio()

    def obter_livro(self, id_livro):
        livro= None
        for livro in self.__livros:
            if livro[0] == id_livro:
                livro = Livro(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5] ,livro[6])
                return livro
        
        return None

    def obter_livros(self, nome_livro):

        livros_encontrados=[]
        for livro in self.__livros:
            nome_livro_min = livro[1].lower()
            if str.__contains__(nome_livro_min, (nome_livro.lower())):
                livro_encontrado = Livro(id_livro=livro[0], titulo=livro[1], autor=livro[2], ref_foto=livro[7])
                livros_encontrados.append(livro_encontrado)
        return livros_encontrados
    
    def obter_info_livros_criticas(criticas):
        return None
    
    def obter_info_livros_colecao(colecao):
        return None
    
    
    def __popular_repositorio(self):
        
        livro_1 = (1,"O Processo", "Franz Kafka", "Romance", "4", 200, "Lorem  dolor sit amet,consectetur adipiscing elit. Aliquam quis varius orci.","foto")
        livro_2 = (2,"No Longer Human", "Osamu Dazai","Ficção", "4.5",240,"Vestibulum sollicitudin lectus id enim pretium maximus. ","foto")
        self.__livros.append(livro_1)
        self.__livros.append(livro_2)

    def print_dados(self):

        print("-------------- Livros ---------------------------")
        for livro in self.__livros:
            print("id_livro:", livro[0], ", titulo:", livro[1], ", genero:", livro[2], ", classificacao:", livro[3],
            ", numero paginas:", livro[4], ", descricao:",livro[5], ", foto:", livro[6] )












    
