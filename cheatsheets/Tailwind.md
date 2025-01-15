## Configuração

**Intalação do Tailwind CSS**
```bash
npm install tailwindcss
```

**Gera o arquivo de configuração padrão** `tailwind.config.js`
```bash
npx tailwindcss init
```

O cérebro do projeto, onde definimos quais arquivos o Tailwind deve escanear para procurar classes (`content`) e configuramos estilos padrões, plugins ou extensões para funcionalidades adicionais.

**Certifique-se do seu conteúdo**
```javascript
module.exports = {
  content: ["./*.html"], // Localize os arquivos HTML
  theme: {
    extend: {}, // Personalizações adicionais
  },
  plugins: [], // Adicione plugins se necessário
};
```

**Crie ou edite o seu**  `input.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
    body {
        @apply antialiased font-sans;
    }
}

@layer utilities {
    .font-playfair {
        font-family: 'Playfair Display', serif;
    }
}
```

`input.css` contém as instruções para o Tailwind CSS sobre como ele deve processar e gerar o CSS final. Ele usa as diretivas do Tailwind como @tailwind para importar as partes do framework (base, componentes e utilitários).

**Adicione os scripts no** `package.json`
```json
{
  "scripts": {
    "build": "tailwindcss -i ./input.css -o ./output.css",
    "watch": "tailwindcss -i ./input.css -o ./output.css --watch"
  },
  "devDependencies": {
    "tailwindcss": "^3.3.0"
  }
}
```

`package.json` gerencia dependências e scripts do projeto. Ele indica quais pacotes estão sendo usados e fornece scripts para automação, como compilação de CSS, execução de servidores, etc. Aqui o Node.js e o npm (ou yarn) leem o package.json para saber quais dependências instalar e quais scripts devem ser executados. O script de compilação (npm run build) é chamado do terminal ou integrado ao processo de desenvolvimento.

`package-lock.json` registra as versões exatas das dependências instaladas no seu projeto. Isso garante que qualquer pessoa que instale as dependências do seu projeto via npm ou yarn tenha exatamente as mesmas versões de pacotes.

**Referencie no HTML**
```html
<link href="./output.css" rel="stylesheet">
```

**Compile**
```bash
npm run build
```

**ou desenvolva em tempo real**
```bash
npm run watch
```

**ao clonar**
```bash
npm install
npm run build
```