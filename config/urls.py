"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('cadastro/', cadastro, name="cadastro"),
    
    path('materias/', consulta_materias, name="materias"),
    
    path('conteudo/', consulta_conteudo, name="conteudo"),
    path('exercicios/', consulta_exercicios, name="exercicios"),
    path('resultado/', verificar_resultado, name="resultado"),
    
    path('pontuacao/', consulta_pontuacao, name="pontuacao"),
    path('pontuacao/deletar', deletar_pontuacao, name="deletar_pontuacao"),
    
    path('calculadora/', consulta_calculadora, name="calculadora"),
    path('ranking/', consulta_ranking, name="ranking"),
    
    path('atividades/', consulta_atividades, name="atividades"),
    path('atividade/deletar', deletar_atividade, name="deletar_atividade"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
