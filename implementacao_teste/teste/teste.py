from teste_apresentacao_livro.teste_livro import TesteLivro
from teste_critica.teste_critica import TesteCritica
from teste_utilizadores.teste_utilizadores import TesteUtilizadores
from teste_colecao.teste_colecao import TesteColecao

from repositorios.repositorio_livro import RepositorioLivro
from repositorios.repositorio_colecao import RepositorioColecao
from repositorios.repositorio_criticas import RepositorioCriticas
from repositorios.repositorio_utilizadores import RepositorioUtilizadores

class TesteApp:

    def __init__(self):
        
        #inicializar repositorios
        self.__rep_livros = RepositorioLivro()
        self.__rep_criticas = RepositorioCriticas()
        self.__rep_colecao = RepositorioColecao()
        self.__rep_utilizadores = RepositorioUtilizadores()        

        #inicializar classes de teste ao dominio
        teste_livro = TesteLivro(self.__rep_livros)
        teste_criticas = TesteCritica(self.__rep_criticas)
        teste_utilizador = TesteUtilizadores(self.__rep_utilizadores)
        teste_colecao = TesteColecao(self.__rep_colecao)

        #testes
        print("-------------- Testes ---------------------------")
        if (teste_livro.correr_teste()):
            print("teste livro passou ")
        else:
            print("teste livro falhou")
        
        if (teste_criticas.correr_teste()):
            print("teste critica passou ")
        else:
            print("teste critica falhou")
        
        if (teste_utilizador.correr_teste()):
            print("teste utilizador passou ")
        else:
            print("teste utilizador falhou")
        
        if (teste_colecao.correr_teste()):
            print("teste colecao passou ")
        else:
            print("teste colecao falhou")
        
        
        #imprmir dados
        self.__rep_utilizadores.print_dados()
        self.__rep_livros.print_dados()
        self.__rep_criticas.print_dados()
        self.__rep_colecao.print_dados()
        

TesteApp()
        


