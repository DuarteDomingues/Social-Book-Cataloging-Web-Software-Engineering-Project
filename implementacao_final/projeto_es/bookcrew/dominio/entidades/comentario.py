from datetime import datetime

class Comentario:

    def __init__(self, id_comentario, id_critica, id_utilizador, texto, data):
        self.__id_comentario = id_comentario
        self.__id_critica = id_critica
        self.__id_utilizador = id_utilizador
        self.__texto = texto
        self.__data = data
        self.__data_format= '%m-%d-%Y'
    
    @property
    def id_comentario(self):
        return self.__id_comentario
    
    @property
    def id_critica(self):
        return self.__id_critica
    
    @property
    def id_utilizador(self):
        return self.__id_utilizador
    
    @property
    def texto(self):
        return self.__texto
    
    @property
    def data(self):
        return self.__data
    
    def data_para_date(self):
        self.__data = datetime.strptime(self.__data, self.__data_format)
    
