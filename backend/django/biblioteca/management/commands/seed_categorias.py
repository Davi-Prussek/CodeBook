from django.core.management.base import BaseCommand
from biblioteca.models import *

categorias = [
    ('Raiz e Metadados', 'Define o documento e metadados', 'html'),
    ('Estruturação de Conteúdo (Semânticas)', 'Organiza a página', 'html'),
    ('Texto e Títulos','Define a hierarquia e formatação', 'html'),
    ('Listas',' Organiza dados em lista', 'html'),
    ('Formulários','Cria interatividade para entrada de dados', 'html'),
    ('Imagens e Multimídia','Insere recursos visuais/auditivos', 'html'),
    ('Tabelas','Estrutura dados tabulares', 'html'),
    ('Links e Incorporação','Conecta ou embute', 'html'),
    ('Elementos Interativos','Aumenta a funcionalidade', 'html'),
        
    ('Texto e Tipografia','Propriedades responsáveis pela aparência e formatação de textos, como fonte, tamanho, alinhamento e espaçamento.','css'),
    ('Cores e Background','Define cores, imagens e efeitos de fundo dos elementos.','css'),
    ('Box Model','Controla tamanho, espaçamento interno (padding), externo (margin) e bordas dos elementos.','css'),
    ('Layout e Posicionamento','Define como os elementos são exibidos e posicionados na página (display, position, etc).','css'),
    ('Flexbox','Sistema de layout unidimensional para organizar elementos em linha ou coluna.','css'),
    ('Grid','Sistema de layout bidimensional para organizar elementos em linhas e colunas.','css'),
    ('Efeitos Visuais','Adiciona sombras, transparência, filtros e outros efeitos estéticos.','css'),
    ('Transições','Cria animações suaves entre mudanças de propriedades.','css'),
    ('Animações','Permite criar animações mais complexas usando keyframes.','css'),
    ('Transformações','Altera escala, rotação, inclinação e posição de elementos.','css'),
    ('Interatividade','Controla comportamento do cursor, seleção de texto e eventos do usuário.','css'),
    ('Responsividade','Adapta o layout para diferentes tamanhos de tela usando media queries e funções responsivas.','css'),
    ('Variáveis CSS','Permite criar valores reutilizáveis dentro do CSS para manter organização e consistência.','css'),
    ('Pseudo-classes', 'Permite aplicar estilos a elementos com base em seu estado ou posição.', 'css'),
    ('Pseudo-elementos','selecionam partes do elemento ou criam conteúdo extra.', 'css'),
    ('outros', "Propriedades diversas que controlam aspectos do comportamento ou apresentação de elementos.",'css'),

    ('Sintaxe e Fundamentos', 'Variáveis, tipos de dados, operadores e estrutura básica da linguagem.', 'js'),
    ('Controle de Fluxo', 'Condicionais (if, switch) e estruturas de repetição (for, while).', 'js'),
    ('Funções', 'Declaração de funções, arrow functions, parâmetros e retorno.', 'js'),
    ('Arrays', 'Manipulação de listas de dados e métodos como map, filter e reduce.', 'js'),
    ('Objetos', 'Criação e manipulação de objetos, propriedades e métodos.', 'js'),
    ('DOM', 'Manipulação de elementos HTML através do Document Object Model.', 'js'),
    ('Eventos', 'Interação com o usuário através de eventos como click, input e submit.', 'js'),
    ('Assincronismo', 'Promises, async/await e controle de código assíncrono.', 'js'),
    ('Requisições HTTP', 'Consumo de APIs utilizando fetch e outras técnicas de requisição.', 'js'),
    ('Classes e OOP', 'Programação orientada a objetos com classes, herança e encapsulamento.', 'js'),
    ('Módulos', 'Importação e exportação de código para organização do projeto.', 'js'),
    ]

class Command(BaseCommand):

    help = 'Cria categorias iniciais do CodeBook'

    def handle(self, *args, **kwargs):

        for nome, descricao, linguagem in categorias:
            Categoria.objects.get_or_create(
                nome=nome,
                linguagem=linguagem,
                defaults={"descricao": descricao})

        self.stdout.write(self.style.SUCCESS('Dados registrados!'))