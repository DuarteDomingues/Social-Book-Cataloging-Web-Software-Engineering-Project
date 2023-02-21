from django.shortcuts import render
from bookcrew.utils.utils import forms_barra_top
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bookcrew.dominio.servicos.servico_livro import ServicoLivro

class ViewControladorPesquisa:

    def __init__(self):
        self.__serv_livros = ServicoLivro()
        self.__num_pesquisas = 5
    
    def view_pesquisa(self, request):
        

        if request.method == "GET":

            titulo = request.GET.get("q")

            if titulo != "" and titulo!=None :

                livros = self.__serv_livros.pedir_livros(titulo, self.__num_pesquisas)
                return render(request,"pesquisa.html", {"livros":livros,"num": self.__num_pesquisas})

            else: 
                return render(request,"pesquisa.html")

        
        if request.method == "POST":

            red = forms_barra_top(request)
            if red!=None:
                return red

        return render(request,"pesquisa.html")


