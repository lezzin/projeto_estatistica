from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import *

# Create your views here.
def consulta_materias(request):
    dados = {
        "materias": get_list_or_404(Materia)
    }
    
    return render(request, 'materia/index.html', dados)


def consulta_conteudo(request):
    id_materia = request.GET.get("materia")
    
    dados = {
        "conteudos": Conteudo.objects.select_related("materia").filter(materia=id_materia),
        "id_materia": id_materia
    }
    
    print(dados["conteudos"])
    
    return render(request, 'conteudo/index.html', dados)


def consulta_exercicios(request):
    id_materia = request.GET.get("materia")
    exercicios = Exercicio.objects.select_related("materia").filter(materia=id_materia)
    
    for exercicio in exercicios:
        exercicio.alternativas = Alternativa.objects.filter(id=exercicio.alternativa)
    
    dados = {
        "exercicios": exercicios
    }
    
    print(dados["exercicios"])
    
    return render(request, 'exercicios/index.html', dados)