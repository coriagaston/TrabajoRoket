
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Base(request):

	return render(request,'base.html')

def Juego(request):

	return render(request,'juego.html')

def Login(request):

	return render(request,'login.html')

def Home(request):

	return render(request,'home.html')

def Ranking(request):

	return render(request,'ranking.html')

@login_required
def InicioJuego(request):

	return render(request,'iniciojuego.html')