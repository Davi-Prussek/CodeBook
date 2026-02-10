from django.db import models

# Create your models here.

class Codigo(models.Model):
    linguagemOpcoes = [('html', 'HTML'),('css', 'CSS'),('js', 'JS')]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    modoDeUsar = models.TextField()
    linguagem = models.CharField(max_length=30, choices=linguagemOpcoes)
    def __str__(self):
        return f'{self.nome} - {self.linguagem}'