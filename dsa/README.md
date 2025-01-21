# Estruturas de Dados e Algoritmos
**usual prompt**
```plaintext
What is the BigO of the code below:
```
**visual abstractions**

[W3Schools](https://www.w3schools.com/dsa/)
[cpython](https://github.com/python/cpython/blob/main/Modules/_collectionsmodule.c)

## Big O

Essa notação não é uma medida de performance. Trata-se uma forma de denotar desempenho do algoritmo. Pois, ele vai nos mostrar o quanto este algoritmo escala de acordo com o tamanho de dado input. Nesse contexto, O(n), por exemplo, não é, necessariamente, mais rápido, que O(n²). Para afirmar tal proposição se faz necessário uma análise mais profunda denominada análise assintótica. Portanto, Big O notation fala sobre escalabilidade e servirá para medir a Complexidade Temporal (runtime) e a Complexidade Espacial (allocation) de um dado algoritmo.

Ps.: Trabalhe sempre sob o signo do pessimismo, ou seja, tendo em perspectiva o pior caso possível.

### Principais Classificações de Big O
#### Da que melhor escala para a pior:

**O(1) - Escala Constante**

Tempo Constante: Independe do tamanho do input. Ex.: Encontrar o primeiro elemento de um array qualquer.

Memória Constante: Quando, por exemplo, precisamos encontrar os quinze maiores elementos dentro de um array, precisaremos alocar nesse caso quinze espaços novos na memória para guardá-los. E aí, tanto faz também se é um array com vinte ou com um milhão de elementos, se não mudar o input, digo a quantidade de dados buscados e armazenados ainda estaremos falando de O(1).

**O(LOG N) - Escala Logarítmica**

`binary search` escala em log de n, pois conforme seu input aumenta rapidamente o tempo de execução aumenta em menor proporção. Veja, se Log2(10) é 3.321928, Log2(20) é 4.321928. Não chegando nem perto de dobrar.

Formalizando: O input aumenta exponencialmente enquanto o tempo de execução aumenta linearmente.

**O(N)**

Complexidade Temporal: Se precisar percorrer todo um array, a quantidade total de elementos implicará proporcionalmente no tempo de execução do algoritmo. Em termos mais técnicos, ele escala exatamente na mesma medida em que o input aumenta.

Complexidade Espacial: Se precisar calcular o dobro dos elementos de um dado array e tiver de armazenar o resultado em um outro array, o espaço na memória alocado será proporcional ao tamanho do array inicial.

**O(N LOG N)**

Todos os algoritmos de `divide and conquer` e de `sorting` com exeção de `bubble sort` que é O(N²).

Complexidade Espacial: Raro e/ou mal feito.

Complexidade Temporal: Avaliar os elementos de um dado array várias vezes, como quando precisamos repetidamente percorrer, dividir, ordenar e juntar todos os elementos recursivamente. Matemáticamente seria algo como O(N) vs. O(LOG N).

**O(N²) - um FOR dentro de outro FOR**

Selection, Inserction, Bubble Sort ...

**Existe, mas não usual: O(2^N), O(raiz de N), O(N!)**

## Arrays

Estruturas de dados de tamanhos fixos que armazenam elementos em posições contíguas de memória.

- O(1) para acessar um elemento pelo índice.
- O(n) para buscar um elemento no pior caso possível, pois seria necessário verificar todos.

## Linked List

Estrutura de dados linear composta por uma sequência de nós, onde cada nó contém valor e um ponteiro.

- A lista pode crescer dinamicamente sem necessidade de realocação de memória.
- Uso de memória adicional para armazenar ponteiros.

### Queue

- FIFO (First in, First out);
- Elementos apontam uns para os outros num único sentido.
- Head (referência para removermos elementos) and Tail (referência para adicionarmos elementos);

### Dequeue

- Elementos apontam uns para os outros em ambos os sentidos.
- Head (referência para adicionarmos e removermos elementos) and Tail (referência para adicionarmos e removermos elementos);

## Hashmap (Dictionary)

Estrutura de dados usada para armazenar pares de chave-valor, oferecendo um acesso extremamente eficiente às informações. Sua principal vantagem é a capacidade de realizar operações em tempo constante O(1).

- **chave** é o identificador único usado para armazenar ou buscar um valor.
- **valor** é a informação associada à chave.
- **função de hash** é quem transforma a chave em um número. O mesmo input deve gerar o mesmo output sempre.
- **Load Fator** é a diferença de tamanho entre a quantidade de dados a quantidade de dados que a gente possui e a nossa estrutura de dados.
- **Collisions** 






