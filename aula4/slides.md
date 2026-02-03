::: center
# Introdução à Programação com Python
## Aula 04: Sequências
:::
---
# Dados no atacado
Até agora, trabalhamos com variáveis que contêm dados simples como números inteiros e reais, strings e booleanos. 

Para trabalhar com grandes quantidades de dados, precisamos de estruturas de dados mais complexas.

O primeiro conceito que nos permite trabalhar com grandes quantidades de dados é o conceito de **sequência**.

Python tem várias estruturas de dados que funcionam como sequências, como _tuplas_ e _listas_.
---
# Tuplas

Uma variável do tipo _tupla_ pode conter vários dados. Ela é criada listando os dados separados por vírgula. Ex:

```python
xpto = "A", 2, 6, "B"
```

Isto significa que a variável `xpto` contém uma sequência de 4 dados: a string "A", o número 2, o número 6 e a string "B". 

Podemos acessar cada um desses dados usando a notação `nome_variavel[indice]`, onde `indice` é um número inteiro que indica a posição do dado na sequência.

```python
print (xpto[2]) # Imprime 6
```
---
# Atribuição múltipla

Sequências permitem atribuir valores a várias variáveis em uma única linha.

```python
x, y, z = 1, 2, 3
```
... é (quase) o mesmo que 

```python
x = 1
y = 2
z = 3
```

--- 
# Por que quase?
Porque  a atribuição múltipla é _simultânea_ e não consecutiva. Considere:
```python
x, y = 1, 2
x, y = y, x
print (x, y) # Imprime 2 1
```
e 
```python
x = 1
y = 2
x = y
y = x
print (x, y) # Imprime 2 2  
```

---
# A função `len`

`len (seq)` retorna o número de elementos na sequência `seq`.

```python
xpto = "A", 2, 6, "B"
print (len(xpto)) # Imprime 4
```

Às vezes precisamos usar parênteses para distinguir uma expressão do tipo tupla de uma sequência de valores.

```python
print (len("A", 2, 6)) # TypeError: len() takes 
                       # exactly one argument (3 given)
print (len(("A", 2, 6))) # Imprime 3
print (len(("A",)) # Imprime 1 (a vírgula é necessária!)
```
---
# Sequências e o comando `for`

Podemos usar `len` para gerar os índices de uma sequência:

```python
xpto = "A", 2, 6, "B"
for i in range(len(xpto)):
    print (xpto[i])
```

Podemos examinar diretamente os elementos de uma sequência usando o comando `for`. 

```python
for x in "A", 2, 6, "B":
    print (x)
```
---
# O que é `range()`?

Na verdade, `range()` é simplesmente uma função que gera uma _sequência_ de  inteiros!

Como tuplas, um 'range()' pode ser indexado e é possível usar o comando `len` para obter o número de elementos.

```python
print (range(5)) # Imprime range(0, 5)
print (len(range(5))) # Imprime 5   
print (range(5)[2]) # Imprime 2
```
--- 
# Strings

Uma string é uma _sequência_ de caracteres.

Como tuplas, uma string pode ser indexada e é possível usar o comando `len` para obter o número de elementos.

```python
abc = "abcdefg"
print (abc[2]) # Imprime c
print (len(abc)) # Imprime 7
for c in abc:
    print (c)
```
---
# Conversão de tipos

O nome do tipo também pode ser usado como uma função para converter um valor para esse tipo.

```python
x = "123"
y = int(x) # Converte a string "123" para o número 123
w = float(x) # Converte a string "123" para o número 123.0
z = str(y) # Converte o número 123 para a string "123"
abc = tuple(x) # Converte a string "123" para a tupla ("1", "2", "3")
xpto = tuple(range(5)) # Converte o range(5) para a tupla (0, 1, 2, 3, 4)
```
---
# Fatias

Subsequências de uma sequência são chamadas de _fatias_.

Para extrair uma fatia de uma sequência, usamos a notação `seq[inicio:fim]`.

A fatia começa no elemento de índice `inicio`. Se omitido, é assumido 0.

A fatia termina no elemento de índice `fim-1`. Se omitido, é assumido o comprimento da sequência.

```python
abc = "abcdefg"
print (abc[2:5]) # Imprime cde
print (abc[2:]) # Imprime cdefg
print (abc[:5]) # Imprime abcde
print (abc[:]) # Imprime abcdefg
```
---
# Índices negativos

Um índice negativo pode ser usado para contar posições de trás para frente.

Por exemplo: 
- `"abcde"[-1]` é o mesmo que `"e"`
- `(0,1,2,3,4)[-2]` é o mesmo que `3`
- `(1,2,3,4,5)[-2:]` é o mesmo que `[4,5]`
- `"abcde"[-4:-2]` é o mesmo que `"bc"`

---
# Fatias com incremento

Fatias podem ter um terceiro argumento que indica o incremento. Se não indicado, é assumido 1.

Para incrementos negativos, a fatia é extraída de forma reversa.

```python
abc = "abcdefg"
print (abc[2:5:2]) # Imprime ce
print (abc[2:5:1]) # Imprime cde
print (abc[5:2:-1]) # Imprime edc
```

---
# Concatenação

Se quisermos juntar duas sequências, usamos o operador `+`.

```python
abc = "abc"
def = "def"
print (abc + def) # Imprime abcdef
```
---
# Repetição

Se quisermos repetir uma sequência, usamos o operador `*`.

```python
abc = "abc"
def = "def"
print (abc * 3) # Imprime abcabcabc
print (def * 2) # Imprime defdef
```
---
# Sequências imutáveis

