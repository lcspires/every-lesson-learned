# Preâmbulo

- 1911: IBM.
- 1940: Assembly.
- 1957: FORTRAN (IBM).
- 1972: C, da dificuldade de desenvolver o UNIX (desde 1969) com Assembly.

Por conta da Guerra Fria, em 1969, a ARPANET foi criada enquanto grupo de pesquisa da ARPA, financiado pelo Departamento de Defesa dos Estados Unidos, visando o desenvolvimento de redes de comunicação descentralizadas.

Nessa época a IBM já aperfeiçoava cada vez mais suas tecnologias, pois era necessário maximizar a utilização de recursos limitados. Nesses idos ela criou o conceito de "máquinas virtuais" cujo objetivo era dividir um grande computador central (mainframe) em vários, permitindo que diferentes usuários e aplicações utilizassem o mesmo hardware ao mesmo tempo, sem interferir uns nos outros.

- 1972: Acordo SALT I (Strategic Arms Limitation Treaty), [Abertura].
- 1973: UNIX, um sistema robusto, porém caro e fechado.
- 1976: Apple I, Computador Pessoal projetado por Wozniak e Jobs.
- 1978: BBS, computadores interligados via linha telefônica.
- 1981: MS-DOS, o primeiro grande movimento de Bill Gates, pois o Sistema Operacional foi adotado pela IBM, uma das maiores e mais influentes empresas de tecnologia do mundo naquele momento e até então.

No dia primeiro de janeiro de 1983, a ARPANET oficialmente mudou do NCP (Network Control Protocol) para o TCP/IP (Transmission Control Protocol/Internet Protocol), que também foi adotado universalmente como padrão oficial para comunicação entre redes, ou seja, a base para interconectar redes distintas, criando o que viria a ser a Internet global, um marco crucial no processo de descentralização da rede.

Com o arrefecimento da Guerra Fria, a rede restrita a fins militares gradualmente se expandiu para universidades e outros centros de pesquisa, uma mudança fundamental para a transição para o que seria a Internet pública.

- 1983: GNU (GNU's Not Unix), buscava ser um sistema operacional multitarefa robusto como o UNIX, porém livre.

- 1984: Macintosh, o grande salto da Apple no mercado de tecnologia, a Interface Gráfica de Usuário (GUI).
- 1985: Windows 1.0, a Microsoft lança uma interface gráfica para MS-DOS, afim de não ficar para trás, visto o sucesso crescente do Macintosh.

Em 1990, Tim Berners-Lee (CERN) desenvolve o HTTP como parte do projeto da World Wide Web (WWW), uma camada de usabilidade mais simples e intuitiva para o público em geral sobre a infraestrutura física da Internet desenvolvida para fins militares.

Neste mesmo ano a administração da Internet foi transferida para provedores comerciais. Os principais players desse mercado são Operadoras de Telecomunicações (Claro, Vivo, etc.), Provedores de Serviços de Internet (ISPs), Empresas de Infraestrutura Técnica como Cisco ou Huawei, Provedores de Serviços de Nuvem e Organizações de Governança que gerenciam, por exemplo, a alocação de domínios globalmente (ICANN) ou a qualidade do serviço local (Anatel).

Na mesma esteira de desenvolvimento do protocolo HTTP veio também os endereços URLs e a linguagem HTML, formando o sistema de comunicação hipermídia contemporâneo, uma rede global de documentos interligados.

Em 1991 Linus Torvalds, então estudante de Ciência da Computação, anunciou publicamente o desenvolvimento de um kernel no comp.os.minix, um fórum online, dizendo: "Estou fazendo um sistema operacional (gratuito) apenas como hobby, não será grande e profissional como o GNU". É o nascimento do Linux, a espinha dorsal de servidores web, a base do sistema operacional mais popular para smartphones do mundo (android), a revolução do software livre e do código aberto.

Em 1993 surge o Mosaic, o primeiro navegador a ser amplamente utilizado pelo grande público, graças à sua interface gráfica amigável.

- 1995: Java, uma maneira de desenvolver software portável, seguro e escalável.

Windows 95, o maior Sistema Operacional de todos os tempos.

PHP, os sites estáticos (feitos apenas em HTML) não eram mais suficientes.

JavaScript, adicionando interatividade e dinamismo nas páginas web.

Apache Web Server, um dos pilares da infraestrutura da internet.

MySQL, uma alternativa barata aos sistemas de bancos de dados comerciais.

O Backbone brasileiro (RNP) entra em atividade.

- 1996: CSS.

- 1998: Google, algoritmos avançados de indexação e ranqueamento (PageRank).

- 1999: Wi-Fi, o padrão 802.11b.

Napster e o conceito de compartilhamento descentralizado, peer-to-peer (P2P).

SourceForge, uma das primeiras e mais influentes plataformas de hospedagem de projetos de software de código aberto.

Microsoft lança os MSN Messenger.

Boom de empresas como Amazon e eBay.

- 2002: O protocolo BitTorrent, uma base potente para o compartilhamento de arquivos.

- 2003: The Pirate Bay, o indexador de "metadados" (arquivos .torrent) mais famoso do mundo.

- 2004: Orkut (proof of concept) e Facebook (só chegou no Brasil em 2010).

- 2005: Git, Linus lança um dos pilares do desenvolvimento de software moderno.

- 2006: Amazon Web Services (AWS), infraestrutura dinâmica, elástica e altamente escalável.

- 2008: Blockchain, tecnologia de registro descentralizado e imutável.

- 2010: Smartphones como o centro da computação.

Milhares de requisições por segundo.

- 2011: Apache Kafka e a falência dos modelos de Arquitetura de Software antigos.

- 2013: Containers, uma forma mais leve de virtualização.

- 2014: .NET (enquanto um projeto de código aberto), Microsoft entra no movimento open source e na cultura de colaboração, adotando o Git enquanto gerenciamento de código e adquirindo o GitHub (2018), tal configuração passou a ser mais eficiente, sustentável e até mesmo lucrativa para a empresa.

- 2022: ChatGPT, a capacidade de analisar grandes volumes de dados.

## Old and New

**Old**

```html
	<h3>significação semântica</h3>
	<p><strong>(ênfase)</strong></p>
	<p><em>(ênfase)</em></p>
	<p>2<sup>3</sup></p>
	<p>2<sub>3</sub></p>
	
	<!-- melhor evitar -->
	<h3 align="center">estilização visual</h3>
	<p>(clean)</p>
	<p><b>(negrito)</b></p>
	<p><i>(itálico)</i></p>
	<p><u>(sublinhado)</u></p>
	<p><s>(riscado)</s></p>
```

**New**

```html
	<h3 class="centrado">estilização visual</h3>
	<p class="negrito">(negrito)</p>
	<p class="italico">(itálico)</p>
	<p class="sublinhado">(sublinhado)</p>
	<p class="riscado">(riscado)</p>
```

```css
.centrado {
  text-align: center;
}
.negrito {
  font-weight: bold;
}
.italico {
  font-style: italic;
}
.sublinhado {
  text-decoration: underline;
}
.riscado {
  text-decoration: line-through;
}
```