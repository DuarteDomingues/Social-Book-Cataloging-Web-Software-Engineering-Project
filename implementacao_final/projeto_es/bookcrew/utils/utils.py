API_KEY = "AIzaSyCmWw59Suh32pASTs-7LEv650k2cQxrHeg"
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def forms_barra_top( request):

        if 'butao_casa' in request.POST:
            print("casa")
            return HttpResponseRedirect(reverse('index'))
        elif 'butao_colecao' in request.POST:
            print("colecao")
            return HttpResponseRedirect(reverse('colecao', args=[request.session['id_utilizador']]))
        
        elif 'butao_procura' in request.POST:
            print("procura")
            return HttpResponseRedirect(reverse('pesquisa'))

        elif 'butao_perfil' in request.POST:
            print("perfil")
            return HttpResponseRedirect(reverse('utilizador', args=[request.session['id_utilizador']]))

        else: 
            return None  





        