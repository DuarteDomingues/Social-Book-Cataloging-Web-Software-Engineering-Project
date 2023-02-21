
class Colecao():

    def __init__(self, id_utilizador, lista_ler=[], lista_ja_leu=[], lista_a_ler=[]):
        self.__id_utilizador = id_utilizador
        self.__lista_ler = lista_ler
        self.__lista_ja_leu = lista_ja_leu
        self.__lista_a_ler = lista_a_ler
    
    @property
    def id_utilizador(self):
        return self.__id_utilizador
    
    @property
    def lista_ler(self):
        return self.__lista_ler
    
    @property
    def lista_ja_leu(self):
        return self.__lista_ja_leu
    
    @property
    def lista_a_ler(self):
        return self.__lista_a_ler
    
    def adicionar_lista_ler(self, livro_colecao):
        if livro_colecao not in self.__lista_ler:

            self.__lista_ler.append(livro_colecao)
    
    def adicionar_lista_ja_leu(self, livro_colecao):
        if livro_colecao not in self.__lista_ja_leu:

            self.__lista_ja_leu.append(livro_colecao)
    
    def adicionar_lista_a_ler(self, livro_colecao):
        if livro_colecao not in self.__lista_ja_leu:

            self.__lista_ja_leu.append(livro_colecao)

