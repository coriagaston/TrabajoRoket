
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

from apps.pregunta.models import Perfil_Usuario, Pregunta, PreguntasRespondidas, Respuesta


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
def validar_intento(self,PreguntasRespondidas, respuesta_selecionada):
		if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
			return 

		pregunta_respondida.respuesta_selecionada = respuesta_selecionada
		if respuesta_selecionada.correcta is True:
			pregunta_respondida.correcta = True
			pregunta_respondida.puntaje = respuesta_selecionada.pregunta.max_puntaje
			pregunta_respondida.respuesta = respuesta_selecionada

		pregunta_respondida.save()



@login_required
def InicioJuego(request):
	Perfil_User, created = Perfil_Usuario.objects.get_or_create(perfil_usuario=request.user)
	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = Perfil_User.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		Perfil_User.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect(pregunta_respondida)



	else: 
		pregunta = Perfil_User.obtener_nuevas_preguntas()
		if pregunta is not None:
			Perfil_User.crear_intentos(pregunta)

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
