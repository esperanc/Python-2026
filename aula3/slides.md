::: center
# Introdução à Programação com Python
## Aula 03: Repetição
:::
---
# Uma tartaruga!

Vamos introduzir a biblioteca `turtle` que nos permite desenhar figuras geométricas.

No ambiente Jupyterlite, esta biblioteca não pode no momento ser instalada, mas podemos instalar uma semelhante facilmente: a biblioteca `jupyturtle`.

Num notebook Jupyterlite, basta digitar o seguinte comando:

```python
import piplite
await piplite.install('jupyturtle', deps=False)
await piplite.install('ipycanvas') 
from jupyturtle import *
```
---

# A ideia da coisa
A tartaruga é um ser que vive numa superfície plana e pode se mover arrastando uma caneta para desenhar figuras geométricas. 

A superfície é criada pelo comando `make_turtle()`
 - É possível personalizar a superfície passando parâmetros para o comando
 - Por exemplo, `make_turtle(height=400, width=400)` cria uma superfície de 400x400 pixels

Uma vez criada a superfície, a tartaruga pode ser controlada com comandos como 
 - `forward(100)` move a tartaruga 100 pixels para frente
 - `left(90)` gira a tartaruga 90 graus para a esquerda

---
# Exemplo
:::row
:::col
```python
make_turtle(height=400, width=400) 
forward(100)
left(90)
forward(100)
```
:::
:::col
:: image { "src": "turtle01.svg" }
:::
:::

---

# Um quadrado!

::: row
::: col
```python
make_turtle(height=400, width=400) 
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
```
:::
::: col
:: image { "src": "turtle02.svg" }
:::
::: 

---

# O comando `for`

:::row
:::col
Claramente, repetir o mesmo comando várias vezes não é a melhor ideia. 

O comando `for` nos permite repetir um bloco de comandos várias vezes.

Sua forma mais usual é a seguinte:

```python
for var in range(n):
    comando
    ...
    comando
```

Onde:
 - `var` é uma variável que assume valores de 0 a n-1
 - `n` é o número de repetições
 - `comandos` são os comandos que serão repetidos
 :::
 
:::

---
# Exemplo

:::row
:::col 
 Nosso quadrado pode então ser desenhado da seguinte forma:
 
 ```python
for i in range(4):
    forward(100)
    left(90)
```
Nesse caso, `i` assume os valores 0, 1, 2 e 3 ... mas não usamos `i` dentro do loop!

Algo mais interesante:

```python
for i in range(20):
    forward (50+i*10)
    left (90)
```
:::
::: col reveal
:: image { "src": "turtle03.svg", "width": "400" }
:::
:::
---
# Repetir enquanto ...

Às vezes não sabemos quantas vezes precisamos repetir um bloco de comandos.

Mas sabemos uma condição que deve ser satisfeita para que o bloco de comandos seja repetido. 

Nesses casos, usamos o comando `while`.

```python
while condicao:
    comando
    ...
    comando
```
---
# Exemplo
:::col  
```python
f = 5
while f < 200:
    forward(f)
    f = f+5  # Não esquecer de incrementar!
    left(95)
```
:::
:::col reveal
:: image { "src": "turtle14.svg" }
:::

---
# Generalização 

Podemos criar uma função para desenhar um quadrado:
:::row
:::col
```python
def quadrado(lado):
    for i in range(4):
        forward(lado)
        left(90)
```
Assim, podemos desenhar um quadrado de qualquer tamanho passando apenas o tamanho do lado como parâmetro:

```python
quadrado(50)
quadrado(100)
```
:::
:::col reveal
:: image { "src": "turtle04.svg"}
:::
:::
---
# Generalização 2

Podemos generalizar ainda mais, criando uma função para desenhar um polígono regular:
:::row
:::col
```python
def poligono(lado, n):
    for i in range(n):
        forward(lado)
        left(360/n)

poligono(50,4)  
poligono(60,5)
poligono(70,6)
```
:::
:::col reveal
:: image { "src": "turtle05.svg"}
:::
:::

--- 
# Docstrings

Quando criamos uma função, é uma **boa prática** explicar o que ela faz, os parâmetros que ela recebe e o que ela retorna.

Isso é feito usando uma _docstring_, que é um literal string que explica o que a função faz. 

