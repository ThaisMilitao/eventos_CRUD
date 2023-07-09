from django.shortcuts import redirect, render
from .models import Evento
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Funcao para retornar a lista com todos os eventos existentes
def home(request):
    # buscar por todos os objetos
    evento = Evento.objects.all().order_by('data')
    #criar dicionario para armezar os dados buscado
    context ={
        'eventos' : evento }
    # retornar o html e os valores do dicionario(context)
    return render(request, 'lista.html', context)

# Funcao para criar eventos
@login_required(login_url='login')
def addEvento(request):
    # verifica se a requisição foi do tipo get ou post
    # se post envia os dados do forms, se nao retorna a pagina html 
    if request.method == 'POST':
        # atribui a variavel o valor que foi "enviado" no forms atraves do metodo post
        # depois salva e redireciona para a home
        nome = request.POST.get('nome')
        local = request.POST.get('local')
        data= request.POST.get('data')
        horario= request.POST.get('horario')
        descricao= request.POST.get('descricao')

        evento = Evento(
            nome=nome,
            local = local,
            data = data,
            horario = horario,
            descricao = descricao,
            user = User.objects.get(username = request.user)
        )
        evento.save()           
        return redirect('home')
    return render(request, 'formEvento.html')

# Funcao para  ver detalhes do evento
@login_required(login_url='login')
def detalharEvento(request, id):
    # busca pelo objeto apartir do id, em seguida cria um dicionario para armezenar o dado
    # e depois tornar o html e o dicionario
    evento = Evento.objects.get(id=id)
    context ={
        'eventos' : evento }
    return render(request, 'detalhes.html', context)

# Funcao para editar evento
@login_required(login_url='login')
def editarEvento(request, id):
    # busca pelo objeto apartir do id, em seguida cria um dicionario para armezenar o dado
    evento = Evento.objects.get(id=id)
    
    context ={
        'eventos':evento
    } 
    
     # verifica se a requisição foi do tipo get ou post
     # se post envia os dados do forms, se nao retorna a pagina html 
    if request.method == 'POST':
        nome = request.POST.get('nome')
        local = request.POST.get('local')
        data= request.POST.get('data')
        horario= request.POST.get('horario')
        descricao= request.POST.get('descricao')
        
        evento.nome=nome
        evento.local = local
        evento.data = data
        evento.horario = horario
        evento.descricao = descricao

        evento.save()
        messages.success(request, 'Editado com sucesso!')
        return redirect('meusEventos')
   
    
    return render(request, 'editEvento.html', context)

# Funcao para deletar evento
@login_required(login_url='login')
def deletarEvento(request, id):
    # busca pelo objeto apartir do id, em seguida deleta e depois redireciona para home
    evento = Evento.objects.get(id=id)
    evento.delete()
    messages.success(request, 'Deletado com sucesso!')
    return redirect('meusEventos')

@login_required(login_url='login')
def meusEventos(request): 
    eventos = Evento.objects.filter(user = User.objects.get(username = request.user))
    context = {
        "mEventos": eventos,
    }
    return render(request, 'meusEventos.html', context)
