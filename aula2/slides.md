::: center
# Introdução à Programação com Python
## Aula 02: Conceitos Básicos

:::

---

# Estrutura de um programa Python

É um arquivo de texto, tipicamente salvo com a extensão `.py`.

- No ambiente Jupyter, é um arquivo `.ipynb`.

Cada linha do arquivo contém uma instrução que o interpretador Python executa.

- No ambiente Jupyter, cada célula contém um _trecho_ de código

Há instruções que não são executadas, como comentários. Exemplo:

```python
# Isto é um comentário
print("Hello, World!")
```

Para executar um programa Python salvo como um arquivo `.py`, use o comando `python nome_do_arquivo.py`.

- No ambiente Jupyter, use o botão "Run" ou pressione `Shift + Enter`.

---

# Tipos de Dados

Python pode processar dados numéricos (inteiros e reais), texto (strings) e booleanos (verdadeiro ou falso).

```python
# Números inteiros
print (1)

# Números reais
print (1.5)

# Texto
print ("Olá, Mundo!")

# Booleanos
print (True)
print (False)

# None (um tipo nulo!)
print (None)
```
---
# O que é `print`?

O `print` é uma função que exibe um ou mais valores.

Normalmente não é necessário usá-la, mas ela é útil para depurar o código, ou seja, para verificar se o código está funcionando corretamente.

No console, ela exibe o valor na linha seguinte ao código.
---

# Expressões

São sequências de operações que resultam em um valor. Cada operação envolve operandos (valores) e  operadores (símbolos que indicam a operação). Por exemplo:

```python
print (1 + 5) # Soma
print (1 - 5) # Subtração
print (1 * 5) # Multiplicação
print (1 / 5) # Divisão
print (1 // 5) # Divisão inteira
print (1 % 5) # Resto da divisão
print (2 ** 5) # Potência
```
---
# Inteiros e reais

Números inteiros e reais (ponto-flutuante) comportam-se diferentemente e são representados de forma diferente.

```python
print (1/2) # 0.5
print (1//2) # 0
print (1.0 // 2) # 0.0
print (1.0 / 2) # 0.5
print (1.0 % 2) # 1.0
print (1 % 2) # 1
```
---
# Strings (cadeias de caracteres)

Literais strings são caracteres entre aspas (simples ou duplas):

```python
print ("Oi")
print ('Oi')
```

Naturalmente, os caracteres dentro das aspas não podem conter aspas. 
Mas é possível sinalizar que a string não termina ali precedendo-o com uma barra invertida.

```python
print ("Oi \"meu chapa\"!")
```
---
# Operadores string

- O operador `+` quando aplicado a strings significa concatenação
- O operador `*` quando aplicado a uma string e um inteiro significa repetição

```python
print ("Oi " + '"meu chapa"!') 
print ('Oi "meu chapa"' + "!"*4)
```
Resultado:
```
Oi "meu chapa"!
Oi "meu chapa"!!!!
```

---
# Precedência de operadores

As operações são executadas da esquerda para a direita.

Alguns operadores têm precedência sobre outros.

1. Parênteses `()`
2. Potência `**`
3. Operadores unários: `+` e `-`
4. Multiplicação `*`, divisão `/`, divisão inteira `//` e resto `%`
5. Adição `+` e subtração `-`

---
# Exemplos

```python
print (2 + 3 * 4) # 14
print ((2 + 3) * 4) # 20
print (-3 ** 2) # -9
print ((-3) ** 2) # 9
print (6 / 3 % 5) # 2.0
print (2 ** 3 ** 2) # 512
print ((2 ** 3) ** 2) # 64
```
---

# Outros operadores

Os operadores aritméticos operam sobre números e resultam em números. Além desses, temos
- Relacionais: 
  - `==` (igualdade), `!=` (diferença),
  - `is` (idêntico), `is not` (não idêntico), 
  - `>` (maior), `<` (menor), `>=` (maior ou igual), `<=` (menor ou igual),
  - `in` (pertence), `not in` (não pertence)
  - operandos são valores quaisquer (ex.: números ou strings)
  - resultado é um valor booleano (`True` ou `False`)
- Lógicos: 
  - `and` (e), `or` (ou), `not` (não)
  - operandos são valores booleanos
  - resultado é um valor booleano

--- 
# Exemplos

