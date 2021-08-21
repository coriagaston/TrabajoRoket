
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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


def RegistroUsuario(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if forms.is_valid():
			usuername = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
	else:
		form = UserCreationForm()
	context = {'form' : form}
	return render(request, 'usuarios/registrar.html')
