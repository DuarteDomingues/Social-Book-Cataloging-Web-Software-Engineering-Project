from dominio.entidades.info_utilizador import InfoUtilizador

class RepositorioUtilizadores():

    def __init__(self):
        
        #atributos de teste, seria uma tabela sql
        self.__utilizadores = []
        self.__amizades = [] #id_utilizador_1, id_utilizador_2
        self.__pedidos_amizades = [] #(id_utilizador_env, id_utilizador_recebe)

        self.__popular_repositorio()

        #self.__utilizadores = [(1, "dudao", "foto_dudao","beep boop"), (0, "boy_piqueno", "foto_boi","beep beep"), (2, "fons", "foto","talarico maister")]
        #self.__amizades = [(1,0),[1,2]] #id_utilizador_1, id_utilizador_2
        #self.__pedidos_amizades = [] #(id_utilizador_env, id_utilizador_recebe)
    
    def obter_info_utilizador(self, id_utilizador):
        info_utilizador = None
        for u in self.__utilizadores:
            if u[0] == id_utilizador:
                info_utilizador = InfoUtilizador(u[0], u[1], u[2], u[3])
        return info_utilizador
    
    def obter_utilizadores(self, nome_utilizador):
        
        utilizadores_encontrados = []
        for u in self.__utilizadores:
            nome_u_min = u[1].lower()
            if  str.__contains__(nome_u_min, (nome_utilizador)):
                utilizador_encontrado = InfoUtilizador(u[0], u[1], u[2], u[3])
                utilizadores_encontrados.append(utilizador_encontrado)
        return utilizadores_encontrados
    
    def obter_amizades(self, id_utilizador):
        
        amizades=[]
        for u in self.__amizades:
            if id_utilizador in u:
                    if u[0] == id_utilizador:
                        amizades.append(u[1])
                    elif u[1] == id_utilizador:
                        amizades.append(u[0])
        return amizades
    
    def enviar_pedido_amizade(self, id_utilizador_env, id_utilizador_rec):

        for pedido in self.__pedidos_amizades:
            if pedido[0] == id_utilizador_env and pedido[1] == id_utilizador_rec:
                return False
        self.__pedidos_amizades.append((id_utilizador_env, id_utilizador_rec))
        return True
    
    def obter_pedidos_amizade(self, id_utilizador):

          
        pedidos=[]
        for pedido in self.__pedidos_amizades:
            if id_utilizador in pedido:
                    if id_utilizador == pedido[1]:
                        pedidos.append(pedido[0])
        return pedidos
    
    
    def __popular_repositorio(self):
        self.__utilizadores = [(1, "dudao", "foto_dudao","beep boop"), (0, "boy_piqueno", "foto_boi","beep beep"), (2, "baba", "foto","talarico maister")]
        self.__amizades = [(1,0),[0,2]] #id_utilizador_1, id_utilizador_2
        self.__pedidos_amizades = [] #(id_utilizador_env, id_utilizador_recebe)
    
    def print_dados(self):

        print("-------------- Utilizadores ---------------------------")
        for utilizador in self.__utilizadores:

            print("id_utilizador:", utilizador[0], ", nome utilizador:", utilizador[1],", foto:", utilizador[2], ", descricao:", utilizador[3]  )
        
        print("-------------- Amizades ---------------------------")
        for amizades in self.__amizades:
            print("utilizador_1:", amizades[0], "utilizador_2:", amizades[1])
        
        print("-------------- Pedidos Amizade ---------------------------")
        for pedidos in self.__pedidos_amizades:
            print("utilizador enviou:", pedidos[0], "utilizador recebeu:", pedidos[1])
        print("----------------------------------------------")

        



    



        

