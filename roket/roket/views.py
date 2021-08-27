
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

from apps.pregunta.models import Perfil_Usuario, Pregunta, PreguntasRespondidas, Respuesta, Categoria

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from django.contrib import messages

def Base(request):

	return render(request,'base.html')

def Juego(request):

	return render(request,'juego.html')

def Login(request):

	return render(request,'login.html')

def Home(request):

	return render(request,'home.html')

#def Ranking(request):

	#return render(request,'ranking.html')

def Preguntas(request):

	return render(request,'Preguntas/pregunta.html')







@login_required
def InicioJuego(request, categoria):
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
		if pregunta_respondida.correcta == False:
			pregunta = None
			
		else:	
			pregunta = Perfil_User.obtener_nuevas_preguntas(categoria)
		if pregunta is not None:
			Perfil_User.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta ,
		}
	else: 
		pregunta = Perfil_User.obtener_nuevas_preguntas(categoria)
		if pregunta is not None:
			Perfil_User.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta ,
		}


	return render(request,'iniciojuego.html',context)

# @login_required
# def InicioJuego(request, categoria):
# 	Perfil_User, created = Perfil_Usuario.objects.get_or_create(perfil_usuario=request.user)
# 	if request.method == 'POST':
# 		pregunta_pk = request.POST.get('pregunta_pk')
# 		pregunta_respondida = Perfil_User.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
# 		respuesta_pk = request.POST.get('respuesta_pk')

# 		try:
# 			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
# 		except ObjectDoesNotExist:
# 			raise Http404
		
# 		Perfil_User.validar_intento(pregunta_respondida, opcion_selecionada)
# 		if pregunta_respondida.correcta == False:
# 			pregunta = None
# 			context ['mensaje']="Pregunta Incorrecta, sin Preguntas"
# 		else:	
# 			pregunta = Perfil_User.obtener_nuevas_preguntas(categoria)
# 		if pregunta is not None:
# 			Perfil_User.crear_intentos(pregunta)
# 		context ['pregunta']=pregunta
# 	else: 
# 		context = {}
# 		pregunta = Perfil_User.obtener_nuevas_preguntas(categoria)
# 		if pregunta is not None:
# 			Perfil_User.crear_intentos(pregunta)
# 		else:
# 			context ['mensaje']="No hay mas preguntas en esta categoria" 
# 			context ['pregunta']=pregunta


# 	return render(request,'iniciojuego.html',context)


class CategoriaListView(ListView):

	model = Categoria
	template_name='Preguntas/categorias.html'

	def get_context_data(self, **kwargs):
		context = super(CategoriaListView, self).get_context_data(**kwargs)
		categoria = Categoria.objects.all()
		context['categorias'] = categoria
		return context


class RankingListView(ListView):

	model = Perfil_Usuario
	template_name='ranking.html'

	def get_context_data(self, **kwargs):
		context = super(RankingListView, self).get_context_data(**kwargs)
		ranking = Perfil_Usuario.objects.order_by('-puntaje_total')[:10]
		context['ranking'] = ranking
		return context



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