Ela é colocada entre aspas triplas (``` ou """) e é a primeira coisa que vem dentro da definição da função.

Por exemplo:

```python
def poligono(lado,n):
    """
    Desenha um polígono no ambiente jpyturtle
    Args:
        n: número de lados
        lado: comprimento do lado
    """
    for i in range(n):
        forward(lado)
        left(360/n)
```
---
# Dicas de tipo (_type hints_)

:::col
Outra boa prática é informar o **tipo** de cada parâmetro e do valor de retorno da função. 

O tipo de um parâmetro é colocado logo após o nome do parâmetro, separado por dois pontos (:).

Os seguintes tipos são comuns:
 - `int` para números inteiros
 - `float` para números reais
 - `str` para strings
 - `bool` para booleanos
:::
:::col reveal
Por exemplo:

```python
def poligono(lado : float, n : int):
    """
    Desenha um polígono no ambiente jpyturtle
    Args:
        n: número de lados
        lado: comprimento do lado
    """
    for i in range(n):
        forward(lado)
        left(360/n)
```
:::
---
# Dicas de tipo - tipo de retorno

Além disso, é possível informar o tipo de retorno da função, que é colocado após o símbolo `->`.

```python
def metade(x : float) -> float:
    return x/2
```
::: row reveal
```python
def poligono(lado : float, n : int) -> None:
    for i in range(n):
        forward(lado)
        left(360/n)
``` 

Note que `None` indica um valor nulo. É o que é assumido como valor de retorno quando uma função não retorna nada.
:::
---
# Passando argumentos por nome

Às vezes é difícil lembrar a ordem dos argumentos de uma função, especialmente se ela tiver muitos argumentos. 

Uma boa prática é passar os argumentos por nome, ou seja, indicar o nome do argumento ao chamar a função.

Por exemplo, podemos chamar a função de três formas:

```python
poligono(50,4)
poligono(n=4, lado=50)
poligono(lado=50, n=4)
```
---
# Exercício

Eis dois desenhos feitos com uma função "misteriosa", mas que foram chamadas com argumentos diferentes. Dê nome a função, colocando uma docstring apropriada e type hints. Dica: o comando `right` gira a tartaruga para a direita!

:::col
:: image { "src": "turtle06.svg" }
:::
:::col
:: image { "src": "turtle07.svg" }
:::
---
::: center
# Vamos praticar!
<button onclick="window.open('https://jupyterlite.github.io/demo/lab/index.html', '_blank')">Abrir JupyterLite</button>
:::

---

# Exercício 
:::col
Implemente a função abaixo:
```python
def arco(r : float, angulo: float) -> None:
    """
    Desenha um arco de círculo à esquerda da tartaruga 
    Args
        r: raio do arco
        angulo: ângulo do arco
    """
```
- Use uma aproximação com uns 20 segmentos de reta.
- Você vai precisar de um pouco de trigonometria para resolver isso!
- Use a biblioteca `math`.
:::
:::col
Exemplo:
```python
arco(50, 180)
```
:: image { "src": "turtle08.svg" }
:::
---

# Exercício 
:::col
Implemente a função abaixo:
```python
def petala (r : float, angulo : float) -> None:
    """
    Desenha uma pétala com dois arcos
    Args:
        r : raio do arco
        angulo: ângulo do arco
    """
```
- Dica: gire um pouco a tartaruga antes de desenhar o primeiro arco!
:::
:::col
Exemplo:
```python
petala (90, 90)
petala (80, 120)
```
:: image { "src": "turtle09.svg" }
:::

---
# Exercício 
:::col
Usando a função `petala`, desenhe algo parecido com o desenho ao lado:

Dicas
- Você pode usar um loop para desenhar uma flor com muitas pétalas!
- O desenho tem 3 flores sobrepostas

:::
::: col
:: image { "src": "turtle10.svg" }
:::
--- 
# Mais comandos de tartaruga

:::col
Para a tartaruga deixar de desenhar, mas ainda assim andar, use o comando `penup()`. Para a tartaruga voltar a desenhar, use o comando `pendown()`. 

Para a tartaruga andar para trás, use o comando `back()`. 

Usando esses comandos, escreva a função
```python
def caixa(largura : float, altura: float) -> None:
    """
    Desenha uma caixa retangular centralizada na
    posição atual da tartaruga
    Args:
        largura: lado da caixa ao longo da direção atual
        altura: lado perpendicular à direção atual 
    """
```
Exemplo:
```python
caixa (200,150)
```

:::
:::col
:: image { "src": "turtle11.svg" }
:::
---
# Exercício
Escreva a função
```python
def caixas_aninhadas(largura, altura, n):
    """
    Desenha caixas aninhadas, todas com a mesma razão de aspecto,
    sendo que cada caixa de dentro é orientada a 90 graus da caixa
    de fora
    Args: 
        largura: largura da caixa mais externa
        altura: altura da caixa mais externa
        n: número total de caixas
    """
```
- Dica: use a função `caixa` que já foi escrita!
---
:::col 
```python
caixas_aninhadas (200,150,5)
```
:: image { "src": "turtle12.svg" }
:::
:::col 
```python
caixas_aninhadas(150,200,4)
```
:: image { "src": "turtle13.svg" }
:::