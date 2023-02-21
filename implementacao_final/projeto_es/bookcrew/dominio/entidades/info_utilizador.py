
class InfoUtilizador():

    def __init__(self,id_utilizador, nome_utilizador, ref_foto, descricao):
        self.__id_utillizador = id_utilizador
        self.__nome_utilizador = nome_utilizador
        self.__ref_foto = ref_foto
        self.__desc = descricao

    @property
    def id_utilizador(self):
        return self.__id_utillizador
    
    @property
    def nome_utilizador(self):
        return self.__nome_utilizador

    @property
    def descricao(self):
        return self.__desc
    
    @property
    def ref_foto(self):
        return str(self.__ref_foto)[16:]