```python
print (1+2 > 3) # False
print (1+2 >= 3) # True
print (1+2 < 3 and 1+2 == 3) # False
print (1+2 < 3 or 1+2 == 3) # True
print (not (1+2 == 3)) # False
print (1+2 is 3) # True
print (1+2 is 3.0) # False
print (1 in (1, 2, 3)) # True
print (1 in (1.0, 2, 3)) # True
```
---
# Variáveis

São nomes que representam valores. 

Um nome válido deve:
- Ter letras, números e `_`
- Não pode começar com números
- Não pode ser uma palavra reservada

Definimos uma variável atribuindo um valor a ela. 

O comando de _atribuição_ é da forma 

```python
nome = expressão
```

Por exemplo: 

```python
x = 1
y = 2 + x
```
--- 
# Atribuição com operadores

Existe uma forma mais compacta de escrever algumas atribuições:

```python
x = x + 1
y = y / z
```

podem ser escritas como:

```python
x += 1
y /= z
```
---
# `input`

Quando executada, a função `input (mensagem)` imprime a mensagem (se houver), suspende a execução do programa, e espera a digitação de uma string como resposta. 

Normalmente usada com atribuição a uma variável:

```python
nome = input ("Qual seu nome ?")
print ("Oi ", nome, "!")
```

Execução:

```
Qual seu nome ? João
Oi João!
```
---
# `input` com conversão

Às vezes, é necessário converter o valor de uma string para outro tipo.

:::col 
```python
a = input ("Entre com um número: ")
b = input ("Entre com outro número: ")
print ("A soma é: ", a + b)
```

Execução:

```
Entre com um número: 1.23452352
Entre com outro número: 2.3456789
A soma é:  1.234523522.3456789
```
:::

:::col reveal
```python
a = float (input ("Entre com um número: "))
b = float (input ("Entre com outro número: "))
print ("A soma é: ", a + b)
```

Execução:

```
Entre com um número: 1.23452352
Entre com outro número: 2.3456789
A soma é:  3.58019241
```
:::
---
# Usando f-strings para imprimir valores

As f-strings (strings formatadas)permitem formatar strings de forma mais flexível. 

Uma f-string é uma string precedida da letra `f` que contém expressões entre chaves `{}`.

```python
a = float (input ("Entre com um número: "))
b = float (input ("Entre com outro número: "))
print (f"A soma é: {a + b}")
```

Execução:

```
Entre com um número: 1.23452352
Entre com outro número: 2.3456789
A soma é:  3.58019241
```
---
# Número de casas decimais

f-strings têm diversas opções para formatar números. 

Um sinal de ":" depois da expressão indica que se seguem opções de formatação.

Alguns exemplos:
```python
print (f"{0.123456:.2f}") # 0.12
print (f"{0.123456:.3f}") # 0.123
print (f"{0.123456:.0f}") # 0
print (f"{0.123456:10.5f}")  #    0.12346
print (f"{0.123456:010.5f}") # 0000.12346
```
---
::: center
# Comandos de decisão
:::
---
#  `if` simples
```python
if condição:
    instrução
    ...
    instrução
```

- `condição` é uma expressão que resulta em um valor booleano
- `instruções` são instruções que são executadas se a condição for verdadeira

---
# Exemplos

```python
if x > 0:
    print ("x é positivo")
```

::: reveal
```python
if x > 0:
    print  ("x é positivo")
    if y > 0:
        print ("y também é positivo")
```
:::

---
# Blocos e indentação

Como o `if`, muitas vezes o Python usa a _indentação_ para indicar _blocos_ de código.

Todos os comandos com a mesma indentação pertencem ao mesmo bloco.

Comandos com indentação maior pertencem ao bloco do comando anterior.

Podemos ter blocos dentro de blocos, dentro de blocos, etc. 
- Isto é chamado de _aninhamento_
---
# `if` com `else`

```python
if condição:
    instrução # se a condição for verdadeira
    ...
    instrução
else:
    instrução # se a condição for falsa
    ...
    instrução
```
---
# Exemplos

:::row
:::col
```python
if x > 0:
    print ("x é positivo")
else:
    print ("x não é positivo")
```
:::

:::col reveal
```python
if x > 0:
    print ("x é positivo")
    if y > 0:
        print ("y também é")
    else:
        print ("mas y não é")
else:
    print ("x não é positivo")
    if y > 0:
        print ("mas y é")
    else:
        print ("nem y tampouco")
```
:::
:::
---
# `if` com `elif`   

