# Python Mundo 123

Repositório de estudos do curso **"Curso em Vídeo - Python"** do Gustavo Guanabara. Aqui ficam os exercícios (`exXXX` e `dXX` = desafios) e os códigos feitos junto com as aulas (`aulaXXX`), organizados por módulo do curso.

Cada arquivo tem comentários meus mostrando onde acertei de primeira, onde precisei colar uma ideia, onde o Claude ajudou e onde simplesmente não entendi nada. A ideia não é exibir código perfeito, é registrar o processo de aprendizado mesmo.

## Como navegar

- `aulaXXX.py` → código feito durante a aula, acompanhando o professor
- `dXX.py` → desafios propostos no fim de cada aula
- `exXX.py` → exercícios extras

## Mundo 1 — Fundamentos

| Arquivo | Conteúdo |
|---|---|
| [`ex001.py`](Mundo%201/ex001.py) | Primeiro "Olá Mundo" |
| [`ex002.py`](Mundo%201/ex002.py) | `input()` + `.format()` para saudação |
| [`ex03.py`](Mundo%201/ex03.py) | Soma de dois números com `.format()` |
| [`ex004.py`](Mundo%201/ex004.py) | Métodos de string: `isnumeric`, `isalpha`, `isupper`, etc. |
| [`teste.py`](Mundo%201/teste.py) | Cadastro simples (nome, idade, peso) com `print` concatenando |
| [`aula06b.py`](Mundo%201/aula06b.py) | Métodos de validação de string (`isalnum`, `isnumeric`, `isalpha`...) |
| [`aula07a.py`](Mundo%201/aula07a.py) | Formatação de strings com alinhamento (`{:>20}`, `{:^20}`, etc.) |
| [`aula07b.py`](Mundo%201/aula07b.py) | Operações aritméticas (soma, multiplicação, divisão, divisão inteira, exponenciação) formatadas |
| [`aula08a.py`](Mundo%201/aula08a.py) | Biblioteca `math`: `sqrt` e `floor` |
| [`aula09a.py`](Mundo%201/aula09a.py) | Manipulação de strings: slicing, `count`, `find`, operador `in` |
| [`aula010a.py`](Mundo%201/aula010a.py) | Estrutura condicional simples (`if`) e composta (`if/else`) |
| [`aula010b.py`](Mundo%201/aula010b.py) | Média de duas notas com condicional |
| [`aula011a.py`](Mundo%201/aula011a.py) | Cores no terminal com códigos ANSI (`\033[31m`) |
| [`d1.py`](Mundo%201/d1.py) | Desafio 1: saudação com nome |
| [`d2.py`](Mundo%201/d2.py) | Desafio 2: data de nascimento formatada |
| [`d3.py`](Mundo%201/d3.py) | Desafio: soma de dois números inteiros |
| [`d5.py`](Mundo%201/d5.py) | Antecessor e sucessor de um número |
| [`d6.py`](Mundo%201/d6.py) | Dobro, triplo e raiz quadrada |
| [`d7.py`](Mundo%201/d7.py) | Média de duas notas |
| [`d8.py`](Mundo%201/d8.py) | Conversão de metros para centímetros e milímetros |
| [`d9.py`](Mundo%201/d9.py) | Tabuada de um número (versão "na mão", sem loop) |
| [`d10.py`](Mundo%201/d10.py) | Conversão de reais para dólares |
| [`d11.py`](Mundo%201/d11.py) | Cálculo de litros de tinta para pintar parede |
| [`d12.py`](Mundo%201/d12.py) | Desconto de 5% em produto |
| [`d13.py`](Mundo%201/d13.py) | Aumento de salário de 15% |
| [`d14.py`](Mundo%201/d14.py) | Conversão de Celsius para Fahrenheit |
| [`d15.py`](Mundo%201/d15.py) | Cálculo de aluguel de carro (diária + km rodado) |
| [`d16.py`](Mundo%201/d16.py) | Parte inteira de um número com `math.trunc` |
| [`d17.py`](Mundo%201/d17.py) | Hipotenusa com `math.hypot` |
| [`d18.py`](Mundo%201/d18.py) | Seno, cosseno e tangente com `math.radians` |
| [`d19.py`](Mundo%201/d19.py) | Escolher aluno aleatório com `random.choice` |
| [`d20.py`](Mundo%201/d20.py) | Embaralhar lista com `random.shuffle` |
| [`d21.py`](Mundo%201/d21.py) | Tentativa de tocar áudio com `pygame` — **não funciona** (incompatibilidade de versão, deixei registrado como aprendizado) |
| [`d22.py`](Mundo%201/d22.py) | Nome em maiúsculas/minúsculas, contagem de letras, primeiro nome |
| [`d23.py`](Mundo%201/d23.py) | Separar unidade, dezena, centena e milhar de um número com `//` e `%` |
| [`d24.py`](Mundo%201/d24.py) | Verificar se uma cidade começa com "Santo" (`.startswith`) |
| [`d25.py`](Mundo%201/d25.py) | Verificar se o nome contém "Silva" (operador `in`) |
| [`d26.py`](Mundo%201/d26.py) | Contar ocorrências da letra "A" em uma frase, achar primeira e última posição |
| [`d27.py`](Mundo%201/d27.py) | Separar primeiro e último nome com `.split()` |
| [`d28.py`](Mundo%201/d28.py) | Jogo de adivinhação simples (0 a 5) com `random.choice` |
| [`d29.py`](Mundo%201/d29.py) | Cálculo de multa por excesso de velocidade |
| [`d30.py`](Mundo%201/d30.py) | Par ou ímpar com `%` |
| [`d31.py`](Mundo%201/d31.py) | Preço de passagem por distância (com regra condicional de desconto) |
| [`d32.py`](Mundo%201/d32.py) | Verificar ano bissexto, com `date.today()` para pegar o ano atual |
| [`d33.py`](Mundo%201/d33.py) | Maior e menor entre 3 números com `max()`/`min()` |
| [`d34.py`](Mundo%201/d34.py) | Reajuste de salário condicional (10% ou 15%) |
| [`d35.py`](Mundo%201/d35.py) | Verificar se 3 medidas formam um triângulo (desigualdade triangular) |

