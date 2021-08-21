
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


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
	data = {
		'form' : CustomUserCreationForm()
	}
	if request.method == 'POST':
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			login(request, user)
			messages.success(request, "Te has registrado correctamente")
			return redirect(to='homeiniciadosesion')
		data["form"] = formulario

	return render(request, 'usuarios/registrar.html', data)


@login_required
def HomeInicioLogin(request):

	return render(request,'homeiniciadosesion.html')
