from bookcrew.repositorios.repositorio_colecao import  RepositorioColecao
from bookcrew.repositorios.repositorio_livro import  RepositorioLivro

class ServicoColecao:

    def __init__(self):

        self.__rep_col = RepositorioColecao()
        self.__rep_livros = RepositorioLivro()
    

    def pedir_col_utilizador(self, id_utilizador):
        return self.__rep_col.obter_colecao_utilizador(id_utilizador)

    
    def atualizar_col(self, col):
        col.set_lista_ler(self.__rep_livros.obter_livro_lista_livros(col.lista_ler))
        col.set_lista_ja_leu(self.__rep_livros.obter_livro_lista_livros(col.lista_ja_leu))
        col.set_lista_a_ler(self.__rep_livros.obter_livro_lista_livros(col.lista_a_ler))
        return col

    
    def pedir_adicionar_livro_colecao(self, id_livro, categoria, id_utilizador):
        return self.__rep_col.adicionar_livro_colecao(id_livro, categoria, id_utilizador)

    def pedir_remover_livro_colecao(self, id_livro, categoria, id_utilizador):
        return self.__rep_col.remover_livro_colecao( id_livro, categoria, id_utilizador)
    