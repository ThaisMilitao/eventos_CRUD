from django.shortcuts import redirect, render
from .models import Evento
from django.contrib import messages

# Create your views here.

# Funcao para retornar a lista com todos os eventos existentes
def home(request):
    # buscar por todos os objetos
    evento = Evento.objects.all()

    #criar dicionario para armezar os dados buscado
    context ={
        'eventos' : evento }
    # retornar o html e os valores do dicionario(context)
    return render(request, 'lista.html', context)

# Funcao para criar eventos
def addEvento(request):
    # verifica se a requisição foi do tipo get ou post
    # se post envia os dados do forms, se nao retorna a pagina html 
    #  
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
            descricao = descricao
        )
        evento.save()
        return redirect('home')

    return render(request, 'formEvento.html')

# Funcao para  ver detalhes do evento
def detalharEvento(request, id):
    # busca pelo objeto apartir do id, em seguida cria um dicionario para armezenar o dado
    # e depois tornar o html e o dicionario
    evento = Evento.objects.get(id=id)
    context ={
        'eventos' : evento }
    return render(request, 'detalhes.html', context)

# Funcao para editar evento
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
        return redirect('home')

    
    return render(request, 'editEvento.html', context)

# Funcao para deletar evento
def deletarEvento(request, id):
    # busca pelo objeto apartir do id, em seguida deleta e depois redireciona para home
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('home')