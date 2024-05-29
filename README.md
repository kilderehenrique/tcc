# Visão Comptacional aplicado a Dengue.

## Resumo da Solução
### Problema: 

Afim de auxiliar no combate ao mosquito Aedes Aegypti, esse projeto visa usar de visão computacional aplicada com inteligência artificial para detectar possíveis focos do mosquito e ajudar
em seu controle. 

### Solução

Esta solução foi aplicada utilizando uma série de ferramentas e bibliotecas quebradas por tópicos dos problemas abordados. 

Do Modelo: antes de tudo,o modelo foi construído e treinado usando a ferramenta teachable machine e assim exportado no formato de tensorflow-Keras
(keras_model.h5) o modelo foi dividido em classes salvas no arquivo "labels.txt" e cada classe contém uma série de imagens usadas como set de treino 
o modelo foi feito para prever a acurácia dos objetos na imagem, isto é: se na imagem há algum objeto que se encaixe em alguma das classes em que ele
foi treinado 

da visão computacional e processamento de imagem: Para processar as imagens e as redimencionar foi a biblioteca de código-aberto 
OpenCV, redimencionando a imagem "crua" para o padrão 244x244 pixels (altura x largura) 

da Conversão de dados não estruturados para estruturados: Nessa fase foi usada a biblioteca NumPy para converter os dados para um Array Numpy
e mudar a forma do input do modelo





### Procedimentos de Instalação e Configuração

### Pré-requisitos

Liste aqui os requisitos necessários para a instalação da sua solução, como versões de software, dependências, etc.

[Requisito 1]

[Requisito 2]

...

### Instalação

Explique os passos necessários para instalar a solução. Inclua comandos de terminal e outras instruções pertinentes.
