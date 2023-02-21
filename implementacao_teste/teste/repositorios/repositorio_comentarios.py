from dominio.entidades.comentario import Comentario

class RepositorioComentarios():

    def __init__(self):
        #atributos de teste, seria tabelas sql
        self.__comentarios = [(0,1,1,"achei muito bom","22-02-2021"), (1,0,0, "nao gostei muito!","12-02-2022")] #(id_comentario, id_critica, id_utilizador, texto)
    
    def obter_comentarios(self, id_critica):
        
        comentarios = []
        for com in self.__comentarios:
            if com[1] == id_critica:
                comentario = Comentario(com[0], com[1], com[2], com[3],com[4])
                comentarios.append(comentario)
        return comentarios
    
    def adicionar_comentario(self, id_critica, id_utilizador, comentario):

        idx = len(self.__comentarios)+1
        com = (idx,id_critica,id_utilizador,comentario,"12-28-2022")
        self.__comentarios.append(com)