## Mundo 2 — Estruturas de decisão e repetição

| Arquivo | Conteúdo |
|---|---|
| [`aula012a.py`](Mundo%202/aula012a.py) | Condicionais aninhadas com `if/elif/else` |
| [`aula013a.py`](Mundo%202/aula013a.py) | Introdução ao `for` com `range()` (início, fim, passo) |
| [`aula013b.py`](Mundo%202/aula013b.py) | Somatório de valores digitados em loop `for` |
| [`aula014.py`](Mundo%202/aula014.py) | Introdução ao `while`, contagem de pares e ímpares |
| [`aula015.py`](Mundo%202/aula015.py) | `while True` com `break` (loop infinito controlado) |
| [`d36.py`](Mundo%202/d36.py) | Simulador de aprovação de empréstimo bancário |
| [`d37.py`](Mundo%202/d37.py) | Conversor de número para binário, octal e hexadecimal |
| [`d38.py`](Mundo%202/d38.py) | Comparação entre dois números (maior/menor/igual) |
| [`d39.py`](Mundo%202/d39.py) | Cálculo de tempo até/desde o alistamento militar |
| [`d40.py`](Mundo%202/d40.py) | Situação do aluno (aprovado/recuperação/reprovado) com cores no terminal |
| [`d41.py`](Mundo%202/d41.py) | Categoria de atleta por idade, com `sleep()` simulando carregamento |
| [`d42.py`](Mundo%202/d42.py) | Classificação de triângulo (equilátero/isósceles/escaleno) |
| [`d43.py`](Mundo%202/d43.py) | Cálculo de IMC com classificação |
| [`d44.py`](Mundo%202/d44.py) | Calculadora de forma de pagamento com desconto/juros |
| [`d45.py`](Mundo%202/d45.py) | Jogo Pedra, Papel e Tesoura contra o computador |
| [`d46.py`](Mundo%202/d46.py) | Contagem regressiva de Ano Novo com `sleep()` |
| [`d47.py`](Mundo%202/d47.py) | Listar números pares de 0 a 50 |
| [`d48.py`](Mundo%202/d48.py) | Soma de ímpares múltiplos de 3 até 500 |
| [`d49.py`](Mundo%202/d49.py) | Tabuada com `for` (versão com loop, evolução do `d9.py`) |
| [`d50.py`](Mundo%202/d50.py) | Contador e acumulador: soma de números pares digitados |
| [`d51.py`](Mundo%202/d51.py) | Progressão aritmética (10 primeiros termos) |
| [`d52.py`](Mundo%202/d52.py) | Verificador de número primo |
| [`d53.py`](Mundo%202/d53.py) | Verificador de palíndromo |
| [`d54.py`](Mundo%202/d54.py) | Contagem de pessoas maiores de idade entre 7 cadastros |
| [`d55.py`](Mundo%202/d55.py) | Maior e menor peso entre 5 valores digitados |
| [`d56.py`](Mundo%202/d56.py) | Cadastro de 4 pessoas: média de idade, mulheres com menos de 20, homem mais velho |
| [`d57.py`](Mundo%202/d57.py) | Validação de entrada (sexo F/M) com `while` |
| [`d58.py`](Mundo%202/d58.py) | Jogo de adivinhação (0 a 10) contando tentativas |
| [`d59.py`](Mundo%202/d59.py) | Calculadora com menu de opções em loop (`while True` + `continue`/`quit`) |
| [`d60.py`](Mundo%202/d60.py) | Fatorial de um número com `math.factorial` |
| [`d61.py`](Mundo%202/d61.py) | Progressão aritmética com `while` (10 termos) |
| [`d62.py`](Mundo%202/d62.py) | PA com `while`, permitindo exibir mais termos sob demanda |
| [`d63.py`](Mundo%202/d63.py) | Sequência de Fibonacci |
| [`d64.py`](Mundo%202/d64.py) | Contador de valores digitados até receber 999 (sentinela) |
| [`d65.py`](Mundo%202/d65.py) | Média, maior e menor valor de uma sequência digitada pelo usuário |
| [`d66.py`](Mundo%202/d66.py) | Soma de valores digitados até o sentinela 999 |
| [`d67.py`](Mundo%202/d67.py) | Tabuada em loop, repetindo até número negativo |
| [`d68.py`](Mundo%202/d68.py) | Jogo de Par ou Ímpar contra o computador |
| [`d69.py`](Mundo%202/d69.py) | Cadastro de pessoal com estatísticas (idade, sexo) |
| [`d70.py`](Mundo%202/d70.py) | Loja: total de compras, produtos caros, produto mais barato |
| [`d71.py`](Mundo%202/d71.py) | Caixa eletrônico: cálculo de cédulas (50/20/10/1) para um valor de saque |

