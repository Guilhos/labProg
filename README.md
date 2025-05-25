# Repositório de Projetos - Laboratório de Programação

## Lista

As respostas da lista estão na pasta `lista`, cada resposta separada por arquivo.

### Q1
A questão do sapo Alef

A estratégia utilizada foi tentar iterar o máximo de vezes para calcular a probabilidade de cada local no mapa. Essa estratégia foi adotada, pois não existe caminho certo para o Alef, se existisse, a probabilidade sempre seria 100%, pois o sapo já saberia o caminho.

Então foi criado de forma iterativa, onde cada passo é aleatório e a probabilidade de um quadrado é a média das probabilidades dos 4 quadrados vizinhos.

### Q2
Insertion sort

Algoritmo de insertion Sort comum, meio difícil, pois foi minha primeira vez desenvolvendo em C

### Q3
Mediana e notificação

Dentro do array da semana, é pego uma sublista dos ultimos dias. Essa sublista passa por um quick sort próprio do C e então é calculada a mediana, pegando o valor do meio, se não tiver meio, é feita a média dos valores intermediarios.

Depois é comparado com o valor do dia atual, se a mediana for menor a notificação é disparada.

### Q4
REGEX

Algoritmo de identificação de regex, primeiro é criado um "tradutor" do regex que entra, depois da tradução é criada uma árvore que irá fazer as operações aritimeticas. Dessa vez foi aplicado em python pois tenho mais familiaridade.

### Q5
Árvore e similaridade

Foi criado uma árvore comum e depois aplicado uma procura nela para encontrar itens similares em sua estrutura. As entradas são as entradas padrão apresentadas pelo codigo do professor.

