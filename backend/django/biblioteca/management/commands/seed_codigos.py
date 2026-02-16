from django.core.management.base import BaseCommand
from biblioteca.models import *

codigos = [

("object-entries","Retorna array com pares [chave,valor].","const obj={a:1}; Object.entries(obj); // [[\"a\",1]]","Objetos","js"),
("object-assign","Copia propriedades para objeto destino.","const a={x:1}; const b={y:2}; Object.assign(a,b); // {x:1,y:2}","Objetos","js"),
("object-freeze","Impede modificações no objeto.","const obj={a:1}; Object.freeze(obj); obj.a=2; obj.a; // 1","Objetos","js"),
("object-seal","Permite alterar valores mas não adicionar/remover propriedades.","const obj={a:1}; Object.seal(obj); obj.a=2; obj.a; // 2","Objetos","js"),
("object-hasOwn","Verifica se objeto possui propriedade própria.","const obj={a:1}; Object.hasOwn(obj,\"a\"); // true","Objetos","js"),
("hasOwnProperty","Verifica se propriedade pertence ao objeto.","const obj={a:1}; obj.hasOwnProperty(\"a\"); // true","Objetos","js"),
("object-create","Cria novo objeto com protótipo definido.","const proto={saudar(){return \"oi\"}}; const obj=Object.create(proto); obj.saudar(); // \"oi\"","Objetos","js"),
("object-getPrototypeOf","Retorna o protótipo do objeto.","const obj={}; Object.getPrototypeOf(obj); // Object.prototype","Objetos","js"),
("object-setPrototypeOf","Define novo protótipo para objeto.","const obj={}; const proto={a:1}; Object.setPrototypeOf(obj,proto); obj.a; // 1","Objetos","js"),
("object-defineProperty","Define ou modifica propriedade.","const obj={}; Object.defineProperty(obj,\"a\",{value:10}); obj.a; // 10","Objetos","js"),
("object-defineProperties","Define múltiplas propriedades.","const obj={}; Object.defineProperties(obj,{a:{value:1},b:{value:2}}); obj.b; // 2","Objetos","js"),
("object-getOwnPropertyNames","Retorna nomes de propriedades próprias.","const obj={a:1}; Object.getOwnPropertyNames(obj); // [\"a\"]","Objetos","js"),
("object-getOwnPropertySymbols","Retorna propriedades Symbol do objeto.","const s=Symbol(); const obj={[s]:1}; Object.getOwnPropertySymbols(obj); // [Symbol()]","Objetos","js"),
("object-fromEntries","Cria objeto a partir de pares [chave,valor].","Object.fromEntries([[\"a\",1]]); // {a:1}","Objetos","js"),
("object-is","Compara dois valores (comparação precisa).","Object.is(NaN,NaN); // true","Objetos","js"),

    # --- DOM ---

    ("document","Objeto principal do DOM.","document;","DOM","js"),
    ("document.documentElement","Retorna elemento <html>.","document.documentElement;","DOM","js"),
    ("document.head","Retorna elemento <head>.","document.head;","DOM","js"),
    ("document.body","Retorna elemento <body>.","document.body;","DOM","js"),
    ("document.getElementById","Seleciona elemento pelo id.","document.getElementById('titulo');","DOM","js"),
    ("document.getElementsByClassName","Seleciona elementos pela classe.","document.getElementsByClassName('item');","DOM","js"),
    ("document.getElementsByTagName","Seleciona elementos pela tag.","document.getElementsByTagName('div');","DOM","js"),
    ("document.querySelector","Seleciona primeiro elemento via seletor CSS.","document.querySelector('.item');","DOM","js"),
    ("document.querySelectorAll","Seleciona todos via seletor CSS.","document.querySelectorAll('.item');","DOM","js"),
    ("element.innerHTML","Define ou retorna HTML interno.","const element = document.querySelector('.box'); element.innerHTML = '<b>Texto</b>';","DOM","js"),
    ("element.textContent","Define ou retorna texto.","const element = document.querySelector('.box'); element.textContent = 'Olá';","DOM","js"),
    ("element.innerText","Define ou retorna texto renderizado.","const element = document.querySelector('.box'); element.innerText = 'Olá';","DOM","js"),
    ("element.value","Define ou retorna valor de input.","const input = document.querySelector('input'); input.value = 'JS';","DOM","js"),
    ("element.setAttribute","Define atributo.","const element = document.querySelector('.box'); element.setAttribute('id','novo');","DOM","js"),
    ("element.getAttribute","Obtém atributo.","const element = document.querySelector('.box'); element.getAttribute('id');","DOM","js"),
    ("element.removeAttribute","Remove atributo.","const element = document.querySelector('.box'); element.removeAttribute('id');","DOM","js"),
    ("element.classList.add","Adiciona classe.","const element = document.querySelector('.box'); element.classList.add('ativo');","DOM","js"),
    ("element.classList.remove","Remove classe.","const element = document.querySelector('.box'); element.classList.remove('ativo');","DOM","js"),
    ("element.classList.toggle","Alterna classe.","const element = document.querySelector('.box'); element.classList.toggle('ativo');","DOM","js"),
    ("element.classList.contains","Verifica se possui classe.","const element = document.querySelector('.box'); element.classList.contains('ativo');","DOM","js"),
    ("element.style","Manipula estilo inline.","const element = document.querySelector('.box'); element.style.color = 'red';","DOM","js"),
    ("getComputedStyle","Obtém estilo computado.","const element = document.querySelector('.box'); getComputedStyle(element).color;","DOM","js"),
    ("document.createElement","Cria elemento.","document.createElement('div');","DOM","js"),
    ("element.appendChild","Adiciona filho.","const parent = document.querySelector('.container'); const child = document.createElement('div'); parent.appendChild(child);","DOM","js"),
    ("element.append","Adiciona múltiplos nós.","const parent = document.querySelector('.container'); const child = document.createElement('div'); parent.append(child);","DOM","js"),
    ("element.prepend","Adiciona no início.","const parent = document.querySelector('.container'); const child = document.createElement('div'); parent.prepend(child);","DOM","js"),
    ("element.before","Insere antes do elemento.","const element = document.querySelector('.box'); const novo = document.createElement('div'); element.before(novo);","DOM","js"),
    ("element.after","Insere depois do elemento.","const element = document.querySelector('.box'); const novo = document.createElement('div'); element.after(novo);","DOM","js"),
    ("element.replaceWith","Substitui elemento.","const element = document.querySelector('.box'); const novo = document.createElement('div'); element.replaceWith(novo);","DOM","js"),
    ("element.remove","Remove elemento.","const element = document.querySelector('.box'); element.remove();","DOM","js"),
    ("element.cloneNode","Clona elemento.","const element = document.querySelector('.box'); element.cloneNode(true);","DOM","js"),
    ("element.parentElement","Retorna pai.","const element = document.querySelector('.box'); element.parentElement;","DOM","js"),
    ("element.children","Retorna filhos.","const element = document.querySelector('.container'); element.children;","DOM","js"),
    ("element.firstElementChild","Primeiro filho.","const element = document.querySelector('.container'); element.firstElementChild;","DOM","js"),
    ("element.lastElementChild","Último filho.","const element = document.querySelector('.container'); element.lastElementChild;","DOM","js"),
    ("element.nextElementSibling","Próximo irmão.","const element = document.querySelector('.box'); element.nextElementSibling;","DOM","js"),
    ("element.previousElementSibling","Irmão anterior.","const element = document.querySelector('.box'); element.previousElementSibling;","DOM","js"),
    ("element.closest","Busca ancestral mais próximo.","const element = document.querySelector('.item'); element.closest('.container');","DOM","js"),
    ("element.matches","Verifica seletor.","const element = document.querySelector('.item'); element.matches('.ativo');","DOM","js"),
    ("addEventListener","Adiciona evento.","const button = document.querySelector('button'); button.addEventListener('click',()=>console.log('clicou'));","DOM","js"),
    ("removeEventListener","Remove evento.","const button = document.querySelector('button'); const fn = ()=>{}; button.removeEventListener('click',fn);","DOM","js"),
    ("event.preventDefault","Previne comportamento padrão.","const form = document.querySelector('form'); form.addEventListener('submit',e=>{ e.preventDefault(); });","DOM","js"),
    ("event.stopPropagation","Impede propagação.","const div = document.querySelector('.box'); div.addEventListener('click',e=>{ e.stopPropagation(); });","DOM","js"),
    ("DOMContentLoaded","Executa quando DOM carrega.","document.addEventListener('DOMContentLoaded',()=>console.log('DOM pronto'));","DOM","js"),
    ("input event","Evento ao digitar.","const input = document.querySelector('input'); input.addEventListener('input',e=>console.log(e.target.value));","DOM","js"),
    ("change event","Evento ao alterar valor.","const input = document.querySelector('input'); input.addEventListener('change',e=>console.log(e.target.value));","DOM","js"),
    ("keydown event","Evento tecla pressionada.","document.addEventListener('keydown',e=>console.log(e.key));","DOM","js"),
    ("scroll event","Evento de rolagem.","window.addEventListener('scroll',()=>console.log(window.scrollY));","DOM","js"),

    # --- Eventos ---

    ("addEventListener","Adiciona um ouvinte de evento.","const button = document.querySelector('button'); button.addEventListener('click',()=>console.log('clicou'));","Eventos","js"),
    ("removeEventListener","Remove um ouvinte de evento.","const button = document.querySelector('button'); const fn = ()=>{}; button.removeEventListener('click',fn);","Eventos","js"),
    ("event.type","Tipo do evento disparado.","document.addEventListener('click',e=>console.log(e.type));","Eventos","js"),
    ("event.target","Elemento que disparou o evento.","document.addEventListener('click',e=>console.log(e.target));","Eventos","js"),
    ("event.currentTarget","Elemento que possui o listener.","document.addEventListener('click',e=>console.log(e.currentTarget));","Eventos","js"),
    ("event.preventDefault","Previne comportamento padrão.","const form = document.querySelector('form'); form.addEventListener('submit',e=>{ e.preventDefault(); });","Eventos","js"),
    ("event.stopPropagation","Impede propagação do evento.","const div = document.querySelector('.box'); div.addEventListener('click',e=>{ e.stopPropagation(); });","Eventos","js"),
    ("event.stopImmediatePropagation","Impede execução de outros listeners.","const div = document.querySelector('.box'); div.addEventListener('click',e=>{ e.stopImmediatePropagation(); });","Eventos","js"),
    ("click","Evento de clique.","const button = document.querySelector('button'); button.addEventListener('click',()=>console.log('click'));","Eventos","js"),
    ("dblclick","Evento de duplo clique.","const button = document.querySelector('button'); button.addEventListener('dblclick',()=>console.log('duplo'));","Eventos","js"),
    ("mousedown","Botão do mouse pressionado.","document.addEventListener('mousedown',()=>console.log('down'));","Eventos","js"),
    ("mouseup","Botão do mouse solto.","document.addEventListener('mouseup',()=>console.log('up'));","Eventos","js"),
    ("mousemove","Movimento do mouse.","document.addEventListener('mousemove',e=>console.log(e.clientX));","Eventos","js"),
    ("mouseover","Mouse entra no elemento.","const div = document.querySelector('.box'); div.addEventListener('mouseover',()=>console.log('entrou'));","Eventos","js"),
    ("mouseout","Mouse sai do elemento.","const div = document.querySelector('.box'); div.addEventListener('mouseout',()=>console.log('saiu'));","Eventos","js"),
    ("keydown","Tecla pressionada.","document.addEventListener('keydown',e=>console.log(e.key));","Eventos","js"),
    ("keyup","Tecla solta.","document.addEventListener('keyup',e=>console.log(e.key));","Eventos","js"),
    ("keypress","Tecla pressionada (legado).","document.addEventListener('keypress',e=>console.log(e.key));","Eventos","js"),
    ("focus","Elemento recebe foco.","const input = document.querySelector('input'); input.addEventListener('focus',()=>console.log('focus'));","Eventos","js"),
    ("blur","Elemento perde foco.","const input = document.querySelector('input'); input.addEventListener('blur',()=>console.log('blur'));","Eventos","js"),
    ("input","Disparado ao digitar.","const input = document.querySelector('input'); input.addEventListener('input',e=>console.log(e.target.value));","Eventos","js"),
    ("change","Disparado ao alterar valor.","const input = document.querySelector('input'); input.addEventListener('change',e=>console.log(e.target.value));","Eventos","js"),
    ("submit","Envio de formulário.","const form = document.querySelector('form'); form.addEventListener('submit',e=>{ e.preventDefault(); console.log('enviado'); });","Eventos","js"),
    ("reset","Reset de formulário.","const form = document.querySelector('form'); form.addEventListener('reset',()=>console.log('resetado'));","Eventos","js"),
    ("scroll","Evento de rolagem.","window.addEventListener('scroll',()=>console.log(window.scrollY));","Eventos","js"),
    ("resize","Redimensionamento da janela.","window.addEventListener('resize',()=>console.log(window.innerWidth));","Eventos","js"),
    ("load","Página totalmente carregada.","window.addEventListener('load',()=>console.log('carregado'));","Eventos","js"),
    ("DOMContentLoaded","DOM totalmente carregado.","document.addEventListener('DOMContentLoaded',()=>console.log('DOM pronto'));","Eventos","js"),
    ("contextmenu","Clique com botão direito.","document.addEventListener('contextmenu',e=>{ e.preventDefault(); console.log('menu'); });","Eventos","js"),
    ("touchstart","Toque iniciado.","document.addEventListener('touchstart',()=>console.log('touch start'));","Eventos","js"),
    ("touchend","Toque finalizado.","document.addEventListener('touchend',()=>console.log('touch end'));","Eventos","js"),
    ("dragstart","Início de arrastar.","const div = document.querySelector('.box'); div.addEventListener('dragstart',()=>console.log('drag'));","Eventos","js"),
    ("dragover","Arrastando sobre elemento.","const div = document.querySelector('.box'); div.addEventListener('dragover',e=>{ e.preventDefault(); });","Eventos","js"),
    ("drop","Soltar elemento.","const div = document.querySelector('.box'); div.addEventListener('drop',()=>console.log('drop'));","Eventos","js"),
    ("event delegation","Delegação de eventos.","const ul = document.querySelector('ul'); ul.addEventListener('click',e=>{ if(e.target.matches('li')) console.log('item clicado'); });","Eventos","js"),
    ("once option","Executa listener apenas uma vez.","const btn = document.querySelector('button'); btn.addEventListener('click',()=>console.log('uma vez'),{ once:true });","Eventos","js"),
    ("capture option","Listener na fase de captura.","document.addEventListener('click',()=>console.log('captura'),{ capture:true });","Eventos","js"),
    ("passive option","Listener passivo (melhora performance).","window.addEventListener('scroll',()=>{}, { passive:true });","Eventos","js"),

    # --- Assincronismo ---

    ("setTimeout","Executa função após tempo determinado.","setTimeout(()=>console.log('executou'),1000);","Assincronismo","js"),
    ("clearTimeout","Cancela um setTimeout.","const id = setTimeout(()=>{},1000); clearTimeout(id);","Assincronismo","js"),
    ("setInterval","Executa função repetidamente.","const id = setInterval(()=>console.log('loop'),1000);","Assincronismo","js"),
    ("clearInterval","Cancela um setInterval.","const id = setInterval(()=>{},1000); clearInterval(id);","Assincronismo","js"),
    ("callback","Função passada como argumento.","function saudacao(cb){ cb(); } saudacao(()=>console.log('oi'));","Assincronismo","js"),
    ("callback hell","Encadeamento excessivo de callbacks.","setTimeout(()=>{ setTimeout(()=>{ console.log('fim'); },1000); },1000);","Assincronismo","js"),
    ("Promise","Objeto para operações assíncronas.","const p = new Promise((resolve,reject)=>{ resolve('ok'); });","Assincronismo","js"),
    ("Promise resolve","Resolve uma Promise.","Promise.resolve('sucesso').then(r=>console.log(r));","Assincronismo","js"),
    ("Promise reject","Rejeita uma Promise.","Promise.reject('erro').catch(e=>console.log(e));","Assincronismo","js"),
    ("then","Executa quando Promise resolve.","Promise.resolve(10).then(r=>console.log(r));","Assincronismo","js"),
    ("catch","Captura erro da Promise.","Promise.reject('erro').catch(e=>console.log(e));","Assincronismo","js"),
    ("finally","Executa sempre após Promise.","Promise.resolve().finally(()=>console.log('fim'));","Assincronismo","js"),
    ("Promise.all","Executa múltiplas Promises em paralelo.","Promise.all([Promise.resolve(1),Promise.resolve(2)]).then(r=>console.log(r));","Assincronismo","js"),
    ("Promise.race","Retorna primeira Promise resolvida.","Promise.race([Promise.resolve(1),Promise.resolve(2)]).then(r=>console.log(r));","Assincronismo","js"),
    ("Promise.allSettled","Retorna todas mesmo com erro.","Promise.allSettled([Promise.resolve(1),Promise.reject('erro')]).then(r=>console.log(r));","Assincronismo","js"),
    ("async function","Declara função assíncrona.","async function teste(){ return 'ok'; }","Assincronismo","js"),
    ("await","Espera Promise resolver.","async function teste(){ const r = await Promise.resolve(5); console.log(r); }","Assincronismo","js"),
    ("try catch async","Captura erro com async/await.","async function teste(){ try{ await Promise.reject('erro'); }catch(e){ console.log(e); } }","Assincronismo","js"),
    ("event loop","Gerencia execução assíncrona.","console.log('A'); setTimeout(()=>console.log('B'),0); console.log('C');","Assincronismo","js"),
    ("microtask queue","Fila de microtarefas (Promises).","Promise.resolve().then(()=>console.log('microtask'));","Assincronismo","js"),
    ("macrotask queue","Fila de macrotarefas (setTimeout).","setTimeout(()=>console.log('macrotask'),0);","Assincronismo","js"),
    ("queueMicrotask","Agenda microtarefa.","queueMicrotask(()=>console.log('micro'));","Assincronismo","js"),
    ("process.nextTick","Executa antes da próxima fase (Node).","process.nextTick(()=>console.log('tick'));","Assincronismo","js"),
    ("setImmediate","Executa após ciclo atual (Node).","setImmediate(()=>console.log('immediate'));","Assincronismo","js"),

    # --- Requisições HTTP ---

    ("HTTP methods","Principais métodos HTTP.","GET, POST, PUT, PATCH, DELETE;","Requisições HTTP","js"),
    ("status codes","Códigos de status HTTP.","200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Server Error;","Requisições HTTP","js"),
    ("Content-Type","Tipo de conteúdo da requisição.","'application/json', 'multipart/form-data', 'text/plain';","Requisições HTTP","js"),
    ("fetch GET","Requisição GET simples.","fetch('https://api.exemplo.com').then(r=>r.json()).then(d=>console.log(d));","Requisições HTTP","js"),
    ("fetch POST","Requisição POST com JSON.","fetch('https://api.exemplo.com',{ method:'POST', headers:{ 'Content-Type':'application/json' }, body:JSON.stringify({ nome:'Davi' }) });","Requisições HTTP","js"),
    ("fetch PUT","Requisição PUT.","fetch('https://api.exemplo.com/1',{ method:'PUT', headers:{ 'Content-Type':'application/json' }, body:JSON.stringify({ nome:'Novo' }) });","Requisições HTTP","js"),
    ("fetch DELETE","Requisição DELETE.","fetch('https://api.exemplo.com/1',{ method:'DELETE' });","Requisições HTTP","js"),
    ("fetch headers","Enviando headers personalizados.","fetch('https://api.exemplo.com',{ headers:{ Authorization:'Bearer token' } });","Requisições HTTP","js"),
    ("fetch status","Verificando status da resposta.","fetch('https://api.exemplo.com').then(r=>console.log(r.status));","Requisições HTTP","js"),
    ("response.ok","Verifica se resposta foi bem sucedida.","fetch('https://api.exemplo.com').then(r=>{ if(r.ok) console.log('sucesso'); });","Requisições HTTP","js"),
    ("response.json","Converte resposta para JSON.","fetch('https://api.exemplo.com').then(r=>r.json());","Requisições HTTP","js"),
    ("response.text","Converte resposta para texto.","fetch('https://api.exemplo.com').then(r=>r.text());","Requisições HTTP","js"),
    ("query params","Enviando parâmetros na URL.","fetch('https://api.exemplo.com?nome=Davi&idade=19');","Requisições HTTP","js"),
    ("FormData","Enviando dados de formulário.","const formData = new FormData(); formData.append('nome','Davi'); fetch('https://api.exemplo.com',{ method:'POST', body:formData });","Requisições HTTP","js"),
    ("upload file","Enviando arquivo.","const formData = new FormData(); formData.append('file',fileInput.files[0]); fetch('https://api.exemplo.com/upload',{ method:'POST', body:formData });","Requisições HTTP","js"),
    ("async fetch","Fetch usando async/await.","async function getData(){ const r = await fetch('https://api.exemplo.com'); const d = await r.json(); console.log(d); }","Requisições HTTP","js"),
    ("try catch fetch","Tratando erro com async/await.","async function getData(){ try{ const r = await fetch('https://api.exemplo.com'); if(!r.ok) throw new Error('erro'); }catch(e){ console.log(e.message); } }","Requisições HTTP","js"),
    ("AbortController","Cancelando requisição.","const controller = new AbortController(); fetch('https://api.exemplo.com',{ signal:controller.signal }); controller.abort();","Requisições HTTP","js"),
    ("credentials include","Enviando cookies na requisição.","fetch('https://api.exemplo.com',{ credentials:'include' });","Requisições HTTP","js"),
    ("mode cors","Configurando modo CORS.","fetch('https://api.exemplo.com',{ mode:'cors' });","Requisições HTTP","js"),
    ("cache control","Controlando cache.","fetch('https://api.exemplo.com',{ cache:'no-store' });","Requisições HTTP","js"),
    ("redirect manual","Controlando redirecionamento.","fetch('https://api.exemplo.com',{ redirect:'manual' });","Requisições HTTP","js"),
    ("axios GET","GET usando Axios.","axios.get('https://api.exemplo.com').then(r=>console.log(r.data));","Requisições HTTP","js"),
    ("axios POST","POST usando Axios.","axios.post('https://api.exemplo.com',{ nome:'Davi' });","Requisições HTTP","js"),
    ("axios headers","Headers no Axios.","axios.get('https://api.exemplo.com',{ headers:{ Authorization:'Bearer token' } });","Requisições HTTP","js"),
    ("XMLHttpRequest","Requisição usando XHR.","const xhr = new XMLHttpRequest(); xhr.open('GET','https://api.exemplo.com'); xhr.onload=()=>console.log(xhr.responseText); xhr.send();","Requisições HTTP","js"),

    # --- Classes e OOP ---

    ("class","Declara uma classe.","class Pessoa{}","Classes e OOP","js"),
    ("constructor","Método executado ao instanciar.","class Pessoa{ constructor(nome){ this.nome=nome; } }","Classes e OOP","js"),
    ("instance","Criação de instância com new.","const p=new Pessoa('Davi');","Classes e OOP","js"),
    ("this","Referência ao objeto atual.","class Pessoa{ constructor(nome){ this.nome=nome; } }","Classes e OOP","js"),
    ("method","Método dentro da classe.","class Pessoa{ falar(){ return 'Oi'; } }","Classes e OOP","js"),
    ("extends","Herança entre classes.","class Aluno extends Pessoa{}","Classes e OOP","js"),
    ("super","Chama construtor da classe pai.","class Aluno extends Pessoa{ constructor(nome){ super(nome); } }","Classes e OOP","js"),
    ("method override","Sobrescrita de método.","class Aluno extends Pessoa{ falar(){ return 'Olá'; } }","Classes e OOP","js"),
    ("static method","Método acessado pela classe.","class Calc{ static soma(a,b){ return a+b; } }","Classes e OOP","js"),
    ("static property","Propriedade estática.","class Pessoa{ static especie='Humano'; }","Classes e OOP","js"),
    ("getter","Define método get.","class Pessoa{ get nome(){ return this._nome; } }","Classes e OOP","js"),
    ("setter","Define método set.","class Pessoa{ set nome(valor){ this._nome=valor; } }","Classes e OOP","js"),
    ("private field","Campo privado com #.","class Pessoa{ #idade=19; }","Classes e OOP","js"),
    ("private method","Método privado.","class Pessoa{ #segredo(){ return 'x'; } }","Classes e OOP","js"),
    ("public field","Campo público direto na classe.","class Pessoa{ idade=19; }","Classes e OOP","js"),
    ("encapsulation","Encapsulamento via métodos.","class Conta{ #saldo=0; depositar(v){ this.#saldo+=v; } }","Classes e OOP","js"),
    ("polymorphism","Polimorfismo via herança.","class Animal{ falar(){ return 'som'; } } class Cachorro extends Animal{ falar(){ return 'latido'; } }","Classes e OOP","js"),
    ("abstraction","Abstração via classe base.","class Forma{ calcularArea(){ throw new Error('Implementar'); } }","Classes e OOP","js"),
    ("prototype","Métodos ficam no prototype.","Pessoa.prototype.falar=function(){ return 'Oi'; };","Classes e OOP","js"),
    ("instanceof","Verifica instância.","p instanceof Pessoa;","Classes e OOP","js"),
    ("Object.create","Cria objeto com prototype específico.","const obj=Object.create(Pessoa.prototype);","Classes e OOP","js"),
    ("composition","Composição de objetos.","const podeVoar={voar(){return 'voando';}}; const passaro={...podeVoar};","Classes e OOP","js"),

    # --- Módulos ---

    ("ES module","Arquivo JS tratado como módulo.","<script type='module' src='main.js'></script>","Módulos","js"),
    ("export named","Exportação nomeada.","export const nome='Davi';","Módulos","js"),
    ("export function","Exportando função nomeada.","export function soma(a,b){ return a+b; }","Módulos","js"),
    ("export list","Exportando múltiplos itens no final do arquivo.","const a=1; const b=2; export { a,b };","Módulos","js"),
    ("export alias","Exportação com alias.","export { soma as adicionar };","Módulos","js"),
    ("export default","Exportação padrão do módulo.","export default function soma(a,b){ return a+b; }","Módulos","js"),
    ("import named","Importação nomeada.","import { soma } from './math.js';","Módulos","js"),
    ("import multiple","Importando múltiplos itens.","import { soma,sub } from './math.js';","Módulos","js"),
    ("import alias","Importação com alias.","import { soma as adicionar } from './math.js';","Módulos","js"),
    ("import default","Importando exportação padrão.","import soma from './math.js';","Módulos","js"),
    ("import all","Importa tudo como objeto.","import * as math from './math.js';","Módulos","js"),
    ("dynamic import","Importação dinâmica assíncrona.","import('./math.js').then(m=>m.soma(2,3));","Módulos","js"),
    ("re export","Reexportando módulo.","export { soma } from './math.js';","Módulos","js"),
    ("re export all","Reexportando tudo.","export * from './math.js';","Módulos","js"),
    ("module scope","Escopo isolado de módulo.","const x=10; // não vai para window","Módulos","js"),
    ("strict mode module","Módulos rodam automaticamente em strict mode.","// em módulo 'use strict' é implícito","Módulos","js"),
    ("top level await","Uso de await no topo do módulo.","const data=await fetch(url);","Módulos","js"),
    ("CommonJS require","Importação no padrão CommonJS.","const math=require('./math');","Módulos","js"),
    ("CommonJS exports","Exportação no padrão CommonJS.","module.exports={ soma };","Módulos","js"),
    ("Node ES module","Ativando ES Modules no Node.","// package.json -> { \"type\": \"module\" }","Módulos","js"),
]   
class Command(BaseCommand):
    help = 'Seed segura com debug'

    def handle(self, *args, **kwargs): 
        for i, (nome, descricao, uso, nome_categoria, linguagem) in enumerate(codigos):
            try:
                categoria = Categoria.objects.get(
                    nome=nome_categoria,
                    linguagem=linguagem
                )

                codigo, created = Codigo.objects.get_or_create(
                    nome=nome,
                    categoria=categoria,
                    defaults={
                        'descricao': descricao,
                        'modoDeUsar': uso
                    }
                )

                if created:
                    print(f"{i} ✅ Criado: {nome}")
                else:
                    print(f"{i} ⚠ Já existia: {nome}")

            except Exception as e:
                print("\n🚨 ERRO NO ITEM:")
                print("Index:", i)
                print("Nome:", nome)
                print("Categoria:", nome_categoria)
                print("Linguagem:", linguagem)
                print("Erro:", e)
                break

        print("Seed finalizada.")
