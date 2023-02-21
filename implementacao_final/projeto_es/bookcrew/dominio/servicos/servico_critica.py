from bookcrew.repositorios.repositorio_criticas import  RepositorioCriticas
from bookcrew.repositorios.repositorio_utilizadores import RepositorioUtilizadores
from bookcrew.repositorios.repositorio_livro import RepositorioLivro
from bookcrew.repositorios.repositorio_comentarios import RepositorioComentarios

class ServicoCritica():

    def __init__(self):
        
        self.__rep_critica = RepositorioCriticas()
        self.__rep_coms = RepositorioComentarios()


    def pedir_critica(self, id_critica):


        return self.__rep_critica.obter_critica(id_critica)
    
    def pedir_obter_criticas_utilizadores(self, amigos_ids,num_criticas):
        return self.__rep_critica.obter_criticas_utilizadores(amigos_ids,num_criticas)
    

    def pedir_lista_livros_critica(self,livros_ids):

        livros = []
        for livro_id in livros_ids:
            livros.append(self.__rep_livro.obter_livro(livro_id))
        
        return list(set(livros))



    def obter_info_utilizador_lista_criticas(self, criticas):

        if criticas !=None:
            ids_utilizadores=[]
            for critica in criticas:
                ids_utilizadores.append(critica.id_utilizador)
        
            ids_utilizadores = list(set(ids_utilizadores)) 

        
        return ids_utilizadores
    
    def obter_livro_ids_criticas(self, criticas):

        ids_livros = []
        if criticas != None:
            for critica in criticas:
                ids_livros.append(critica.id_livro)
        
        return list(set(ids_livros))
    

    def pedir_comentarios(self,id_critica):

        return self.__rep_coms.obter_comentarios(id_critica)
    
    def obter_ids_utilizadores_comentarios(self, comentarios):

        comentarios_ids = []
        for comentario in comentarios:
            comentarios_ids.append(comentario.id_utilizador)
        return list(set(comentarios_ids))
    
    def pedir_adicionar_comentario(self, id_critica,id_utilizador,mensagem):

        self.__rep_coms.adicionar_comentario(id_critica,id_utilizador,mensagem)


    

    def __ordenar_criticas(self,criticas):
        
        ordenar_criticas = criticas
        for critica in ordenar_criticas:
            critica.data_para_date()
        ordenar_criticas.sort(key=lambda a: a[4], reverse= True)
        return ordenar_criticas
