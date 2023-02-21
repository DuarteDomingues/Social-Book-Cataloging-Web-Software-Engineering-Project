from dominio.servicos.servico_critica import ServicoCritica


class TesteCritica():

      def __init__(self, rep_criticas):

        self.__rep_criticas = rep_criticas

        serv_critica = ServicoCritica(self.__rep_criticas)
        serv_critica.pedir_adicionar_critica( 1, 1, "gostei", 3)

        self.__criticas_livro = serv_critica.pedir_criticas_livro(1,3)
      
      def correr_teste(self):

        if ((len(self.__criticas_livro)>2) and self.__criticas_livro[0].texto == "gostei do livro, achei muito bom"
        and self.__criticas_livro[0].id_livro==1 and self.__criticas_livro[1].id_critica==2 and self.__criticas_livro[1].id_utilizador==1
        and self.__criticas_livro[2].texto == "gostei"):
          return True
        else:
          return False


    