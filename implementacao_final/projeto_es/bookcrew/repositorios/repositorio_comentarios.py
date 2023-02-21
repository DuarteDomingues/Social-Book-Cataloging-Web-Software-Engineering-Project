from bookcrew import models
from bookcrew.dominio.entidades.comentario import Comentario
from datetime import date

class RepositorioComentarios():

    
    def obter_comentarios(self, id_critica):
        
        comentarios_res=[]

        comentarios = models.Comentario.objects.filter(id_critica=id_critica)
        if comentarios!=None:
            for com in comentarios:
                vals = [com.id_comentario, com.id_critica.pk, com.id_utilizador.pk, com.texto, com.data]
                com = Comentario(vals[0],vals[1],vals[2],vals[3],vals[4])
                comentarios_res.append(com)
        
        return comentarios_res


    
    def adicionar_comentario(self, id_critica, id_utilizador, texto):

        critica =  models.Critica.objects.get(pk=id_critica)
        util = models.Utilizador.objects.get(pk=id_utilizador)
        curr_data = str(date.today())
        Comentario = models.Comentario.objects.create(id_critica=critica, id_utilizador=util, texto=texto,data=curr_data)
        if Comentario!=None:
            return True
        else:
            return False









