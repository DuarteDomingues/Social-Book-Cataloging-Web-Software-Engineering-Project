from bookcrew import models
from bookcrew.dominio.entidades.colecao import Colecao
from datetime import date


class RepositorioColecao:


    def adicionar_livro_colecao(self, id_livro, categoria, id_utilizador):

        if models.Colecao.objects.filter(id_utilizador=id_utilizador).exists():
            colecao_livro = models.Colecao.objects.get(id_utilizador=id_utilizador)

            subcolecao = models.Subcolecao.objects.create(id_colecao=colecao_livro,id_livro=id_livro,
            categoria=categoria)
            if subcolecao!=None:
                return True
        
        else:
            self.criar_colecao(id_utilizador)

            colecao_livro = models.Colecao.objects.get(id_utilizador=id_utilizador)

            subcolecao = models.Subcolecao.objects.create(id_colecao=colecao_livro,id_livro=id_livro,
            categoria=categoria)
            if subcolecao!=None:
                return True

        return False

    def criar_colecao(self,id_utilizador):
        utilizador = models.Utilizador.objects.get(id_utilizador=id_utilizador)
        models.Colecao.objects.create(id_utilizador=utilizador)


    
    def remover_livro_colecao(self, id_livro, categoria, id_utilizador):

        utilizador = models.Utilizador.objects.get(id_utilizador=id_utilizador)
        colecao_livro = models.Colecao.objects.get(id_utilizador=utilizador)
        id_colecao = colecao_livro.id_colecao
        if colecao_livro!=None:
            subcolecao = models.Subcolecao.objects.get(id_livro=id_livro, id_colecao=id_colecao, categoria=categoria)
            subcolecao.delete()
            return True

        return False
    
    def verificar_livro_colecao(self, id_livro, id_utilizador):

        col = Colecao(id_utilizador)
        colecao_livro = models.Colecao.objects.get(id_utilizador = id_utilizador)
        if colecao_livro!=None:
            #obter todas as tabelas Subcolecao em que têm a colecao_livro
            subcolecoes = models.Subcolecao.objects.filter(id_colecao=colecao_livro.pk)
            for sub in subcolecoes:
                if sub.id_livro == id_livro:
                    return 0
                elif sub.id_livro == id_livro:
                    return 1
                elif sub.id_livro == id_livro:
                    return 3
                    
        return None
    
    def obter_colecao_utilizador(self, id_utl):
        
        col = Colecao(id_utl)
        colecao_livro = models.Colecao.objects.get(id_utilizador = id_utl)
        if colecao_livro!=None:
            #obter todas as tabelas Subcolecao em que têm a colecao_livro
            subcolecoes = models.Subcolecao.objects.filter(id_colecao=colecao_livro.pk)
            for sub in subcolecoes:
                if sub.categoria == 0:
                    print("0")
                    col.adicionar_lista_ler(sub.id_livro)
                elif sub.categoria == 1:
                    print("1")
                    col.adicionar_lista_ja_leu(sub.id_livro)
                elif sub.categoria == 2:
                    print("2")
                    col.adicionar_lista_a_ler(sub.id_livro)
                    
        return col


