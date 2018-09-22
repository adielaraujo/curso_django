from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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


@login_required
def home(request):
    menu_home_ativo = 'active'
    data = {'menu_home_ativo':menu_home_ativo}
    return render(request, 'core/index.html', data)


@login_required
def lista_pessoas(request):
    menu_pessoa_ativo = 'active'
    menu_cadastro_ativo = 'active'
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data =  {'pessoas': pessoas,
        'form':form, 
        'menu_pessoa_ativo':menu_pessoa_ativo, 
        'menu_cadastro_ativo':menu_cadastro_ativo}
    return render(request, 'core/lista_pessoas.html',data)


@login_required
def pessoa_novo(request):
    form = PessoaForm (request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
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


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    data =  {'obj': pessoa}
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', data)


@login_required
def lista_veiculos(request):
    menu_veiculo_ativo = 'active'
    menu_cadastro_ativo = 'active'
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos,
        'form': form,
        'menu_veiculo_ativo':menu_veiculo_ativo, 
        'menu_cadastro_ativo':menu_cadastro_ativo}

    return render(request, 'core/lista_veiculos.html', data)


@login_required
def veiculo_novo(request):
    form = VeiculoForm (request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
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


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    data =  {'obj': veiculo}
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', data)


@login_required
def lista_movimentos_rotativos(request):
    menu_movimento_rotativo_ativo = 'active'
    menu_cadastro_ativo = 'active'
    movRotativo = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'rotativos': movRotativo,
        'form': form,
        'menu_movimento_rotativo_ativo':menu_movimento_rotativo_ativo, 
        'menu_cadastro_ativo':menu_cadastro_ativo}

    return render(request, 
        'core/lista_movimentos_rotativos.html', data)


@login_required
def movimento_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentos_rotativos')


@login_required
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


@login_required
def movimento_rotativo_delete(request, id):
    mov = MovRotativo.objects.get(id=id)
    data =  {'obj': mov}
    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_movimentos_rotativos')
    else:
        return render(request, 'core/delete_confirm.html', data)


@login_required
def lista_mensalistas(request):
    menu_mensalista_ativo = 'active'
    menu_cadastro_ativo = 'active'
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas,
        'form': form,
        'menu_mensalista_ativo':menu_mensalista_ativo, 
        'menu_cadastro_ativo':menu_cadastro_ativo}

    return render(request, 
        'core/lista_mensalistas.html', data)

@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required
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

@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    data =  {'obj': mensalista}
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)


@login_required
def lista_movimentos_mensalistas(request):
    menu_movimento_mensalista_ativo = 'active'
    menu_cadastro_ativo = 'active'
    movimentosMensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movimentosMensalistas': movimentosMensalistas,
        'form': form,
        'menu_movimento_mensalista_ativo':menu_movimento_mensalista_ativo, 
        'menu_cadastro_ativo':menu_cadastro_ativo}

    return render(request, 
        'core/lista_movimentos_mensalistas.html', data)


@login_required
def mov_mensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentos_mensalistas')


@login_required
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



@login_required
def mov_mensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    data =  {'obj': mov_mensalista}
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movimentos_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)


