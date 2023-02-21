from django.shortcuts import render
from bookcrew.dominio.servicos.servico_colecao import ServicoColecao
from bookcrew.utils.utils import forms_barra_top
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from bookcrew.utils.colecao_val import Colecoes

from django.forms import HiddenInput


class ViewControladorColecao:

    def __init__(self):
        self.__serv_col = ServicoColecao()


    def obter_info_colecao(self, id_utilizador):

        col = self.__serv_col.pedir_col_utilizador(id_utilizador)
        col = self.__serv_col.atualizar_col(col)
        
        return col

    def view_colecao(self, request, id_utilizador):

        col = self.obter_info_colecao(id_utilizador)

        if request.method == "POST":
            red = forms_barra_top(request)
            if red!=None:
                return red
            
            #self.__remover__colecao(request, col.lista_ler, col.lista_ja_leu, col.lista_a_ler)
            self.__remover__colecao(request, col)


        return render(request, 'colecao.html',{"lista_ler": col.lista_ler,"lista_ja_leu": col.lista_ja_leu,"lista_a_ler":col.lista_a_ler})
    


    def __remover__colecao(self, request, col):
        
        if 'butao_read' in request.POST:
            id_livro  = str(request.POST.get("hid_read"))

            self.__serv_col.pedir_remover_livro_colecao(id_livro, Colecoes.LER.value, request.session['id_utilizador'])
            col.lista_ja_leu.pop()


            return HttpResponseRedirect(request.path)

        if 'butao_reading' in request.POST:
            id_livro  = str(request.POST.get("hid_reading"))

            self.__serv_col.pedir_remover_livro_colecao(id_livro, Colecoes.A_LER.value, request.session['id_utilizador'])
            col.lista_ler.pop()


            return HttpResponseRedirect(request.path)


        if 'butao_want_read' in request.POST:
                id_livro  = str(request.POST.get("hid_want"))

                self.__serv_col.pedir_remover_livro_colecao(id_livro, Colecoes.A_LER.value, request.session['id_utilizador'])
                col.lista_a_ler.pop()


                return HttpResponseRedirect(request.path)






