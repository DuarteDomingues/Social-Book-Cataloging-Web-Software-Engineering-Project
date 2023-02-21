
from repositorios.repositorio_livro import RepositorioLivro

class ServicoLivro:

    def __init__(self,rep_livros):
        #self.__rep_livros = RepositorioLivro()
        self.__rep_livros = rep_livros
    
    def pedir_livro(self,id_livro):
        return self.__rep_livros.obter_livro(id_livro)
    
    def pedir_livros_nome(self, nome_livro):
        return self.__rep_livros.obter_livros(nome_livro)
    
    def order_livros_decrescente(self, livros):

        ordenar_livros = livros
        ordenar_livros.sort(key=lambda a: a[4], reverse= True)
        return ordenar_livros
    
        





