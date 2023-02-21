from dominio.entidades.critica import Critica
from datetime import date

class RepositorioCriticas:

    def __init__(self):
        
        #atributos de teste, seria tabelas sql
        #(id_critica, id_livro, id_utilizador,texto, data, num_gostos,classif)
        self.__criticas = []
        self.__popular_repositorios()
    
    def obter_criticas_livro(self, id_livro, num_criticas):

        criticas = []
        c=0
        for i in range (len(self.__criticas)):
            if self.__criticas[i][1] == id_livro and c <num_criticas:
                nova_critica = Critica(self.__criticas[i][0],self.__criticas[i][1],self.__criticas[i][2],
                self.__criticas[i][3],self.__criticas[i][4],self.__criticas[i][5])
                criticas.append(nova_critica)
                c=c+1
            
        return criticas
    
    #obter por ordem de tempo
    def obter_criticas_amigos(self, amigos, num_criticas):

        criticas = []
        c=0
        for i in range(len(self.__criticas)):
            for amigo in amigos:
                if self.__criticas[i][2] == amigo and c < num_criticas:
                    nova_critica = Critica(self.__criticas[i][0],self.__criticas[i][1],self.__criticas[i][2],
                    self.__criticas[i][3],self.__criticas[i][4],self.__criticas[i][5])
                    criticas.append(nova_critica)
                    c=c+1 

        return criticas
    
    def adicionar_critica(self, id_livro, id_utilizador, texto, classif):

        idx = len(self.__criticas)+1
        curr_data = str(date.today())
        critica = (idx, id_livro, id_utilizador, texto,curr_data,0,classif)
        self.__criticas.append(critica)
    
    def __popular_repositorios(self):

        self.__criticas = [(1,1,1,"gostei do livro, achei muito bom", "22-08-2022", 4), (2,1,1,"não gostei do final", "21-08-2022", 2)]
    
    def print_dados(self):
        
        print("-------------- Criticas ---------------------------")
        for critica in self.__criticas:
            print("id_critica:", critica[0], ", id_utilizador:", critica[1], ", texto:", critica[2], ", data:",critica[3],
            ", num gostos", critica[4], ", classificacao", critica[5] )


        # id_livro, id_utilizador,texto, data, num_gostos,classif)







    
