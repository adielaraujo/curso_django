
from django.urls import include, path, re_path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movimentos_rotativos,
    lista_mensalistas,
    lista_movimentos_mensalistas,
    pessoa_novo,
    veiculo_novo,
    movimento_rotativo_novo,
    mensalista_novo,
    mov_mensalista_novo,
    pessoa_update,
    veiculo_update,
    movimento_rotativo_update,
    mensalista_update,
    mov_mensalista_update, 
    pessoa_delete,
    veiculo_delete,
    movimento_rotativo_delete,
    mensalista_delete,
    mov_mensalista_delete, 
    
)



urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoas-update/(?P<id>\d+)/$', pessoa_update, 
        name='core_pessoa_update'),
    re_path(r'^pessoas-delete/(?P<id>\d+)/$', pessoa_delete, 
        name='core_pessoa_delete'),


    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, 
        name='core_veiculo_update'),
    re_path(r'^veiculo-delete/(?P<id>\d+)/$', veiculo_delete, 
        name='core_veiculo_delete'),



    re_path(r'^movimentos-rotativos/$', 
        lista_movimentos_rotativos, name='core_lista_movimentos_rotativos'),
    re_path(r'^movimento-rotativo-novo/$', 
        movimento_rotativo_novo, name='core_movimento_rotativo_novo'),
    re_path(r'^movimento-rotativo-update/(?P<id>\d+)/$', movimento_rotativo_update, 
        name='core_movimento_rotativo_update'),
    re_path(r'^movimento-rotativo-delete/(?P<id>\d+)/$', movimento_rotativo_delete, 
        name='core_movimento_rotativo_delete'),


    re_path(r'^mensalistas/$', 
        lista_mensalistas, name='core_lista_mensalistas'),
    re_path(r'^mensalista-novo/$', 
        mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, 
        name='core_mensalista_update'),
    re_path(r'^mensalista-delete/(?P<id>\d+)/$', mensalista_delete, 
        name='core_mensalista_delete'),



    re_path(r'^movimentos-mensalistas/$', 
        lista_movimentos_mensalistas, name='core_lista_movimentos_mensalistas'),
    re_path(r'^movimento-mensalista/$', 
        mov_mensalista_novo, name='core_movimento_mensalista_novo'),
    re_path(r'^mov-mensalista-update/(?P<id>\d+)/$', mov_mensalista_update, 
        name='core_mov_mensalista_update'),
    re_path(r'^mov-mensalista-delete/(?P<id>\d+)/$', mov_mensalista_delete, 
        name='core_mov_mensalista_delete'),



]