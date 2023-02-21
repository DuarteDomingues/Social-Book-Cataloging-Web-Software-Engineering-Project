from repositorios.repositorio_criticas import RepositorioCriticas


class ServicoCritica():

    def __init__(self, rep_criticas):
        #self.__rep_criticas= RepositorioCriticas()
        self.__rep_criticas = rep_criticas
    
    def pedir_criticas_livro(self, id_livro, num_criticas):

        criticas = self.__rep_criticas.obter_criticas_livro(id_livro, num_criticas)
        return criticas
    
    def pedir_criticas_amigos(self, amigos, num_criticas):

        criticas = self.__rep_criticas.obter_criticas_amigos(amigos, num_criticas)
        return criticas

    
    def pedir_adicionar_critica(self,  id_livro, id_utilizador, texto, classif):
        self.__rep_criticas.adicionar_critica(id_livro, id_utilizador, texto, classif)


    def __ordenar_criticas(self,criticas):
        
        ordenar_criticas = criticas
        for critica in ordenar_criticas:
            critica.data_para_date()
        ordenar_criticas.sort(key=lambda a: a[4], reverse= True)
        return ordenar_criticas
    
    def pedir_comentarios(self, id_critica):
        return self.__ordenar_comentarios(self.__rep__comentarios.obter_comentarios(id_critica))
    
    def pedir_adicionar_comentario(self, id_critica, id_utilizador, comentario):
        return self.__rep__comentarios.adicionar_comentario(id_critica, id_utilizador, comentario)
    
    def __ordenar_comentarios(self, comentarios):

        ordenar_comentarios = comentarios
        for comentario in ordenar_comentarios:
            comentario.data_para_date()

        ordenar_comentarios.sort(key=lambda a: a[4], reverse= True)
        return ordenar_comentarios

