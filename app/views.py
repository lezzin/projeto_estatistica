import datetime
from django.shortcuts import render, get_list_or_404, redirect
from django.shortcuts import get_list_or_404
from .models import *

# Create your views here.
def index(request):
    dados = { "usuario_nao_logado": request.session.get("usuario") == None }
    
    return render(request, 'index.html', dados)
    
    
def login(request):
    dados = { "usuario_nao_logado": request.session.get("usuario") == None }
     
    if request.method == "GET":
        return render(request, 'login/index.html', dados)
    else:
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        if Usuario.objects.filter(email=email, senha=senha).exists():
            request.session["usuario"] = Usuario.objects.filter(email=email, senha=senha)[0].id
            return redirect("index")
        else:
            return redirect("cadastro")
   
        
def logout(request):
    try:
        del request.session["usuario"]
        return redirect("login")
    except:
        return redirect("index")

        
def cadastro(request):
    dados = { "usuario_nao_logado": request.session.get("usuario") == None }
    
    if request.method == "GET":
        return render(request, 'cadastro/index.html', dados)
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        if Usuario.objects.filter(email=email, senha=senha).exists():
            return redirect("cadastro")
        else:
            usuario_criado = Usuario(nome=nome, email=email, senha=senha)
            usuario_criado.save()
            return redirect("login")
        

def consulta_materias(request):
    if request.session.get("usuario") == None:
        return redirect("login")
    
    dados = {
        "materias": get_list_or_404(Materia),
        "usuario_nao_logado": request.session.get("usuario") == None 
    }
    
    return render(request, 'materia/index.html', dados)


def consulta_conteudo(request):    
    if request.session.get("usuario") == None:
        return redirect("login")
    
    id_materia = request.GET.get("materia")
    
    dados = {
        "conteudos": Conteudo.objects.select_related("materia").filter(materia=id_materia),
        "materia": Materia.objects.filter(id=id_materia).first(),
    }
    
    return render(request, 'conteudo/index.html', dados)


def consulta_exercicios(request):   
    if request.session.get("usuario") == None:
        return redirect("login")
    
    id_materia = request.GET.get("materia")
    exercicios = Exercicio.objects.filter(materia=id_materia).all()
    
    for exercicio in exercicios:    
        exercicio.alternativa = Alternativa.objects.filter(materia=id_materia).filter(exercicio=exercicio.id).order_by("?")
    
    dados = {
        "exercicios": exercicios,
        "idmateria": id_materia,
        "materia": (Materia.objects.filter(id=id_materia).values()[0]["nome"]).lower(),
    }
    
    return render(request, 'exercicios/index.html', dados)


def consulta_pontuacao(request):    
    if request.session.get("usuario") == None:
        return redirect("login")
    
    pontuacoes = Pontuacao.objects.filter(usuario=request.session["usuario"])
    dados = { 
        "pontuacoes": pontuacoes ,
    }
    
    return render(request, 'pontuacao/index.html', dados)


def deletar_pontuacao(request) :    
    if request.session.get("usuario") == None:
        return redirect("login")
    
    pontuacao = request.POST.get("id")
    Pontuacao.objects.filter(id=pontuacao).delete()
    
    return redirect("pontuacao")


def verificar_resultado(request):    
    if request.session.get("usuario") == None:
        return redirect("login")
    
    id_materia = request.POST.get("materia")
    nome_materia = str.lower(Materia.objects.filter(id=id_materia).first().nome)
    exercicios = Exercicio.objects.filter(materia=id_materia)
    id_usuario = request.session.get("usuario")
    
    pontuacao_usuario = 0
    for exercicio in exercicios:
        id_exercicio = exercicio.id
        nome_input = f"resposta-{id_exercicio}"
        resposta = request.POST.get(nome_input)
        alternativas = Alternativa.objects.filter(exercicio=id_exercicio)
        
        for alternativa in alternativas:
            id_alternativa = alternativa.id
            
            if alternativa.status == "correta" and  int(id_alternativa) == int(resposta):
                pontuacao_usuario += 5
                
    if Pontuacao.objects.filter(usuario=id_usuario, materia=id_materia).exists():
        Pontuacao.objects.filter(usuario=id_usuario, materia=id_materia).delete()
        
    pontuacao = Pontuacao(quantidade=pontuacao_usuario, usuario=Usuario(id=id_usuario), materia=Materia(id=id_materia))
    pontuacao.save()
    
    resumo_atividade = ResumoAtividade(descricao=f"Realizou exercício na matéria {nome_materia}", data= datetime.datetime.now(), usuario=Usuario(id=id_usuario))
    resumo_atividade.save()
    
    dados = { 
        "pontuacao": pontuacao_usuario,
    }
    
    return render(request, "resultado/index.html", dados)


def consulta_calculadora(request):
    if request.session.get("usuario") == None:
        return redirect("login")
    
    dados = {
        "materias": get_list_or_404(Materia),
    }
      
    return render(request, "calculadora/index.html", dados)


def consulta_ranking(request):
    if request.session.get("usuario") == None:
        return redirect("login")
    
    dados = {
        "materias": Materia.objects.all(),
        "pontuacoes": Pontuacao.objects.all().order_by("-quantidade"),
    }
    
    for materia in dados['materias']:
        materia.pontuacoes = Pontuacao.objects.filter(materia=materia.id)
        
    return render(request, "ranking/index.html", dados)


def consulta_atividades(request):
    if request.session.get("usuario") == None:
        return redirect("login")
    
    dados = {
        "atividades": ResumoAtividade.objects.filter(usuario=request.session.get("usuario"))
    }
     
    return render(request, "atividades/index.html", dados)


def deletar_atividade(request) :    
    if request.session.get("usuario") == None:
        return redirect("login")
    
    atividade = request.POST.get("id")
    ResumoAtividade.objects.filter(id=atividade).delete()
    
    return redirect("atividades")
