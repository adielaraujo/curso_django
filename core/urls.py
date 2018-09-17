
from django.urls import include, path, re_path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movimentos_rotativos,
    lista_mensalistas,
    lista_movimentos_mensalistas,
    pessoa_novo,
)



urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoas-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^movimentos-rotativos/$', 
        lista_movimentos_rotativos, name='core_lista_movimentos_rotativos'),
    re_path(r'^mensalistas/$', 
        lista_mensalistas, name='core_lista_mensalistas'),
    re_path(r'^movimentos-mensalistas/$', 
        lista_movimentos_mensalistas, name='core_lista_movimentos_mensalistas'),

]