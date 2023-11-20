from django.db import models

import os
import uuid
from django.utils import timezone


def gerar_nome_aleatorio(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]

    # Generate a unique filename using a timestamp and a random string
    unique_filename = f"{timezone.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}.{ext}"

    # Return the unique filename
    return os.path.join('images/', unique_filename)


# Create your models here.
class Usuario(models.Model):
    ADMIN = "1"
    USUARIO = "2"
    
    USER_CHOICES = [
        (ADMIN, "Administrador"),
        (USUARIO, "Usuário"),
    ]
    
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    senha = models.CharField()
    tipo_usuario = models.CharField(
        max_length=2,
        choices=USER_CHOICES,
        default=ADMIN,
    )
    
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.senha}, {self.tipo_usuario}"
    

class Contato(models.Model):
    mensagem = models.TextField()
    assunto = models.TextField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.mensagem}, {self.assunto}, {self.usuario}"
    

class Materia(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=255)
     
    def __str__(self):
        return f"{self.nome}, {self.descricao}"
    
    
class Conteudo(models.Model):
    descricao = models.TextField(blank=True)
    imagem = models.FileField(blank=True, upload_to=gerar_nome_aleatorio)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.descricao}, {self.materia}"
    
    
class Exercicio(models.Model):
    enunciado = models.TextField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    imagem = models.FileField(blank=True, upload_to=gerar_nome_aleatorio)
 
    def __str__(self):
        return f"{self.enunciado}, {self.materia}"


class Alternativa(models.Model):
    CORRETA = "correta"
    INCORRETA = "incorreta"
    
    STATUS_ALTERNATIVAS = [
        (CORRETA, "Correta"),
        (INCORRETA, "Incorreta"),
    ]
    
    descricao = models.TextField()
    status = models.CharField(
        choices=STATUS_ALTERNATIVAS,
        default=INCORRETA,
    )    
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.descricao}, {self.status}, {self.materia}, {self.exercicio}"
    
    
class Pontuacao(models.Model):
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.quantidade}, {self.usuario.nome}, {self.materia.nome}"


class ResumoAtividade(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.descricao}, {self.data}, {self.usuario}"