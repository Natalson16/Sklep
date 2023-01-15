from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Samochody, Kategoria
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Twoje konto zostało utworzone!')
                return redirect(loginPage)

        dane = {'form': form}
        return render(request, 'rejestracja.html', dane)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(index)
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło jest nieprawidłowe')

        dane = {}
        return render(request, 'logowanie.html', dane)

def logoutUser(request):
    logout(request)
    return redirect(loginPage)


@login_required(login_url='logowanie')
def index(request):
    url = 'http://127.0.0.1:8000/'
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie,
            'url' : url}
    return render(request, 'szablon.html', dane)


@login_required(login_url='logowanie')
def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    samochod_kategorii_user = Samochody.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'samochod_kategorii_user': samochod_kategorii_user,
            'kategorie': kategorie}
    return render(request, 'kategoria.html', dane)


@login_required(login_url='logowanie')
def samochod(request, id):
    samochod_user = Samochody.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'samochod_user': samochod_user, 'kategorie': kategorie}
    return render(request, 'samochod.html', dane)
