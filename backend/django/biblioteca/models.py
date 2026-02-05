from django.db import models

# Create your models here.

class Codigo(models.Model):
    LANGUAGE_CODE=[
    ('html','HTML'),
    ('css','CSS'),
    ('js','JS','javascript','JavaScript','JAVASCRIPT')],

    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)
    modoDeUsar = models.TextField(max_length=200)
    linguagem = models.CharField(max_length=30, choices=LANGUAGE_CODE)
    def __str__(self):
        return f'{self.nome} - {self.linguagem}'