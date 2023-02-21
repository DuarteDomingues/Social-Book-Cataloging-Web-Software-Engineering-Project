from dominio.servicos.servico_utilizador import ServicoUtilizador


class TesteUtilizadores:

    def __init__(self, rep_utilizadores):


        ##Inicializar repositorios
        self.__rep_utilizadores = rep_utilizadores
    

        serv_utilizadores = ServicoUtilizador(self.__rep_utilizadores)

        self.__utilizadores_b = serv_utilizadores.pedir_utilizadores_nome("b")
        self.__amizades_1 = serv_utilizadores.pedir_lista_amigos(1)
        serv_utilizadores.pedir_envio_pedido_amizade(2,1)
        self.__lista_pedidos = serv_utilizadores.pedir_pedidos_amizade(1)


    
    
    def correr_teste(self):

        if ( ((len(self.__utilizadores_b)>1)) and  self.__utilizadores_b[0].nome_utilizador=="boy_piqueno" and
        self.__utilizadores_b[0].id_utilizador==0  and self.__utilizadores_b[1].id_utilizador==2 and
        self.__utilizadores_b[0].descricao=="beep beep" and len(self.__amizades_1)>0 and len(self.__lista_pedidos)>0):
            return True
        else:
            return False
        




