from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bookcrew.utils.utils import API_KEY
from bookcrew import models
from bookcrew.dominio.entidades.livro import Livro
import requests

class RepositorioLivro():

    def __init__(self):
        
        self.__servico = build('books', 'v1', developerKey=API_KEY)


    def obter_livro(self, id_livro):
        
            try:
                livro = self.__servico.volumes().get(volumeId = id_livro).execute()
                

                titulo, autor, genero, num_pag ,desc, ref_foto = self.__obter_campos_livro_valid(livro)           
                livro_resultado = Livro(id_livro, titulo, autor, genero, 0, num_pag ,desc, ref_foto)
                return livro_resultado
            
            except HttpError as error:
                print(f'An error occurred: {error}')
                return None

    
        
    def obter_livros(self, nome_livro, max_resultados):

        livros_resultantes = []
        try:
            livros = self.__servico.volumes().list(q=nome_livro, maxResults=max_resultados).execute()
            if livros!=None:
                for livro in livros['items']:
                    
                    titulo, autor, genero, num_pag ,desc, ref_foto = self.__obter_campos_livro_valid(livro)
                    livro_resultado = Livro(livro['id'], titulo, autor, genero, 0, num_pag ,desc, ref_foto)
                    livros_resultantes.append(livro_resultado)
                    
            return livros_resultantes
        
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
    
    def __obter_campos_livro_valid(self, livro):

        titulo = "" 
        autor = "" 
        genero = ""
        num_pag = 0
        desc = "" 
        ref_foto = "" 

        if 'authors' in livro['volumeInfo']:
            if len(livro['volumeInfo']['authors'])!=0:
                autor = livro['volumeInfo']['authors'][0]
                    
        if 'categories' in livro['volumeInfo']:
                if len(livro['volumeInfo']['categories'][0])!=0:
                    genero = livro['volumeInfo']['categories'][0]
        
        if 'title' in livro['volumeInfo']:
            titulo = livro['volumeInfo']['title']
        
        if 'pageCount' in livro['volumeInfo']:
            num_pag = livro['volumeInfo']['pageCount']
        
        if 'description' in livro['volumeInfo']:
            desc = livro['volumeInfo']['description']
        
        if 'imageLinks' in livro['volumeInfo']:
            if 'thumbnail' in livro['volumeInfo']['imageLinks']:
                ref_foto = livro['volumeInfo']['imageLinks']['thumbnail']
            else:   
                ref_foto = "default"
     
        else:
            ref_foto = "default"
        
        

        return titulo, autor, genero, num_pag ,desc, ref_foto
    
    def obter_livro_lista_livros(self, livros_ids):

        livros = []
        for livro_id in livros_ids:
            livros.append(self.obter_livro(livro_id))
        
        return list(set(livros))
    
    









    
