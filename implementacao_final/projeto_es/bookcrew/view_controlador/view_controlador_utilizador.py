from django.shortcuts import render
from bookcrew.view_controlador.view_controlador_colecao import ViewControladorColecao
from bookcrew.utils.utils import forms_barra_top
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from bookcrew.dominio.servicos.servico_utilizador import ServicoUtilizador



class ViewControladorUtilizador:

    def __init__(self):
        self.__view_col = ViewControladorColecao()
        self.__serv_utl = ServicoUtilizador()
    
    def view_utilizador(self, request, id_utilizador):

        utilizador_info = self.__serv_utl.pedir_info_utilizador(id_utilizador)

        utilizadores_amizades = self.__serv_utl.pedir__amizades(id_utilizador)
        utilizadores_pedidos, utilizadores_ids = self.__obter_pedidos_amizade(request, id_utilizador)

        opcao = self.ver_amizade(request, id_utilizador)

        if request.method == "POST":

            red = forms_barra_top(request)
            if red!=None:
                return red
            

            if 'butao_ped_amizade' in request.POST:
                self.__serv_utl.pedir_enviar_ped_amizade(request.session['id_utilizador'],id_utilizador)
            
            if utilizadores_ids!=None:
                for id in utilizadores_ids:
                    if str(id) in request.POST:
                      
                        self.__serv_utl.pedir_criar_amizade(id, request.session['id_utilizador'])
                        return HttpResponseRedirect(request.path)

        
        return render(request,"utilizador.html",{"utilizador_info":utilizador_info, "opcao": opcao, "utilizadores":utilizadores_amizades,
        "utilizadores_pedidos": utilizadores_pedidos})


    def ver_amizade(self, request, id_utilizador):
        
        
        if request.session['id_utilizador'] != id_utilizador:
            
            if id_utilizador in self.__serv_utl.pedir__amizades(request.session['id_utilizador']):
                
                return 0
            else:
                print("PEDIDOS ",request.session['id_utilizador'] in self.__serv_utl.pedir_pedidos_amizade(id_utilizador))

                if request.session['id_utilizador'] in self.__serv_utl.pedir_pedidos_amizade(id_utilizador):
                    print("enviado")
                    return 1
                
                else:
                    print("enviar")
                    return 2
    
    
    def __obter_pedidos_amizade(self, request, id_utilizador):

        if request.session['id_utilizador'] == id_utilizador:

            utilizadores_ids = self.__serv_utl.pedir_pedidos_amizade(request.session['id_utilizador'])
            utilizadores = self.__serv_utl.pedir_info_utilizadores(utilizadores_ids)
            return utilizadores, utilizadores_ids
        else:
            return None, None

    
    #obter info _ utilizador
    #obter colecao