from dominio.servicos.servico_livro import ServicoLivro



class TesteLivro:

    def __init__(self, rep_livros):


        ##Inicializar repositorios
        self.__rep_livros = rep_livros
    

        serv_livro = ServicoLivro(self.__rep_livros)
        self.__livro_um = serv_livro.pedir_livro(1)
        self.__livros_nome = serv_livro.pedir_livros_nome("No")
    
    def correr_teste(self):

        if ( self.__livro_um.id_livro ==1 and self.__livro_um.titulo =="O Processo" 
        and self.__livro_um.autor =="Franz Kafka" and self.__livro_um.genero == "Romance" and self.__livro_um.num_pag == 200 
        and self.__livro_um.desc != "" and (len(self.__livros_nome)!=None) and self.__livros_nome[0].id_livro==2):
            return True
        
        else:
            return False
        




