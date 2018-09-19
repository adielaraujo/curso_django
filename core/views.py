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
    MensalistaForm,
    MovMensalistaForm,
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

def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm (request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    data =  {'obj': pessoa}
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', data)




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


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm (request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    data =  {'obj': veiculo}
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', data)






def lista_movimentos_rotativos(request):
    movRotativo = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'rotativos': movRotativo,'form': form}
    return render(request, 
        'core/lista_movimentos_rotativos.html', data)

def movimento_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentos_rotativos')


def movimento_rotativo_update(request, id):
    data = {}
    mov = MovRotativo.objects.get(id=id)
    form = MovRotativoForm (request.POST or None, instance=mov)
    data['movimento_rotativo'] = mov
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movimentos_rotativos')
    else:
        return render(request, 'core/update_movimento_rotativo.html', data)



def movimento_rotativo_delete(request, id):
    mov = MovRotativo.objects.get(id=id)
    data =  {'obj': mov}
    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_movimentos_rotativos')
    else:
        return render(request, 'core/delete_confirm.html', data)



def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas,'form': form}
    return render(request, 
        'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')



def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    data =  {'obj': mensalista}
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)



def lista_movimentos_mensalistas(request):
    movimentosMensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movimentosMensalistas': movimentosMensalistas,'form': form}
    return render(request, 
        'core/lista_movimentos_mensalistas.html', data)



def mov_mensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentos_mensalistas')

def mov_mensalista_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movimentos_mensalistas')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)



def mov_mensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    data =  {'obj': mov_mensalista}
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movimentos_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)