Tuplas e strings são sequências imutáveis, ou seja, não podem ser modificadas após sua criação.

Se quisermos modificar uma sequência, devemos criar uma nova sequência.

```python
xpto = "abc", "def", "ghi"
com_tracos = () # tupla vazia
for s in xpto:
    r = "" # string vazia
    for c in s:
        r = r + c + "-"
    com_tracos = com_tracos + (r,) # adiciona r à tupla
print (com_tracos) # Imprime ('a-b-c-', 'd-e-f-', 'g-h-i-')
```
---
# Listas

São como tuplas, mas mutáveis! 

Um literal de lista é criado usando colchetes. 

```python
xpto = ["abc", "def", "ghi"]
xpto[1] = "jkl"
print (xpto) # Imprime ['abc', 'jkl', 'ghi']
```
--- 
# Atribuição a fatias

É possível alterar uma fatia de uma lista usando uma atribuição.

```python
xpto = ["abc", "def", "ghi"]
xpto[1:2] = ["jkl", "mno"]
print (xpto) # Imprime ['abc', 'jkl', 'mno', 'ghi']
```

O valor atribuído precisa ser uma sequência.

```python
xpto = ["abc", "def", "ghi"]
xpto[1:2] = 1, 2  # Ok!
xpto[1:2] = 1     # TypeError
```

--- 
# Inserção e remoção usando fatias

Se quisermos remover uma fatia de uma lista, podemos atribuir uma lista vazia.

```python
xpto = ["abc", "def", "ghi"]
xpto[1:2] = []
print (xpto) # Imprime ['abc', 'ghi']
```

Para inserir elementos em uma lista, podemos atribuir uma sequência a uma fatia vazia.

```python
xpto = ["abc", "def", "ghi"]
xpto[1:1] = ["jkl", "mno"]
print (xpto) # Imprime ['abc', 'jkl', 'mno', 'def', 'ghi']
```
---
# Inserção e remoção - funções

```python
def insere (lista:list, posicao:int, valor) -> None:
    """Insere valor em lista[posicao]"""
    lista[posicao:posicao]=[valor]

def remove (lista:list, posicao:int) -> any:
    """Remove de lista o elemento na posicao dada e o retorna"""
    x = lista[posicao]
    lista[posicao:posicao+1] = []
    return x
---
# Métodos de listas
Listas, como muitos outros _objetos_ em Python, possuem _métodos_. 

Um método é uma função que está associada a um objeto. 

Um método é chamado com a sintaxe `objeto.metodo(argumentos)`.

Por exemplo:
- `lista.insert(i,valor)` é o mesmo que `insere(lista, i, valor)`
- `lista.append(valor)` é o mesmo que `insere(lista, len(lista), valor)`
- `lista.pop(i)` é o mesmo que `remove(lista, i)`
   - Uma diferença: é possível não passar o argumento para `pop`
   - Se não for passado o argumento, remove o _último_ elemento
   - Existe um atalho para pop: `del lista[i]`
---
# Exemplos:

```python
lista = [1,2,3]
lista.insert(1,4)
print (lista) # Imprime [1, 4, 2, 3]
lista.append(99)
print (lista) # Imprime [1, 4, 2, 3, 99]
x = lista.pop(2)
print (lista) # Imprime [1, 4, 3, 99]
print (x) # Imprime 2
```

---
# Uma palavra sobre eficiência!

Usar métodos de listas é mais eficiente do que usar fatias!

Inserção e remoção de elementos no **fim** de uma lista é **muito** mais eficiente do que no início!

(Por quê?)

---
# Matrizes

Listas podem conter listas.

Uma lista de listas de números é uma _matriz_.

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (matriz[1][1]) # Imprime 5
```
---
# Vamos praticar!

Crie a função `transposta(matriz)` que retorna a transposta de uma matriz.

```python
print (transposta([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) 
# Imprime [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```
<button onclick="window.open('https://jupyterlite.github.io/demo/lab/index.html', '_blank')">Abrir JupyterLite</button>

---
# Você vai errar muito isto!
:::col
```python
a = [1, 2, 3]
b = a
b[2] = 4
print (a) # Imprime [1, 2, 4]
```

Explicação: 
- `b = a` diz que b e a se referem à mesma lista.
- **Não quer dizer** que b é uma _cópia_ de a.
:::
::: col reveal
Para fazer uma cópia, podemos usar fatias

```python
a = [1, 2, 3]
b = a[:]
b[2] = 4
print (a) # Imprime [1, 2, 3]
```
:::
---
# Exercícios:
1. Crie a função `primos(n)` que retorna uma lista com os todos os números primos até `n`,usando o [_crivo de Eratóstenes_](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes).
```python
print (primos(40)) 
# Imprime [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
```

2. Crie a função `fibonacci(n)` que retorna uma lista com os primeiros `n` números da sequência de Fibonacci.
```python
print (fibonacci(10)) 
# Imprime [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
---
# Exercícios
3. Crie a função `mult(a,b)` que retorna a multiplicação das matrizes   `a` e `b`.
```python
print (mult([[1, 2], [3, 4]], [[1, 2], [3, 4]])) 
# Imprime [[7, 10], [15, 22]]
```
Dicas: 
- Crie a função `coluna(m,i)` que retorna a coluna `i`de `m`
- Crie a função `produto(v1,v2)` que retorna o produto escalar de dois vetores
---
:::center
[-> Códigos desta aula](https://esperanc.github.io/jupyterlite/lab/index.html?fromURL=https://raw.githubusercontent.com/esperanc/Python-2026/refs/heads/main/aula4/sequencias.ipynb)
:::
---
::: center
# Até a próxima!
:::





