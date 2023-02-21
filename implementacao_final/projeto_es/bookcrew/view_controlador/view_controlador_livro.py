from django.shortcuts import render,HttpResponseRedirect
from bookcrew.dominio.servicos.servico_livro import ServicoLivro

from django import forms
from django.urls import reverse
from bookcrew.utils.utils import forms_barra_top


class AdicionarLivroForm(forms.Form):

    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'comment'}),label='', required=True)
    classificao = forms.IntegerField(min_value=1, max_value=5, required=True, error_messages={'required': 'Classification is required'})

class AdicionarColecaoForm(forms.Form):
    COLECAO_ESCOLHAS=[
    (0, 'Already read'),
    (1, 'Reading'),
    (2, 'Want to read'),
    ]
    val = forms.CharField(widget=forms.Select(choices=COLECAO_ESCOLHAS),required=True)

#novo FORM para adicionar

class ViewControladorLivro:

    def __init__(self):
        
        self.__servico_livro= ServicoLivro()
        self.__num_criticas = 5

    def view_livro(self,request,id_livro):

        livro, criticas, info_utilizadores = self.__servico_livro.obter_info_livro(id_livro, self.__num_criticas)
        livro_col = self.__servico_livro.pedir_verificar_livro_colecao(id_livro, request.session['id_utilizador'])

        if request.method == 'POST':
            form = AdicionarLivroForm(request.POST)
            formbutao = AdicionarColecaoForm(request.POST)
            if form.is_valid():
                mensagem = form.cleaned_data['mensagem']
                classificao = form.cleaned_data['classificao']
              
                self.__servico_livro.pedir__adicionar_critica(livro.id_livro,request.session['id_utilizador'],mensagem,classificao)
                return HttpResponseRedirect(request.path)

            if formbutao.is_valid():
                val_col = formbutao.cleaned_data['val']
                self.__servico_livro.pedir_adicionar_livro_colecao(livro.id_livro,int(val_col),request.session['id_utilizador'])
                return HttpResponseRedirect(reverse('colecao', args=[request.session['id_utilizador']]))

            red = forms_barra_top(request)
            if red!=None:
                return red
         
        
        else: 
            form = AdicionarLivroForm()
            formbutao = AdicionarColecaoForm(request.POST)



        
        return render(request, 'livro.html',{"livro": livro,"criticas": criticas,"info_utilizadores":info_utilizadores,"form":form,
        "formbutao":formbutao,"livro_col":livro_col})
    

