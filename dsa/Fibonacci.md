# Fibonacci

```python
print("Fibonacci de 10:", fibonacci(10))  # 55
```

## Uma implementação recursiva ingênua

### Quando a ineficiência surge da repetição de cálculos desnecessários

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
````

Essa abordagem tem complexidade exponencial **(O^N)** porque cada chamada recursiva faz duas chamadas adicionais, criando uma árvore de chamadas que cresce exponencialmente. Se a implementação piorar, como adicionar mais recursões aninhadas ou recalcular subproblemas mais de uma vez por camada, a complexidade pode atingir algo tão absurdo quanto **O(N!)**.

## Abordagem com Memoization (compatível com recursão)

### Armazenando os resultados dos subproblemas com Programação Dinâmica - Top-Down

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

- Complexidade Temporal: O(N), pois cada subproblema é resolvido uma única vez.
- Complexidade Espacial: O(N), para armazenar os resultados no dicionário `memo`.

## Abordagem Iterativa (Bottom-Up)

### #Simplicidade

```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

- Complexidade Temporal: O(N), pois percorre uma única vez de 1 a *n*.
- Complexidade Espacial: O(1), já que só usa variáveis escalares (a e b).

## Usando Álgebra Linear para Performance Extrema

### Matriz de Exponenciação (Para Fibonacci em Tempo Logarítmico)

```python
def fibonacci_matrix(n):
    def multiply_matrices(m1, m2):
        return [
            [m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
            [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]],
        ]

    def matrix_exponentiation(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_exponentiation(matrix, power // 2)
            return multiply_matrices(half, half)
        else:
            return multiply_matrices(matrix, matrix_exponentiation(matrix, power - 1))

    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_exponentiation(base_matrix, n)
    return result_matrix[0][0]
```

- Complexidade Temporal: O(log N), graças à exponenciação rápida.
- Complexidade Espacial: O(log N), devido à pilha de recursão.
