from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models  import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
)

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
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos,'form': form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm (request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def lista_movimentos_rotativos(request):
    movRotativo = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'rotativos': movRotativo,'form': form}
    return render(request, 
        'core/lista_movimentos_rotativos.html', 
        data)

def movimento_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentos_rotativos')

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

