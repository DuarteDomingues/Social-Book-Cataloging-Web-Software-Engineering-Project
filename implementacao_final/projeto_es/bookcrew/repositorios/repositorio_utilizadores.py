
from bookcrew import models
from bookcrew.dominio.entidades.info_utilizador import InfoUtilizador
from django.db.models import Q

class RepositorioUtilizadores():

    
    def obter_info_utilizador(self, id_utilizador):
        info_utilizador = None
        utilizador = models.Utilizador.objects.get(pk=id_utilizador)
        if utilizador != None:
            valores = [utilizador.id_utilizador,utilizador.nome, utilizador.foto, utilizador.descricao]
            info_utilizador = InfoUtilizador(valores[0],valores[1],valores[2],valores[3]) 
            return info_utilizador
        else: 
            return None
        
    
    def utilizador_id(self, id_utilizador):

        utilizador = models.Utilizador.objects.get(id_utilizador=id_utilizador)
        if utilizador != None:
            
            return utilizador.id_utilizador
        else: 
            return None
    
    #create user
        
    
    def obter_info_utilizadores(self, utilizadores_ids):
        
        info_utilizadores = []
        utilizadores = models.Utilizador.objects.filter(id_utilizador__in=utilizadores_ids)
    
        if utilizadores!=None:
            for utilizador in utilizadores:
                if utilizador != None:
                    valores = [utilizador.id_utilizador,utilizador.nome, utilizador.foto, utilizador.descricao]
                    info_utilizador = InfoUtilizador(valores[0],valores[1],valores[2],valores[3]) 
                    info_utilizadores.append(info_utilizador)
        
        return info_utilizadores
       

    
    def obter_utilizadores(self, nome_utilizador):
        
        utilizadores_encontrados = []
        
        utilizadores = models.Utilizador.objects.filter(nome__startswith=nome_utilizador)
        if utilizadores != None:
            for utilizador in utilizadores:
                valores = [utilizador.nome, utilizador.foto, utilizador.descricao]
                info_utilizador = InfoUtilizador(valores[0],valores[1],valores[2]) 
                utilizadores_encontrados.append(info_utilizador)
        
        return utilizadores_encontrados
    
    def criar_utilizador(self, nome):

        foto = "ref_foto"
        desc = "gosto imenso de livros históricos "
        utilizador = models.Utilizador.objects.create(nome=nome,foto=foto,descricao=desc)
        id = utilizador.id_utilizador
        return id
    
    def obter_id_utilizador(self, nome_utilizador):
        
        utilizador = models.Utilizador.objects.get(nome=nome_utilizador)
        if utilizador != None:
            return utilizador.id_utilizador
        else: 
            return None
    
    def obter_amizades(self, id_utilizador):
        
        amizades_res = []
        amizades = models.Amizade.objects.filter(Q(id_utilizador_1=id_utilizador) | Q(id_utilizador_2=id_utilizador))
        
        for a in amizades:
            print(a.id_utilizador_1)
            if a.id_utilizador_1.pk == id_utilizador:
                amizades_res.append(self.obter_info_utilizador(a.id_utilizador_2.pk))
            else:
                amizades_res.append(self.obter_info_utilizador(a.id_utilizador_1.pk))
        
        return amizades_res
    
    
    def enviar_pedido_amizade(self, id_utilizador_env, id_utilizador_rec):

        utilizador_1 = models.Utilizador.objects.get(pk=id_utilizador_env)
        utilizador_2 = models.Utilizador.objects.get(pk=id_utilizador_rec)

        pedido = models.PedidoAmizade.objects.create(
        id_utilizador_env=utilizador_1,
        id_utilizador_recebe=utilizador_2)

        if pedido != None:
            return True
        return False
    

    def obter_pedidos_amizade(self, id_utilizador):

        pedidos_amizade = []
        utilizador = models.Utilizador.objects.get(pk=id_utilizador)
        pedidos = models.PedidoAmizade.objects.filter(id_utilizador_recebe=utilizador)
        for p in pedidos:
            pedidos_amizade.append(p.id_utilizador_env.pk)
        return pedidos_amizade


    #remover pedido amizade
    #criar amizade

    def remover_pedido_amizade(self, id_utilizador_env, id_utilizador_rec):

        utilizador_env = models.Utilizador.objects.get(pk=id_utilizador_env)
        utilizador_rec = models.Utilizador.objects.get(pk=id_utilizador_rec)

        pedido = models.PedidoAmizade.objects.get(id_utilizador_env=utilizador_env, id_utilizador_recebe = utilizador_rec)
        pedido.delete()
    
    def criar_amizade(self, id_utilizador_1, id_utilizador_2):

        utilizador_1 = models.Utilizador.objects.get(pk=id_utilizador_1)
        utilizador_2 = models.Utilizador.objects.get(pk=id_utilizador_2)

        amizadeutilizador = models.Amizade.objects.create(id_utilizador_1=utilizador_1,id_utilizador_2=utilizador_2)
        if amizadeutilizador!=None:
            return True
        else:
            return False


    
'''
    @property
    def pedidos_amizade(self):
        return self.__pedidos_amizades


'''