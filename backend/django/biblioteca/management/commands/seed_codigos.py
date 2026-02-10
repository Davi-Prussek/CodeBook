from django.core.management.base import BaseCommand
from biblioteca.models import *

HTML = [

]

CSS = [

]

JS = [

]

class Command(BaseCommand):

    help = 'Deu errado kkkk'
    def handle(self, *args, **kwargs): 
        objetos = []

        for nome, desc, uso in HTML:
            objetos.append(Codigo(
            nome=nome,
            descricao=desc,
            modoDeUsar=uso,
            linguagem='html'
        ))

        for nome,desc, uso in CSS:
            objetos.append(Codigo(
            nome=nome,
            descricao=desc,
            modoDeUsar=uso,
            linguagem='css'
        ))

        for nome,desc, uso in JS:
            objetos.append(Codigo(
            nome=nome,
            descricao=desc,
            modoDeUsar=uso,
            linguagem='JS'
        ))

        Codigo.objects.bulk_create(objetos, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Dados registrados!'))