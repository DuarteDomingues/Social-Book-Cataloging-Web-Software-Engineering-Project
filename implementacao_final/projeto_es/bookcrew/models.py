from django.db import models


class Utilizador(models.Model):
    id_utilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='bookcrew/static/utilizadores_imgs')
    descricao = models.TextField()



class Critica(models.Model):
    id_critica = models.AutoField(primary_key=True)
    id_livro =  models.CharField(max_length=200)
    id_utilizador = models.ForeignKey('Utilizador', on_delete=models.CASCADE, to_field='id_utilizador')
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    num_gostos = models.IntegerField(default=0)
    classif = models.IntegerField()


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_critica = models.ForeignKey('Critica', on_delete=models.CASCADE)
    id_utilizador = models.ForeignKey('Utilizador', on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class Colecao(models.Model):

    id_colecao = models.AutoField(primary_key=True)
    id_utilizador =  models.ForeignKey('Utilizador', on_delete=models.CASCADE)


class Subcolecao(models.Model):

    id_sub_colecao = models.AutoField(primary_key=True)
    id_colecao = models.ForeignKey('Colecao', on_delete=models.CASCADE)
    categoria = models.IntegerField(default=0)
    id_livro = models.CharField(max_length=200)


class Amizade(models.Model):
    id_amizade = models.AutoField(primary_key=True)
    id_utilizador_1 = models.ForeignKey('Utilizador', related_name='amizade_1', on_delete=models.CASCADE)
    id_utilizador_2 = models.ForeignKey('Utilizador', related_name='amizade_2', on_delete=models.CASCADE)


class PedidoAmizade(models.Model):

    id_pedido_amizade = models.AutoField(primary_key=True)
    id_utilizador_env = models.ForeignKey('Utilizador', related_name='utilizador_env', on_delete=models.CASCADE)
    id_utilizador_recebe = models.ForeignKey('Utilizador', related_name='utilizador_rec', on_delete=models.CASCADE)


