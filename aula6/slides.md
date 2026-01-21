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
 
