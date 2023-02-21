from django.contrib import admin

# Register your models here.
from . models import Comentario, Colecao, Utilizador, Critica, Subcolecao, Amizade, PedidoAmizade

admin.site.register(Comentario)
admin.site.register(Colecao)

admin.site.register(Utilizador)
admin.site.register(Critica)

admin.site.register(Subcolecao)

admin.site.register(Amizade)
admin.site.register(PedidoAmizade)