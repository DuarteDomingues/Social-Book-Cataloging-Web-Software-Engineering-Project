'''
from django.urls import path
from . import views
from view_controlador.view_controlador_livro import ViewControladorLivro 
from view_controlador.view_controlador_critica_comp import ViewControladorCriticaComp
from view_controlador.view_controlador_pesquisa import ViewControladorPesquisa
from view_controlador.view_controlador_utilizador import ViewControladorUtilizador
from view_controlador.view_controlador_pagina_principal import ViewControladorPrincipal

urlpatterns = [
    path("", ViewControladorPrincipal().view_principal, name="index"),
    path("critica_comp/<int:id_critica>", ViewControladorCriticaComp().view_critica_completa, name="critica_comp"),
      path("pesquisa", ViewControladorPesquisa(cona=None).view_pesquisa, name="pesquisa"),
      #path("livro", views.livro, name="livro"),
      path("utilizador", ViewControladorUtilizador().view_utilizador, name="utilizador"),
      path("colecao", views.colecao, name="colecao"),
      path("livro/<str:id_livro>", ViewControladorLivro().view_livro, name="livro"),

]

'''