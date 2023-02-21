"""projeto_es URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookcrew import views
from bookcrew.view_controlador.view_controlador_livro import ViewControladorLivro
from bookcrew.view_controlador.view_controlador_pagina_principal import ViewControladorPrincipal
from bookcrew.view_controlador.view_controlador_critica_comp import ViewControladorCriticaComp
from bookcrew.view_controlador.view_controlador_colecao import ViewControladorColecao
from bookcrew.view_controlador.view_controlador_pesquisa import ViewControladorPesquisa
from bookcrew.view_controlador.view_controlador_utilizador import ViewControladorUtilizador

urlpatterns = [
    
    path("", views.login_view),
    path("home", ViewControladorPrincipal().view_principal, name="index"),
    path("critica_comp/<int:id_critica>", ViewControladorCriticaComp().view_critica_completa, name="critica_comp"),
   # path("livro", views.livro, name="livro"),
    path("pesquisa", ViewControladorPesquisa().view_pesquisa, name="pesquisa"),
    path("colecao/<int:id_utilizador>", ViewControladorColecao().view_colecao, name="colecao"),
    path("utilizador/<int:id_utilizador>", ViewControladorUtilizador().view_utilizador, name="utilizador"),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path("livro/<str:id_livro>", ViewControladorLivro().view_livro, name="livro"),
    path("teste", views.livro, name="xd")

]
