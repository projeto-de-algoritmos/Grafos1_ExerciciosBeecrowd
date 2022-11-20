# 1195 - Árvore Binária de Busca

Link do problema resolvido - https://www.beecrowd.com.br/judge/pt/problems/view/1195

## Descrição do Problema
Em uma árvore binária, o percurso por nível é um percurso denominado breadth first search (BFS) ou em português, busca em largura, a qual seria não-recursiva por natureza. Este percurso utiliza uma fila ao invés de pilha para armazenar os próximos 2 nodos que devem ser pesquisados (filho à esquerda e à direita). Esta é a razão pela qual você deve percorrer os nodos na ordem FIFO ao invés da ordem LIFO, obtendo desta forma a recursão.

Portanto nossa tarefa aqui, após algumas operações de inserção sobre uma árvore binária de busca (pesquisa), é imprimir o percurso por nível sobre estes nodos. Por exemplo, uma entrada com a sequência de valores inteiros: 8 3 10 14 6 4 13 7 1 resultará na seguinte árvore:


## Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro C (C ≤ 1000), indicando o número de casos de teste que virão a seguir. Cada caso de teste é composto por 2 linhas. A primeira linha contém um inteiro N (1 ≤ N ≤ 500) que indica a quantidade de números que deve compor cada árvore e a segunda linha contém N inteiros distintos e não negativos, separados por um espaço em branco.

## Saída
Para cada caso de teste de entrada você deverá imprimir a mensagem "Case n:", onde n indica o número do caso de teste seguido por uma linha contendo a listagem por nível dos nodos da árvore, conforme o exemplo abaixo.

Obs: Não deve haver espaço em branco após o último item de cada linha e há uma linha em branco após cada caso de teste, inclusive após o último. A árvore resultante não terá nodos repetidos e também não terá mais do que 500 níveis.

## Resolução

O problema foi resolvido através da implementação de uma árvore de busca binária, na qual utilizamos nós com informações da dado, esquerda e direita, aplicando a lógica necessária para posicionar os mesmos da maneira correta. Após isso usamos o BFS para definir os níveis do árvore e, consequentemente, retornar uma lista com a ordem exata que esperamos dos dados.
