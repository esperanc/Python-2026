::: center
# Introdução à Programação com Python
## Aula 6: Recursão
:::
---
# Indução matemática

- Técnica de prova matemática 
- Usada para provar que uma propriedade é válida para um conjunto _enumerável_ (que se pode contar).
- Baseada em dois princípios:

  1. **Caso(s) base**: Provar que a propriedade é válida para alguns elementos conhecidos
    - Tipicamente o primeiro (ou alguns poucos).

  2. **Passo indutivo**: Provar que, se a propriedade é válida para o _n_-ésimo elemento, vale também para o _n+1_-ésimo.
    - **Importante**: Aqui é permitido _assumir_ que a propriedade é válida para o _n_-ésimo elemento

- <u>Ideia implícita</u>: O caso geral fatalmente cai em um dos casos base.

---
# Exemplo: soma dos primeiros _n_ números naturais

Seja $P(n)$ a propriedade de que a soma dos primeiros _n_ números naturais é igual a $\frac{n(n+1)}{2}$.

1. **Caso base**: Provar que $P(1)$ é válida.

> $$
 P(1) = \frac{1(1+1)}{2} = \frac{1 \times 2}{2} = 1
 $$


2. **Passo indutivo**: Provar que, se $P(n)$ é válida, então $P(n+1)$ também é válida.

> $$
P(n+1) = P(n) + (n+1) = \frac{n(n+1)}{2} + \frac{2(n+1)}{2} = \frac{(n+1)(n+2)}{2}
$$

---
# Recursão

É o análogo computacional da indução matemática.

Uma função é _recursiva_ se ela chama a si mesma 
  - Pode ser de forma direta ou indireta (a função chama outra função, que chama outra função, que chama a primeira função)

---
# Estrutura de uma função recursiva

Para definir uma função recursiva, precisamos:

1. Definir um ou mais casos base
  - O problema tem uma solução trivial?
  - Se sim, retorna a solução
2. Definir um passo indutivo
  - Se não, o problema é reduzido a um ou mais problemas menores 
  - Problema _menor_ computado recursivamente

---
# Exemplo: lista contém elemento?

:::col
Versão iterativa:
```python
def contem (lst, x):
    for e in lst:
        if e == x:
            return True
    return False
```
:::
::: col
Versão recursiva:
```python
def contem_rec (lst, x):
    if len(lst) == 0:
        return False
    if lst[0] == x:
        return True
    return contem_rec(lst[1:], x)
```
:::
---
# Exemplo: índice de um elemento

:::col
Versão iterativa:
```python
def indice (lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1
```
:::
::: col
Versão recursiva:
```python
def indice_rec (lst, x):
    if len(lst) == 0:
        return -1
    if lst[0] == x:
        return 0
    i = indice_rec(lst[1:], x)
    if i == -1:
        return -1
    return i + 1
```
:::
---
# Recursão e repetição

Muitas vezes a versão não recursiva é mais eficiente do que a versão recursiva.

Por exemplo, a versão iterativa de `contem` e `indice` são mais eficientes do que as versões recursivas.

 - Fazer o fatiamento da lista e a chamada recursiva é mais custoso do que o loop

Há situações em que a versão recursiva é mais eficiente ou mais _simples_ do que a versão iterativa.

 - Há problemas que são naturalmente recursivos

---
# Exemplo: encontrar uma subsequência

:::col
Uma sequência `s` é uma subsequência de uma sequência `t` se:

1. `s` é vazia, ou
2. `s[0]` é igual a `t[i]` para algum índice `i` **e** 
`s[1:]` é uma subsequência de `t[i+1:]`

Podemos ver que esta definição é recursiva!
:::
::: col reveal
A transcrição para código é imediata:
```python
def subsequencia(s,t):
    if len(s) == 0: return True
    for i in range(len(t)):
        if s[0] == t[i]:
            return subsequencia(s[1:],t[i:])
    return False
```
:::
---
# Exemplo clássico: busca binária

Seja `lst` uma lista ordenada e `x` um elemento.

1. Se `lst` é vazia, `x` não está em `lst`.
2. Se `lst` tem exatamente um elemento, `x` é esse elemento ou `x` não está na lista.
3. Se `lst` tem 2 ou mais elementos:
    - Seja `meio` o índice do elemento do meio da lista
    - Se `x` < `lst[meio]`:
      - Então só pode estar em `lst[:meio]`
    - Senão, só pode estar em `lst[meio:]`

