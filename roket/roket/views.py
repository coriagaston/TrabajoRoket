
from django.shortcuts import render

def Home(request):

	return render(request,'home.html')

def Juego(request):

	return render(request,'juego.html')