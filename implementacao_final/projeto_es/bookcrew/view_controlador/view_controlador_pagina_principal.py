from django.shortcuts import render
from bookcrew.dominio.servicos.servico_livro import ServicoLivro
from bookcrew.dominio.servicos.servico_critica import ServicoCritica
from bookcrew.dominio.servicos.servico_utilizador import ServicoUtilizador

from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from bookcrew.view_controlador.forms.forms_globais import FormBarra
from bookcrew.utils.utils import forms_barra_top




class ViewControladorPrincipal:

    def __init__(self):
        self.__servico_critica = ServicoCritica()
        self.__servico_livro = ServicoLivro()
        self.__servico_utilizador = ServicoUtilizador()

        self.__num_criticas = 5
    

    def __obter_informacao_criticas(self, request):

        id_utilizador= request.session['id_utilizador']
        amigos = self.__servico_utilizador.pedir__amizades(id_utilizador)
        amigos_ids = self.__servico_utilizador.obter_ids_lista_utilizadores(amigos)

        criticas_amigos = self.__servico_critica.pedir_obter_criticas_utilizadores(amigos_ids, self.__num_criticas)
        criticas_livros_ids = self.__servico_critica.obter_livro_ids_criticas(criticas_amigos)

        livros = self.__servico_livro.pedir_livro_lista_livros(criticas_livros_ids)

        return amigos, criticas_amigos, livros



    def view_principal(self, request):

        amigos, criticas_amigos, livros = self.__obter_informacao_criticas(request)
       

        if request.method == "POST":
           
            red = forms_barra_top(request)
            if red!=None:
                return red

            return render(request, 'index.html',{"livros": livros,"criticas": criticas_amigos,"utilizadores":amigos})
        
        
        #obter amigos utilizador
        #obter criticas recentes dos amigos

        return render(request, 'index.html',
        {"livros": livros,"criticas": criticas_amigos,"utilizadores":amigos})

