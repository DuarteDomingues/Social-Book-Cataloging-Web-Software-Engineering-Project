from bookcrew.repositorios.repositorio_utilizadores import  RepositorioUtilizadores

class ServicoUtilizador:


    def __init__(self):
        self.__rep_utilizadores = RepositorioUtilizadores()
    

    def pedir_info_utilizador(self, id_utilizador):

        return self.__rep_utilizadores.obter_info_utilizador(id_utilizador)
    
    def pedir_info_utilizadores(self, id_utilizadores):

        return self.__rep_utilizadores.obter_info_utilizadores(id_utilizadores)
    

    def obter_ids_lista_utilizadores(self, utilizadores):

        ids=[]
        if utilizadores != None:
            for utl in utilizadores:
                ids.append(utl.id_utilizador)
        
        return list(set(ids))
    

    def pedir_criar_amizade(self,id, id_utl):

        self.__rep_utilizadores.remover_pedido_amizade(id, id_utl)
        self.__rep_utilizadores.criar_amizade(id, id_utl)
        return True

    
    def pedir__amizades(self, id_utl):
        return self.__rep_utilizadores.obter_amizades(id_utl)
    
    def pedir_pedidos_amizade(self, id_utl):
        return self.__rep_utilizadores.obter_pedidos_amizade(id_utl)
    
    
    def obter_amizades_ids(self,utilizadores ):
        ids=[]
        if utilizadores != None:
            for utl in utilizadores:
                ids.append(utl.id_utilizador)
        
        return list(set(ids))
    
    def pedir_enviar_ped_amizade(self, id_utilizador_env, id_utilizador_rec):
        return self.__rep_utilizadores.enviar_pedido_amizade(id_utilizador_env, id_utilizador_rec)
    

    



