from django.shortcuts import render #MANTENHO

# catalogo/views.py
from django.http import HttpResponse
 
def home(request): #requisião e resposta
    return HttpResponse("Bem-vindo!")
 
def sobre(request):
    return HttpResponse("Sobre nós")