from django.shortcuts import render,redirect
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from . import models
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from bookcrew.repositorios.repositorio_utilizadores import RepositorioUtilizadores
from bookcrew.repositorios.repositorio_colecao import RepositorioColecao


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

rep__utilizadores = RepositorioUtilizadores()
rep_colecao = RepositorioColecao()

def login_view(request):

    if 'id_utilizador' in request.session:
        return redirect("index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                request.session['name'] = username
                messages.info(request, f"You are now logged in as {username}.")

                id_utilizador = rep__utilizadores.obter_id_utilizador(username)
                request.session['id_utilizador'] = id_utilizador

                return redirect("index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})



def register_view(request):
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )

            nome= form.cleaned_data.get('username')
            id_utilizador = rep__utilizadores.criar_utilizador(nome)
            rep_colecao.criar_colecao(id_utilizador)
            rep__utilizadores.criar_amizade(id_utilizador, 1)
            
            request.session['id_utilizador'] = id_utilizador
            #criar utilizador
            #obter id utilizador
            #guardar o id do utilizador na sessao

            return redirect('index')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


#na pagina de login, ver se o utilizador tem sessao
#se utilizador tem sessao vai logo para o index
#senao fica no login


def livro(request):
    # Obtain the API key
    api_key = "AIzaSyCmWw59Suh32pASTs-7LEv650k2cQxrHeg"

    # Build the client object
    service = build('books', 'v1', developerKey=api_key)
    
    # Call the API
    try:
       # query = request.POST['query']
        results = service.volumes().list(q='python', maxResults=5).execute()

        #book_id = 'H9emM_LGFDEC'

        #book = models.Colecao.objects.get(id_livro = book_id )
        #results = service.volumes().get(volumeId=book.id_livro).execute()
        print(results['id'])

    except HttpError as error:
        print(f'An error occurred: {error}')
        books = None
    
    # Render the search results template
    return render(request, 'livro.html')


#LqmaDwAAQBAJ
#pMEUG8oNBfkC  
#H9emM_LGFDEC
#LqmaDwAAQBAJ



#obterLivro
#obterCriticas
#obterInfoUtilizadores
#criarCritica
#adicionarColecao
#removerColecao

