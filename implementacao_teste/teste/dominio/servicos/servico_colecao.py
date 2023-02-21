from repositorios.repositorio_colecao import RepositorioColecao

class ServicoColecao:

    def __init__(self, rep_col):

        #self.__rep_col = RepositorioColecao()
        self.__rep_col = rep_col
    
    def pedir_adicionar_livro_colecao(self, id_livro, categoria, id_utilizador):
        return self.__rep_col.adicionar_livro_colecao(id_livro, categoria, id_utilizador)

    def remover_livro_colecao(self, id_livro, categoria, id_utilizador):
        return self.__rep_col.remover_livro_colecao( id_livro, categoria, id_utilizador)
    
    def pedir_colecao_utilizador(self, colecao):
        return self.__rep_col.obter_colecao_utilizador(colecao)