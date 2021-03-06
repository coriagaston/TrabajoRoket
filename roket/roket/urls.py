"""roket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as  auth
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    #Cree el Home
    path('', views.Home, name='home'),
    
    #Inicio del juego

    path('iniciojuego/<int:categoria>', views.InicioJuego, name='iniciojuego'),
    
    path('ranking/', views.RankingListView.as_view(), name='ranking'),
    
    path('juego/', views.Juego, name='juego'),
    #login 
    path('login/',auth.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    #logout
    path('logout/', auth.LogoutView.as_view(),name='logout'),

    path('registrar/', views.RegistroUsuario, name='registrar'),

    path('homeiniciadosesion/', views.HomeInicioLogin, name='homeiniciadosesion'),

    path('pregunta/', views.Preguntas, name='preguntas/pregunta.html'),

    path('categoria/', views.CategoriaListView.as_view(), name='categorias'),
    

    

]
