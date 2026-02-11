from django.core.management.base import BaseCommand
from biblioteca.models import *

codigos = [

]

class Command(BaseCommand):

    help = 'Deu errado kkkk'
    def handle(self, *args, **kwargs): 


        for nome, descricao, uso, nome_categoria, linguagem in codigos:

            categoria = Categoria.objects.get(
                nome=nome_categoria,
                linguagem=linguagem
            )

            Codigo.objects.get_or_create(
                nome=nome,
                categoria=categoria,
                defaults={
                    'descricao': descricao,
                    'modoDeUsar': uso
                }
            )

        self.stdout.write(self.style.SUCCESS('Dados registrados!'))