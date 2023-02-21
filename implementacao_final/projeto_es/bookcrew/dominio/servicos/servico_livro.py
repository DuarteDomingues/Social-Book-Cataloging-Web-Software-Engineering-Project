from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

from bookcrew.repositorios.repositorio_livro import RepositorioLivro
from bookcrew.repositorios.repositorio_criticas import RepositorioCriticas
from bookcrew.repositorios.repositorio_utilizadores import RepositorioUtilizadores
from bookcrew.repositorios.repositorio_colecao import  RepositorioColecao


class ServicoLivro:

    def __init__(self):
        self.__rep_livro = RepositorioLivro()
        self.__rep_criticas = RepositorioCriticas()
        self.__rep_utilizadores = RepositorioUtilizadores()
        self.__rep_col = RepositorioColecao()

    def pedir_livro_lista_livros(self, livros_ids):

        livros = []
        for livro_id in livros_ids:
            livros.append(self.__rep_livro.obter_livro(livro_id))
        
        return list(set(livros))
    

    def pedir_livro(self, id_livro):
        return self.__rep_livro.obter_livro(id_livro)

    def pedir_livros(self,nome_livro, max_resultados ):
        return self.__rep_livro.obter_livros(nome_livro, max_resultados)


    
    def obter_info_livro(self, id_livro, num_criticas):

        livro = self.pedir_livro(id_livro)
        criticas = self.__pedir_criticas(id_livro,num_criticas)
        info_utilizadores = self.__pedir_utilizadores(criticas)

        return livro, criticas, info_utilizadores


    def pedir_adicionar_livro_colecao(self, id_livro, categoria, id_utilizador):
        return self.__rep_col.adicionar_livro_colecao(id_livro, categoria, id_utilizador)


    def pedir_verificar_livro_colecao(self,id_livro, id_utl):
        return self.__rep_col.verificar_livro_colecao(id_livro, id_utl)
    
    def pedir__adicionar_critica(self, id_livro,sub_cat,mensagem,classificao):
        return self.__rep_criticas.adicionar_critica(id_livro,sub_cat,mensagem,classificao)


        
    def order_livros_decrescente(self, livros):

        ordenar_livros = livros
        ordenar_livros.sort(key=lambda a: a[4], reverse= True)
        return ordenar_livros



    def __obter_info_utilizador_lista_criticas(self, criticas):

        if criticas !=None:
            ids_utilizadores=[]
            for critica in criticas:
                ids_utilizadores.append(critica.id_utilizador)
        
            ids_utilizadores = list(set(ids_utilizadores)) 

        
        return ids_utilizadores
    


    def __pedir_criticas(self, id_livro, num_criticas):
        return self.__rep_criticas.obter_criticas_livro(id_livro,num_criticas)
    
    def __pedir_utilizadores(self,criticas):
        utilizadores_ids = self.__obter_info_utilizador_lista_criticas(criticas)
        info_utilizadores = self.__rep_utilizadores.obter_info_utilizadores(utilizadores_ids)
        return info_utilizadores



