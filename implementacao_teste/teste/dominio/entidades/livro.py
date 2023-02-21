
class Livro:

    def __init__(self, id_livro, titulo=None, autor=None, genero=None, classif=None, num_pag=None, desc=None, ref_foto=None):
        self.__id_livro = id_livro
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__classif = classif
        self.__num_pag = num_pag
        self.__desc = desc
        self.__ref_foto = ref_foto
    
    @property
    def id_livro(self):
        return self.__id_livro
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def classif(self):
        return self.__classif
    
    @property
    def num_pag(self):
        return self.__num_pag
    
    @property
    def desc(self):
        return self.__desc
    
    @property
    def ref_foto(self):
        return self.__ref_foto
    
