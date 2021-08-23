
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

from apps.pregunta.models import Perfil_Usuario, Pregunta


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
	Perfil_User, created = Perfil_Usuario.objects.get_or_create(perfil_usuario=request.user)
	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = Perfil_User.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('resputa_pk')
	else: 
		respondidas = PreguntasRespondidas.objects.filter(perfil_usuario=Perfil_User).values_list('pregunta__pk',flat=True)
		pregunta = Pregunta.objects.exclude(pk__in=respondidas)

		context = {
			'pregunta':pregunta
		}


	return render(request,'iniciojuego.html',context)


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
			#messages.success(request, "Te has registrado correctamente")
			return redirect(to='homeiniciadosesion')
		data["form"] = formulario

	return render(request, 'usuarios/registrar.html', data)


@login_required
def HomeInicioLogin(request):

	return render(request,'homeiniciadosesion.html')