## Mundo 3 — Listas, tuplas, dicionários, funções e arquivos

| Arquivo | Conteúdo |
|---|---|
| [`aula016.py`](Mundo%203/aula016.py) | Tuplas, `enumerate()` e `sorted()` |
| [`aula016a.py`](Mundo%203/aula016a.py) | Tuplas são imutáveis — slicing e indexação |
| [`aula017.py`](Mundo%203/aula017.py) | Listas: `append`, `insert`, `remove`, `sort`, cópia de listas com `[:]` vs referência |
| [`aula018b`](Mundo%203/aula018b) | Lista de listas (registro de pessoas com nome + idade) |
| [`aula19.py`](Mundo%203/aula19.py) | Anotação rápida sobre dicionários |
| [`d72.py`](Mundo%203/d72.py) | Números por extenso de 0 a 20 usando tupla como "dicionário" |
| [`d73.py`](Mundo%203/d73.py) | Manipulação de tupla com times do Brasileirão (slicing, `sorted`, `index`) |
| [`d74.py`](Mundo%203/d74.py) | Tupla de 5 números aleatórios, com `min()`/`max()` |
| [`d75.py`](Mundo%203/d75.py) | Tupla com 4 números: contagem, posição, ocorrências |
| [`d76.py`](Mundo%203/d76.py) | Lista de preços em tupla, exibida em formato de tabela |
| [`d77.py`](Mundo%203/d77.py) | Contagem de vogais em uma lista de palavras |
| [`d78.py`](Mundo%203/d78.py) | Maior e menor valor de uma lista, incluindo posições repetidas |
| [`d79.py`](Mundo%203/d79.py) | Lista sem valores duplicados, com validação de entrada |
| [`d80.py`](Mundo%203/d80.py) | Inserção ordenada em lista (insertion sort manual) |
| [`d81.py`](Mundo%203/d81.py) | Lista sem duplicados, ordenada de forma decrescente, com busca |
| [`d82.py`](Mundo%203/d82.py) | Separação de números pares e ímpares em listas distintas |
| [`d83.py`](Mundo%203/d83.py) | Validador de parênteses balanceados em uma expressão |
| [`d84.py`](Mundo%203/d84.py) | Cadastro de pessoas (nome + peso) com maior e menor peso |
| [`d85.py`](Mundo%203/d85.py) | Lista de listas para separar pares e ímpares |
| [`d86.py`](Mundo%203/d86.py) | Matriz 3x3 preenchida pelo usuário e exibida |
| [`d87.py`](Mundo%203/d87.py) | Matriz 3x3: soma de pares, soma da 3ª coluna, maior valor da 2ª linha |
| [`d88.py`](Mundo%203/d88.py) | Gerador de jogos da Mega-Sena (números aleatórios sem repetição) |
| [`d89.py`](Mundo%203/d89.py) | Boletim de alunos: cadastro, listagem em tabela e consulta por código |
| [`d90.py`](Mundo%203/d90.py) | Dicionário de aluno: nome, média e situação |
| [`d91.py`](Mundo%203/d91.py) | Simulação de dados com dicionário de jogadores e `randint` |
| [`d92.py`](Mundo%203/d92.py) | Dicionário com nome e ano de nascimento, calculando idade com `datetime` |
| [`d93.py`](Mundo%203/d93.py) | Registro de gols por partida com lista de dicionários |
| [`d94.py`](Mundo%203/d94.py) | Cadastro de pessoas com estatísticas (mulheres, acima da média) usando dicionários |
| [`d95.py`](Mundo%203/d95.py) | Lista de jogadores com dicionários e `.copy()` para evitar bug de referência |
| [`d96.py`](Mundo%203/d96.py) | Cálculo de área de terreno usando funções (`def`) |
| [`d97.py`](Mundo%203/d97.py) | Função `escreva()` com tamanho adaptável usando `~` |
| [`d98.py`](Mundo%203/d98.py) | Função `contador()` com início, fim, passo e contagem personalizada |
| [`d99.py`](Mundo%203/d99.py) | Função `maior()` com `*args` para receber múltiplos valores |
| [`d100.py`](Mundo%203/d100.py) | Sorteio de números sem repetição com `random.sample` e soma dos pares |
| [`d101.py`](Mundo%203/d101.py) | Verificador de aptidão para votar usando `datetime` e funções |
| [`d102.py`](Mundo%203/d102.py) | Função `fatorial()` com parâmetro `show` para exibir a conta passo a passo |
| [`d103.py`](Mundo%203/d103.py) | Função `ficha()` com parâmetros opcionais e tratamento de campos vazios |
| [`d104.py`](Mundo%203/d104.py) | Função `leiaInt()` com validação via `isnumeric()` |
| [`d105.py`](Mundo%203/d105.py) | Função `notas()` com `*args` retornando dicionário com estatísticas da turma |
| [`d106.py`](Mundo%203/d106.py) | Sistema de ajuda interativo (PyHELP) com `help()` e cores ANSI |
| [`d107/`](Mundo%203/d107) | Módulo `funcoes.py` com `metade`, `dobro`, `aumentar`, `diminuir`, `moeda` |
| [`d108/`](Mundo%203/d108) | Módulo `funcoes.py` + parâmetro `fmt` para formatar saída com `moeda()` |
| [`d109/`](Mundo%203/d109) | Adição de função `resumo()` ao módulo de funções financeiras |
| [`d110/`](Mundo%203/d110) | Refatoração com `aum` e `red` como parâmetros de percentual |
| [`d111/`](Mundo%203/d111) | Pacote `utilidadescev` com submódulo `funcoes` |
| [`d112/`](Mundo%203/d112) | Pacote com `funcoes` e `dado` (inclui `leiadinheiro()` com validação) |
| [`d113.py`](Mundo%203/d113.py) | `leiaInt()` e `leiaReal()` com `try/except` em loop |
| [`d114.py`](Mundo%203/d114.py) | Verificador de acesso ao site Pudim com `urllib.request` |
| [`d115/`](Mundo%203/d115) | Sistema de cadastro com menu, leitura e escrita em arquivo `.txt` |
| [`d115 - resolucao/`](Mundo%203/d115%20-%20resolucao) | Resolução do professor para o d115 — estrutura com pacote `ex115.lib` |

## Sobre os comentários no código

Bati em vários desses desafios sem saber a solução de cara — isso fica registrado nos próprios arquivos: trechos comentados mostram tentativas anteriores, lugares onde usei a resolução oficial do curso pra comparar com a minha, e pontos onde pedi ajuda do Claude (principalmente em laços de repetição e listas de listas, que foi onde mais travei). Mantive isso de propósito: é mais útil pra mim revisar depois sabendo onde realmente entendi e onde só copiei.