---
# Busca binária: 1a versão
```python
def bb(lista:list, x)-> bool:
    if len(lista) == 0: return False
    if len(lista) == 1: return x == lista[0]
    meio = len(lista)//2
    if x < lista[meio]: return bb(lista[:meio],x)
    return bb(lista[meio:],x)
```
::: row reveal
Não é muito legal fazer fatiamento de listas!
:::
---
# Busca binária: 2a versão
```python
def busca_binaria (lista : list, x)-> bool:
    def busca (i,j): # Está em lista[i:j]?
        if j-i == 0: return False
        if j-i == 1: return x == lista[i]
        meio = (i+j)//2
        if x < lista[meio]: return busca(i,meio)
        return busca(meio,j)
    return busca(0,len(lista))
```
---
# Busca binária: 3a versão
``` python
def bb_iterativa (lista: list, x) -> bool:
    i,j = 0, len(lista)
    while j-i > 1:
        meio = (i+j)//2
        if x < lista[meio]: j = meio
        else: i = meio
    if j-i == 0: return False
    return x == lista[i]
```
---
# Padrões recursivos geométricos
:::col ratio=60%
O que faz o seguinte código?
```python
def setup():
    tam = min(windowWidth, windowHeight) * 0.9
    createCanvas(tam, tam)
    recursivo (0, 0, tam, 5)

def recursivo (x,y,tam,n):
    if n == 0: 
        rect (x,y,tam)
    else:
        tam /= 2
        recursivo(x,y,tam,n-1)
        recursivo(x,y+tam,tam,n-1)
        recursivo(x+tam,y,tam,n-1)
```
:::
::: reveal col ratio=40% 
::image src="sierpinski.png"
:::
---
# Padrões recursivos geométricos
:::col ratio=60%
E este?
```python
def setup():
    tam = min(windowWidth, windowHeight) * 0.9
    createCanvas(tam, tam)
    recursivo (0, 0, tam, 5)

def recursivo (x,y,tam,n):
    if n == 0: 
        rect (x,y,tam)
    else:
        tam /= 2
        recursivo(x+tam,y+tam,tam,n-1)
        recursivo(x,y+tam,tam,n-1)
        recursivo(x+tam,y,tam,n-1)
```
:::
::: col reveal ratio=40%
::image src="sierpinski2.png"
:::
---
# Estruturas de dados recursivas

Uma estrutura de dados é _recursiva_ se ela é definida em termos de si mesma.

## Por exemplo: lista

(Não confundir com a lista do Python!)

Uma lista é uma estrutura de dados recursiva definida como:

1. Uma lista vazia
2. Um elemento seguido de uma lista

---
# Exemplo: Árvore binária de busca (ABB)
:::col
Uma árvore binária de busca (ABB) é uma estrutura de dados recursiva definida como:

1. Uma árvore vazia
2. Um nó interno com um valor $x$ e duas ABBs à esquerda e à direita, tais que
    - Todos os valores na árvore esquerda são menores que $x$
    - Todos os valores na árvore direita são maiores que $x$
:::
::: col
::image src="abb.svg" width="100%"
:::

---
# Uma ABB com listas

:::col 
1. ABB vazia: `[]`
2. ABB não vazia: `[x, esq, dir]`

Onde `esq` e `dir` são ABBs.
::: 
::: col 
```python
abb = [
    6,  
    [   
        3, 
        [   
            1, 
            [],            
            [2, [], []]    
        ],
        [   
            5, 
            [4, [], []],   
            []             
        ]
    ],
    [   
        8,
        [7, [], []],        
        [9, [], []]         
    ]
]
```
:::
---
# Busca em uma ABB

Segue diretamente da definição:

```python
def busca (abb, x):
    if len(abb) == 0: return False
    if abb[0] == x: return True
    if x < abb[0]: return busca(abb[1], x)
    return busca(abb[2], x)
```
---
# Inserção em uma ABB

1. Se a ABB é vazia, insere o valor
2. Se o valor é menor que a raiz, insere na subárvore esquerda
3. Senão, insere na subárvore direita

## Estratégias para implementar:

1. Criar uma cópia da ABB com a novo valor no lugar certo
2. Modificar a ABB original
---
# Implementação com cópia

Nesse caso, podemos até usar tuplas ao invés de listas!

```python
def insere (abb, x):
    if len(abb) == 0: return (x, (), ())
    if x < abb[0]: return (abb[0], insere(abb[1], x), abb[2])
    return (abb[0], abb[1], insere(abb[2], x))
```
---
# Implementação modificando a ABB original

Segue diretamente da definição:
```python
def insere (abb, x):
    if len(abb) == 0: abb[:]=[x, [], []]
    if x < abb[0]: insere(abb[1], x)
    else: insere(abb[2], x)
```
--- 
# Remoção em uma ABB

Um pouco mais difícil!

Precisamos considerar o nó onde está o valor a ser removido.

1. O nó é folha (não tem filhos):
    - Basta removê-lo
2. O nó tem um filho:
    - Basta removê-lo e coloca-lo no lugar
3. O nó tem dois filhos:
    - Encontrar um _valor substituto_:
       - O menor valor da subárvore direita
       - (ou o maior valor da subárvore esquerda)
    - Trocar o valor do nó por esse valor substituto
    - Remover o valor substituto da subárvore

 ---