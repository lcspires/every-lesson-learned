# Apache Kafka, um nó da rede

Originalmente desenvolvido pelo LinkedIn (2010) enquanto uma solução escalável, resiliente e de baixa latência para atender às necessidades crescentes de capturar, processar e distribuir grandes volumes de dados em tempo real. Posteriormente foi doado para a Apache Software Foundation (2011) e hoje é uma das plataformas de streaming de eventos mais utilizadas no mundo para **integrar serviços**. Estamos sob o signo da Arquitetura Orientada a Eventos.

Palavras-chave: microsserviços, sistemas distribuídos, sistemas escaláveis, sistemas complexos, java, pub/sub, jaeger.

## microsserviços

- Cada serviço vai ter a sua própria base de dados, a comunicação se dá apena via APIs ou por Eventos.
- Event Driven Architecture parte do pressuposto de que um dado  serviço não tem a base de dados de outro, seu endpoint ou seu esquema. Trata-se em resumo de saber apenas quais tópicos escutar e quais tópicos publicar.

## Quais problemas o Kafka Resolve?

- Transporte escalável: permite a transmissão eficiente de dados entre sistemas distribuídos com baixa latência.
- Desacoplamento de sistemas: atua como uma camada intermediária entre produtores (quem gera dados) e consumidores (quem processa ou armazena dados), facilitando a integração.
- Processamento de eventos: permite análises em tempo real ao consumir fluxos contínuos de dados.
- Persistência de dados: armazena dados de forma durável, garantindo que eventos não sejam perdidos.
- Resiliência: falhas em componentes individuais não interrompem o sistema.

## Como é definida a Arquitetura de um broker Kafka?

**Broker** é o núcleo do Kafka, responsável por armazenar e distribuir mensagens. Cada broker é uma instância única de um servidor Kafka, este é identificado por um ID único e pode armazenar várias partições de tópicos.

**Cluster** são múltiplos brokers trabalhando em conjunto como uma única entidade lógica.

**Producers** são sistemas que publicam dados em tópicos, como um item adicionado ao carrinho de compras.

**Consumers** são aplicações que consomem dados dos tópicos, como um gerador de notas fiscais, por exemplo.

**Tópico** é uma categoria ou o nome do Feed/Stream.

**Chave** 

## Como desenhar uma arquitetura usando Kafka?

Primeiro **defina o caso de uso**, ou seja, determine se o Kafka será usado para streaming de dados, integração de sistemas ou pipelines ETL. Em seguida identifique produtores e consumodores.

O segundo passo é **planejar a estrutura de tópicos** com base no tipo de eventos ou dados. Por conseguinte, divida tópicos em partições com base na carga esperada e no nível de paralelismo necessário.

O passo três implica **configurar a infraestrutura** a partir do dimensionamento dos brokers com base na capacidade de armazenamento e taxa de transferência. Não esqueça da replicação para garantir resiliência.

Por fim, use ferramentas como Kafka Streams ou ksqlDB para **processar os dados** em tempo real.

Os sistemas de **monitoramento** mais usuais são Prometheus e Grafana.

## Usando Kafka no Java SE

## Usando Kafka no Quarkus

## Bub/Sub Alternatives

Amazon Kinesis, RabbitMQ, MuleSoft Anypoint Plataform, Azure Event Hubs, PieSync, TIBCO Spotfire, IBM MQ, Google Cloud Pub/Sub