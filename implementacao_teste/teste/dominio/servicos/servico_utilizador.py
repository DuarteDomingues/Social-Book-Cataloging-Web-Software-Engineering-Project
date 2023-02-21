from repositorios.repositorio_utilizadores import RepositorioUtilizadores

class ServicoUtilizador:

    def __init__(self, rep_utilizadores):
        #self.__rep_utilizadores = RepositorioUtilizadores()
        self.__rep_utilizadores = rep_utilizadores
    
    def pedir_envio_pedido_amizade(self, id_utilizador_env, id_utilizador_rec):

        self.__rep_utilizadores.enviar_pedido_amizade(id_utilizador_env, id_utilizador_rec)
    
    def pedir_info_utilizador(self, id_utilizador):

        return self.__rep_utilizadores.obter_info_utilizador(id_utilizador)
    
    def pedir_lista_amigos(self, id_utilizador):

        return self.__rep_utilizadores.obter_amizades(id_utilizador)
    
    def pedir_pedidos_amizade(self, id_utilizador):

        return self.__rep_utilizadores.obter_pedidos_amizade(id_utilizador)
    
    def pedir_info_utilizadores(self, id_utilizadores):

        info_utilizadores=[]
        for id in id_utilizadores:
            info_utilizador = self.__rep_utilizadores.obter_info_utilizador(id)
        return info_utilizadores
    
    def pedir_utilizadores_nome(self, nome_utilizadores):
        return self.__rep_utilizadores.obter_utilizadores(nome_utilizadores)
    
    def ordenar_utilizadores_decrescente(self, utilizadores):
        return None

