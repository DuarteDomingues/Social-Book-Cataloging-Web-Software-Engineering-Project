from dominio.servicos.servico_colecao import ServicoColecao


class TesteColecao:

    def __init__(self, rep_colecao):


        ##Inicializar repositorios
        self.__rep_colecao = rep_colecao
    

        serv_colecao = ServicoColecao(self.__rep_colecao)
        serv_colecao.pedir_adicionar_livro_colecao(1,1,1)

        self.__col = serv_colecao.pedir_colecao_utilizador(1)
    
    
    def correr_teste(self):

        if ( len(self.__col.lista_ja_leu)>0 and len(self.__col.lista_a_ler)==0 and self.__col.lista_ja_leu[0]==1
        and self.__col !=None):
            return True
        else:
            return False
        

    


