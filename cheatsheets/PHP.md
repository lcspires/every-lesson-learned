# PHP

**PHPMailer** via [Packagist](https://packagist.org/)

```json
"require": {
	"phpmailer/phpmailer": "^6.9.2"
}
```

`composer install` `composer update`

## Carregamento Automático

`Address.php` in `/source/Loading/`

```php
namespace Source\Loading;

class Address { ... }
```

### Autoloader via SPL (Standard PHP Library)

`autoload.php` in `/source/`

```php
<?php

spl_autoload_register(function($class){
	$prefix = "Source\\";
	$baseDir = __DIR__ . "/";
	
	$len = strlen($prefix);
	
	if (strncmp($prefix, $class, $len) !==  0){
		return;
	}
	
	$relativeClass = substr($class, $len);
	
	$file = $baseDir . str_replace("\\", "/", $relativeClass) . ".php";
	
	if (file_exists($file)){
		require $file;
	}	
});
```

`index.php`

```php
require __DIR__ . "/source/autoload.php";

$address = new \Source\Loading\Address();
```

### Autoloader via Composer

`composer.json`

```json
{
	"name": "lcspires/lispector",
	"description": "Inventory Application",
	"minimum-stability": "stable",
	"authors": [
		{
			"name": "Lucas Pires",
			"email": "ferreira.l@ufba.br",
			"homepage": "https://github.com/lcspires",
			"role": "Developer"
		}
	],
	"config": {
		"vendor-lib": "vendor"
	},
	"autoload": {
		"psr-4": {
			"Source\\": "source/"
		}
	}
}
```

```bash
composer dump-autoload
```

`index.php`

```php
<?php

require __DIR__ . "/vendor/autoload.php";

use Source\Loading\User;

$user = new User();
```

## PHPMailer