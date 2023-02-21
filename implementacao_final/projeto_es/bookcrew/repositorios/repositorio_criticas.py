from bookcrew import models
from bookcrew.dominio.entidades.critica import Critica
from datetime import date


class RepositorioCriticas:


    def obter_critica(self, id_critica):

        critica_model = models.Critica.objects.get(pk=id_critica)

        if critica_model != None:
            critica = Critica(critica_model.id_critica,critica_model.id_livro,critica_model.id_utilizador.pk,
            critica_model.texto,critica_model.data,critica_model.num_gostos,critica_model.classif)
            return critica
        else: 
            return None


    def obter_criticas_livro(self, id_livro, num_criticas):

        criticas_obtidas=[]
        criticas = models.Critica.objects.filter(id_livro=id_livro).all()[:num_criticas]
        if criticas!=None:
            for critica in criticas:
                print("id_user ",critica.id_utilizador.pk)
                nova_critica = Critica(critica.id_critica,critica.id_livro,critica.id_utilizador.pk,
                critica.texto,critica.data,critica.num_gostos,critica.classif)
                criticas_obtidas.append(nova_critica)
        
        return criticas_obtidas


    
    #obter por ordem de tempo
    def obter_criticas_utilizadores(self, utilizadores, num_criticas):

        criticas_res = []

        #.latest('data')[:num_criticas]
        
        criticas = models.Critica.objects.filter(id_utilizador__pk__in=utilizadores)[:num_criticas]

        if criticas!=None:        
            for critica in criticas:
                nova_critica = Critica(critica.id_critica,critica.id_livro,critica.id_utilizador.pk,
                critica.texto,critica.data,critica.num_gostos,critica.classif)
                criticas_res.append(nova_critica)
        
            return criticas_res

        return None

    
    def adicionar_critica(self, id_livro, id_utilizador, texto, classif):

        util = models.Utilizador.objects.get(pk=id_utilizador)
        curr_data = str(date.today())
        critica = models.Critica.objects.create(id_utilizador=util,id_livro=id_livro,texto=texto,data=curr_data,num_gostos=0,classif=classif)
        if critica!=None:
            return True
        else:
            return False






    
