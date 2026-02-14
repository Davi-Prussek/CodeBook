from django.db import models
from django.utils.html import format_html

# Create your models here.

linguagemOpcoes = [('html', 'HTML'),('css', 'CSS'),('js', 'JavaScript')]

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    linguagem = models.CharField(max_length=20, choices=linguagemOpcoes)

    class Meta:
        unique_together = ('nome', 'linguagem')
         
    def __str__(self):
        return format_html(
            'Categoria: {}<br>Linguagem: {}<br>ID: {}',
            self.nome,
            self.linguagem,
            self.id,
        )

class Codigo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    modoDeUsar = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='codigos')
    def __str__(self):
        return format_html(
            'Código: {}<br>Categoria: {}<br>Linguagem: {}<br>ID: {}',
            self.nome,
            self.categoria.nome,
            self.categoria.linguagem,
            self.id,
        )