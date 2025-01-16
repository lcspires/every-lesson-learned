# Inteligência Artificial

Modelos maquínicos que não seguem regras explicitamente programadas, mas aprendem a tomar decisões ou reconhecer padrões a partir de dados. Ou seja, em vez de programar manualmente todas as regras para identificar um objeto em uma imagem, por exemplo, treinamos um modelo fornecendo milhares de exemplos (dados de entrada) e o modelo aprende uma lógica subjacente para realizar a tarefa baseando-se em correlações estatísticas e estruturas ocultas nos dados que não são explicitamente descritas, mas sim descobertas pelo próprio modelo durante o treinamento. Tais modelos tornam os sistemas eficazes em tarefas onde as regras explícitas são difíceis ou impossíveis de descrever, como reconhecimento de fala, processamento de linguagem natural e análise de padrões em grandes volumes de dados.

Os modelos necessitam de dados rotulados para aprender e geralmente têm dificuldade em generalizar além do domínio dos dados de treinamento. Isso quer dizer que, apesar da complexidade crescente dos sistemas de inteligência artificial, ainda estamos no domínio em que o funcionamento desses sistemas pode ser descrito e entendido matematicamente e computacionalmente, pois as bases teóricas que os guiam são claras e mensuráveis. Técnicas de interpretabilidade como SHAP, LIME ou Grad-CAM permitem insights sobre os fatores que levaram a uma decisão e revelam que modelos populares, como LLMs, carecem de entendimento real do contexto, baseando-se apenas em correlações nos dados.

- Machine Learning (ML) `regressão linear` `regressão logística` `árvore de decisão`
- Deep Learning `aprendizado profundo` `redes convolucionais` `redes recorrentes`
- Natural Language Processing (NLP) `processamento de linguagem natural`
- Computer Vision `visão computacional` `aproximações por padrões médios`
- Robotics `robótica` `aprendizado por reforço` `planejamento de movimentos` `SLAM`
- Data Analytics `análise de dados` `detecção de anomalias em sistemas complexos`

**Popularização**

- Scikit-learn (2007)
- Keras (2015)
- TensorFlow (2015)
- spaCy (2015)
- PyTorch (2016)
- Transformers (2018)

**Gradiente Descendente (Gradient Descent)** `método de minimização de erros (ou otimização) mais usual`

## aplicações ao longo do tempo

IA Simbólica (regras explícitas e lógicas formais): Sistemas Especialistas, como um Sistema de Diagnóstico Médico.

Machine Learning: Corretor Ortográfico, Sistema de Recomendação.

- Em 2012, Alex Krizhevsky teve a brilhante ideia de usar a própria GPU para rodar uma rede neural convolucional afim de classificar imagens para uma competição de modelos de aprendizado de máquina. Ele superou o desempenho dos modelos concorrentes feitos com CPUs de maneira impressionante, afinal de contas, placas de vídeo são utilizadas para multiplicar matrizes, como não pensaram nisso antes? O trabalho de Alex representou, portanto, um ponto de inflexão crucial no desenvolvimento da IA, especialmente no campo do deep learning, antes desse momento, redes neurais eram caras e pesadas em termos de custos computacionais.

Transfer Learning

Hugging Face

Modelos de Linguagem de Grande Escala: LLMs, GPT-3, LLaMA, etc.

DeepMind: biologia estrutural e a previsão de estruturas de proteínas, um processo que era extremamente complexo e demorado que exigia conhecimento especializado e muita experimentação.

Também tem tido um avançado promissor no campo da engenharia de processos industriais, especialmente quando se trata de otimização de processos de produção, design de novos materiais, misturas de substâncias e desenvolvimento de novos produtos.

Devin: agentes.

## Projetos

C, Rust, Python

Escreva na mão uma Regressão Linear, depois uma Regressão Logística, depois uma Árvore, depois façar algum modelo de clusterização como o K-Medoids, para entender matemáticamente como funciona essas coisas simples, então procure por modelos maiores.

GSM Symbolic: understanding the limitations of mathematical reasoning in large language models.

### Identificação de Padrões Sonoros em Sinais de Rádio e TV

Este sistema foi desenvolvido para uma empresa especializada em clipping de mídia, responsável por monitorar, registrar e gerar relatórios sobre o conteúdo transmitido, realizar tal operação utilizando técnicas de processamento de sinais digitais (DSP) e aprendizado de máquina.

**Funcionamento do sistema:**

1. Cadastro do objetos de interesse, como jingles, comerciais, ou até mesmo padrões sonoros específicos.
2. Processamento de áudio e extração de características.
3. Análise contínua dos sinais de áudio transmitidos.
4. Ao detectar o padrão cadastrado, registrar o evento e sua localização na linha do tempo.
5. Gerar um relatório detalhado indicando todas as ocorrências do objeto de mídia nos sinais monitorados.