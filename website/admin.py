from django.contrib import admin
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'sobrenome',
        'endereco',
        'email',
        'receber_noticia',
        'mensagem_email'
    )


admin.site.register(Contato, ContatoAdmin)