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
        "conteudos": Conteudo.objects.select_for_update("materia").filter(materia=id_materia)
    }
    
    return render(request, 'conteudo/index.html', dados)