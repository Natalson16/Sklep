"""Sklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Samochody.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rejestracja/', Samochody.views.registerPage, name="rejestracja"),
    path('logowanie/', Samochody.views.loginPage, name="logowanie"),
    path('wylogowanie/', Samochody.views.logoutUser, name="wylogowanie"),

    path('', Samochody.views.index, name='index'),
    path('kategoria/<id>/', Samochody.views.kategoria, name='kategoria'),
    path('samochod/<id>/', Samochody.views.samochod, name='samochod')]
