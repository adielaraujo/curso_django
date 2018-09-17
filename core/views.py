from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models  import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .forms import PessoaForm

def home(request):
    context = {'mensagem':'Ola mundo'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data =  {'pessoas': pessoas,'form':form}
    return render(request, 'core/lista_pessoas.html',data)

def pessoa_novo(request):
    form = PessoaForm (request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = MovRotativo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})

def lista_movimentos_rotativos(request):
    movRotativo = MovRotativo.objects.all()
    return render(request, 
        'core/lista_movimentos_rotativos.html', 
        {'rotativos': movRotativo})

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 
        'core/lista_mensalistas.html', 
        {'mensalistas': mensalistas})

def lista_movimentos_mensalistas(request):
    movimentosMensalistas = MovMensalista.objects.all()
    return render(request, 
        'core/lista_movimentos_mensalistas.html', 
        {'movimentosMensalistas': movimentosMensalistas})

