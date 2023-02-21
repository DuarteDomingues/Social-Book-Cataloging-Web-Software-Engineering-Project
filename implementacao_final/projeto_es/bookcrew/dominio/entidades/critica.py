from datetime import datetime

class Critica:

    def __init__(self, id_critica, id_livro, id_utilizador,texto, data, num_gostos=0,classif=0):
        self.__id_critica = id_critica
        self.__texto = texto
        self.__data = data
        self.__num_gostos = num_gostos
        self.__id_livro = id_livro
        self.__id_utilizador = id_utilizador
        self.__classif = classif
    
    @property
    def id_critica(self):
        return self.__id_critica
    
    @property
    def texto(self):
        return self.__texto
    
    @property
    def data(self):
        return self.__data
    
    @property
    def num_gostos(self):
        return self.__num_gostos
    
    @property
    def id_livro(self):
        return self.__id_livro
    
    @property
    def id_utilizador(self):
        return self.__id_utilizador
    
    @property
    def classif(self):
        return self.__classif
    
    def data_para_date(self):
        self.__data = datetime.strptime(self.__data, self.__data_format) 