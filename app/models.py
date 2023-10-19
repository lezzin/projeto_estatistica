from django.db import models

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
    mensagem = models.CharField(max_length=45)
    assunto = models.CharField(max_length=45)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.mensagem}, {self.assunto}, {self.usuario}"
    

class Materia(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=255)
     
    def __str__(self):
        return f"{self.nome}, {self.descricao}"
    
    
class Conteudo(models.Model):
    descricao = models.CharField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.descricao}, {self.materia}"
    
    
class Exercicio(models.Model):
    enunciado = models.CharField(max_length=255)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
 
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
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.quantidade}, {self.usuario}, {self.materia}, {self.exercicio}"


class ResumoAtividade(models.Model):
    descricao = models.IntegerField()
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.descricao}, {self.data}, {self.usuario}"