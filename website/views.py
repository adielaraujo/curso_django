from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models import Contato
from django.contrib import messages

# Create your views here.

def website_home(request):
    menu_home = 'active'
    data = {'menu_home':menu_home}
    return render(request, 'website/index.html', data)


def website_servicos(request):
    menu_servicos = 'active'
    data = {'menu_servicos':menu_servicos}
    return render(request, 'website/servicos.html', data)


def website_sobre(request):
    menu_sobre = 'active'
    data = {'menu_sobre':menu_sobre}
    return render(request, 'website/sobre.html', data)


def website_planos(request):
    menu_planos = 'active'
    data = {'menu_planos':menu_planos}
    return render(request, 'website/planos.html', data)


def website_contato(request):
    menu_contato = 'active'
    if request.method=='POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('inputEmail')
            contato['nome'] = request.POST.get('inputNome')
            contato['sobrenome'] = request.POST.get('inputSobrenome')
            contato['endereco'] = request.POST.get('inputEndereco')
            contato['receber_noticia'] = True if request.POST.get('checkReceberNoticia') == 'on' else False
            contato['mensagem_email'] = request.POST.get('inputMensagem')

            Contato.objects.create(**contato)
        except Exception as e:
            messages.error(request, str(e))
        else:
            messages.success(request,'Contato realizado com sucesso')
    
    data = {'menu_contato':menu_contato,}
    return render(request, 'website/contato.html', data)

