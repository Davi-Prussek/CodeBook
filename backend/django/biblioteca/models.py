from django.db import models

# Create your models here.

linguagemOpcoes = [('html', 'HTML'),('css', 'CSS'),('js', 'JavaScript')]

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    linguagem = models.CharField(max_length=20, choices=linguagemOpcoes)
    def __str__(self):
        return f'{self.nome} - {self.linguagem}'

class Codigo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    modoDeUsar = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT ,related_name='codigos')
    def __str__(self):
        return f'{self.nome}'