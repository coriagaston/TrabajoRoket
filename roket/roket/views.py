
from django.shortcuts import render

def Base(request):

	return render(request,'base.html')

def Juego(request):

	return render(request,'juego.html')