```python
if condição 1:
    instrução # se a condição 1 for verdadeira
elif condição 2:
    instrução # se a condição 1 for falsa e a condição 2 for verdadeira
...
elif condição n:
    instrução # se todas as anteriores forem falsas e esta verdadeira
else:
    instrução # se todas forem falsas
```
---
# Exemplo
```python
if x > y:
    print ("x maior que y")
elif x < y:
    print ("x menor que y")
else:
    print ("x igual a y")
```

---

# Exemplo clássico: equação do segundo grau

```python
a = 1
b = 2
c = 1

delta = b**2 - 4*a*c
if delta < 0:
    print("Delta negativo, não há solução real")
elif delta == 0:
    x = -b / (2*a)
    print("x =", x)
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)
```
---

::: center
# Vamos praticar!
<button onclick="window.open('https://jupyterlite.github.io/demo/lab/index.html', '_blank')">Abrir JupyterLite</button>
:::

---
# Funções

Uma função define um bloco de código que pode ser invocado a qualquer momento. 

Definição de uma função:

```python
def nome_da_função(parametros):
    instruções
    ...
    instruções
```

Invocação de uma função:

```python
nome_da_função(valores)
```
---
# Exemplo

```python
def saudacao(nome):
    print ("Olá, " + nome)

saudacao("Claudio")
saudacao("Maria")
saudacao("João")
```

---
# Parâmetros (argumentos)

Se uma função espera parâmetros, devemos passar valores para eles.

Podemos pensar que os parâmetros são variáveis que recebem valores quando a função é invocada.

**Importante:** os parâmetros só existem dentro da função!

```python
def saudacao(nome):
    print ("Olá, " + nome)

saudacao("Claudio")
print (nome) # Erro!
```
--- 
# Parâmetros opcionais

Parâmetros podem ser opcionais, se forem declarados com um valor padrão (_"default"_).

```python
def saudacao(nome, chamada="Olá"):
    print (chamada + ", " + nome)

saudacao("Claudio")
saudacao("Maria", "Oi")
saudacao("João", "E aí")
```

Como os parâmetros são passados em ordem, apenas os últimos podem ser opcionais.
---
# Passando parâmetros por nome

Podemos passar parâmetros por nome, isto é, não precisamos passar os parâmetros na ordem em que foram declarados.

```python
def saudacao(nome, chamada="Olá"):
    print (chamada + ", " + nome)

saudacao("Claudio")
saudacao(chamada="Oi", nome="Maria")
saudacao("Claudio", chamada="E aí")
```
Uma vez que passamos um parâmetro por nome, todos os parâmetros seguintes devem ser passados por nome.
```python
saudacao(chamada="Oi", "Maria") # inválido
```
---
# `return`

Os argumentos são valores passados do chamador para a função.

A função pode _retornar_ um valor para o chamador através do comando `return`

```python
def soma(a, b):
    return a + b

print (soma(1, 2))
```
---
::: center
# Vamos praticar!

Que tal converter nosso código para uma função?

<button onclick="window.open('https://jupyterlite.github.io/demo/lab/index.html', '_blank')">Abrir JupyterLite</button>
:::

---
# Bibliotecas

São repositórios de código que podem ser usados para resolver problemas comuns.

Por exemplo, a biblioteca `math` fornece funções para operações matemáticas como raiz quadrada, seno, cosseno, etc.

Para usar uma biblioteca, devemos importá-la usando `import`.

Usa-se a notação `biblioteca.funcao` para acessar as funções da biblioteca.

```python
import math

print (math.sqrt(4)) # Raiz quadrada de 4
print (math.sin(math.pi /4)) # Seno de 45 graus
```

---

# Importando elementos específicos

Ao invés de importar toda a biblioteca, podemos importar apenas os elementos que precisamos usando `from`.

```python
from math import sqrt, sin, pi

print (sqrt(4))
print (sin(pi /4))
```
Podemos até importar todos os elementos de uma biblioteca (não recomendado):

```python
from math import *

print (sin(sqrt(pi)))
```

---
# Exercício: Ponto em círculo

Escreva uma função

```python
def ponto_em_circulo(x, y, cx, cy, r):
    ...
```

que receba como parâmetros
- um ponto com coordenadas `x` e `y`,
- um círculo com centro em `cx`, `cy` e raio `r`,

e retorne `True` se o ponto está dentro do círculo ou `False` caso contrário.
---
:::center
# Até a próxima!
:::




