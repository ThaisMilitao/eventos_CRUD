from django.shortcuts import render
from django.shortcuts import render, redirect
from xml.dom import ValidationErr
import re
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = auth.authenticate(username=username, password=password)      
        if user is not None:
            auth.login(request, user=user)         
            return redirect('home') 
        messages.success(request, 'Username e/ou senha incorreta')
    return render(request, 'formLogin.html')

@login_required(login_url='login')
def logOut(request):
    auth.logout(request)
    return redirect('home')

def signUp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = User(username=username,email=email, first_name = name)
        context={"usuario":user}
        if not User.objects.filter(username=username).exists():
            if validarSenha(password):
                messages.error(request, 'Requisitos:\n*Pelo menos 2 letras Maiuscula\n*Pelo menos 2 numeros')
                return render(request, "formSignUp.html", context)
            user = User.objects.create_user(email=email, first_name = name, username=username, password=password)
            user.save()
            return redirect('login')
        messages.success(request, 'username já existe')
        return render(request, "formSignUp.html", context)

    return render(request, "formSignUp.html")

def validarSenha(password):
    min_numero = 2
    min_letraMaiuscula = 2
    # min_letraMinuscula = 2
    # min_carac_especial = 1
    # tamanho_minimo = 8
    
    # if len(password or ()) < tamanho_minimo:
    #     return ValidationErr("Tamanho minimo de" + str(tamanho_minimo) + "caracteres")
    if len(re.findall(r"[A-Z]", password)) < min_letraMaiuscula:
        return ValidationErr("Possuir pelo menos" + str(min_letraMaiuscula) + "letra Maiuscula")
    # if len(re.findall(r"[a-z]", password)) < min_letraMinuscula:
    #     return ValidationErr("Possuir pelo menos" + str(min_letraMinuscula) + "letra minuscula")
    if len(re.findall(r"[0-9]", password)) < min_numero:
        return ValidationErr("Possuir pelo menos" + str(min_numero) + "numeros")
    # if len(re.findall(r"[!#$%&'*+-.^_`|~:]", password)) < min_carac_especial:
    #     return ValidationErr("Possuir pelo menos" + str(min_carac_especial) + "caractere especial")