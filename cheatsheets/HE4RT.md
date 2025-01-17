# HE4RT

```php
<?= "Hello, friend." ?>
```

- [php.net](https://www.php.net/docs.php)
- [escovar bits](https://github.com/danielhe4rt/php4noobs/blob/master/3-Basico/06-Operadores-bitwise.md)

## Ambiente de Desenvolvimento

- Cmder | Terminal Linux com GIT para Windows
- Notepad++, Visual Studio, Neovim | Editores de Texto
- PHP | Instalar e Instanciar enquanto Variável de Ambiente
- [Linux] `sudo apt install php php-mysql php-zip php-curl`
- `php -S localhost:8000` | Servidor e Banco de Dados
- Xdebug | Depuração e Análise `sudo apt install tree`

## Usual

```php
echo "Função de Saída"; // Comentário.

var_dump($var, function()); // Depuração.

/* Tipos de Dados */

$boolean = true; // fAlSe (são valores case-insensitives).

$int = 0x1A; // hexadecimal (equivalente a 26 decimal).

$float = 1.2e3; // notação científica (equivalente a 1200).

$string = "1 caractere é o mesmo que 1 byte na memória".

$array = ["mapa" => "ordenado"]; // Chaves não são obrigatórias.

/*
* Funções automatizam blocos de código
* @param $name string
* @return string
*/

function hello(string $name)
{
	return "Hello, " . $name . ".";
}

$name = "Lucas";
echo hello($name); // Hello, Lucas.

// Concatenação
//$codar = "programar.";
//$euQuero = 'Eu quero ' . $codar;
$euQuero = 'Eu quero';
$euQuero .= $codar;
echo $euQuero; // Eu quero programar.

// backticks / backquotes `` 
echo `ls`; // executam o conteúdo como um comando shell
// Tal qual shell_exec(), exec(), shell_exec() e system()

/* Estruturas */

if (first condition) {
    // condição verdadeira
} else if(second condition) {
    // condição verdadeira
} else {
    // condição falsa
}

switch (cond) {
    case val1:
        // faça algo
        break;
    case val2:
        // faça algo
        break;
    defaut:
        // faça algo quando nenhuma das opções for selecionada
        break;
}

$idade = 21;
$result = match (true) {
    $idade >= 65 => 'Idoso',
    $idade >= 25 => 'Adulto',
    $idade >= 18 => 'Jovem adulto',
    default => 'Criança',
};

$descricaoPorCodigo = array(
    1 => 'Este usuário já existe.',
    2 => 'Senha incorreta.',
    3 => 'Este usuário está bloqueado.',
);

// Operador ternário - Retorna 'Alguma coisa deu errado', pois a chave 5 não existe
return isset($descricaoPorCodigo[5]) ? $descricaoPorCodigo[5] : 'Alguma coisa deu errado.';

// Simplificando com Coalescência nula
return $descricaoPorCodigo[5] ?? 'Alguma coisa deu errado.';
```

## scripts via parâmetros

`script.php`

```php
<?php

// Verifica se há argumentos além do nome do arquivo
if ($argc > 1) {
    echo "Número de argumentos passados: " . ($argc - 1) . PHP_EOL;
    echo "Lista de argumentos:" . PHP_EOL;

    // Itera sobre os argumentos (ignorando o primeiro, que é o nome do script)
    for ($i = 1; $i < $argc; $i++) {
        echo "Argumento {$i}: {$argv[$i]}";
    }
} else {
    echo "Nenhum argumento foi passado!";
}
```

```bash
php script.php teste exemplo 123
```