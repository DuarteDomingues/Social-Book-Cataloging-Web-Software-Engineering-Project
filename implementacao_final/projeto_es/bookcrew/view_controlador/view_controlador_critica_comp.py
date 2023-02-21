from django.shortcuts import render, HttpResponseRedirect,redirect
from django.urls import reverse
from django import forms
from bookcrew.utils.utils import forms_barra_top
from bookcrew.dominio.servicos.servico_livro import ServicoLivro
from bookcrew.dominio.servicos.servico_critica import ServicoCritica
from bookcrew.dominio.servicos.servico_utilizador import ServicoUtilizador

from bookcrew.view_controlador.forms.forms_globais import FormBarra


class AdicionarComentarioForm(forms.Form):
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comment...'}),label='')


class ViewControladorCriticaComp:

    def __init__(self):
     
        self.__servico_critica = ServicoCritica()
        self.__servico_livro = ServicoLivro()
        self.__serv_utilizador = ServicoUtilizador()

    def __obter_info_critica_comp(self, id_critica):

        critica = self.__servico_critica.pedir_critica(id_critica)
        livro = self.__servico_livro.pedir_livro(critica.id_livro)

        utilizador = self.__serv_utilizador.pedir_info_utilizador(critica.id_utilizador)

        comentarios = self.__servico_critica.pedir_comentarios(id_critica)

        utilizadores_ids = self.__servico_critica.obter_ids_utilizadores_comentarios(comentarios)

        utilizadores_info = self.__serv_utilizador.pedir_info_utilizadores(utilizadores_ids)

        return critica,livro,utilizador,comentarios, utilizadores_info
        #comentarios obter utilizadores_ids dos comentarios



    def view_critica_completa(self,request,id_critica):

        critica,livro,utilizador,comentarios,utilizadores_info = self.__obter_info_critica_comp(id_critica)

        if request.method == 'POST':
            form = AdicionarComentarioForm(request.POST)
            if form.is_valid():
                mensagem = form.cleaned_data['mensagem']
                self.__servico_critica.pedir_adicionar_comentario(id_critica,utilizador.id_utilizador,mensagem)
                return HttpResponseRedirect(request.path)
            
            red = forms_barra_top(request)
            if red!=None:
                return red
        
        else: 
            form = AdicionarComentarioForm()
        
        
        return render(request, 'critica_completa.html',{"critica": critica,"livro": livro,"utilizador":utilizador,"comentarios":comentarios,
        "utilizadores_info":utilizadores_info,'form': form})

    
#fixar id_utilizador