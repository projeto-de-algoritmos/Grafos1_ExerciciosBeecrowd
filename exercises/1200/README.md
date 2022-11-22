# 1200 - Operações em ABP I

Link do problema resolvido - https://www.beecrowd.com.br/judge/pt/problems/view/1200

## Descrição do Problema
Marcela recebeu como trabalho de Algoritmos a tarefa de fazer um programa que implemente uma Árvore Binária de Pesquisa (ou Busca). O Programa deve aceitar os seguintes comandos:

- I n: Insere na árvore binária de pesquisa o elemento n.
- INFIXA: lista os elementos já cadastrado segundo o percurso infixo
- PREFIXA: lista os elementos já cadastrado segundo o percurso prefixo
- POSFIXA: lista os elementos já cadastrado segundo o percurso posfixo
- P n: pesquisa se o elemento n existe ou não.


A qualquer momento pode-se inserir um elemento, visitar os elementos previamente inseridos na ordem infixa, prefixa ou posfixa ou ainda procurar por um elemento na árvore para saber se o elemento existe ou não.


## Entrada
A entrada contém N operações utilizando letras (A-Z,a-z) sobre uma árvore binária de Busca, que inicialmente se encontra vazia. A primeira linha de entrada contém a inserção de algum elemento. As demais linhas de entrada podem conter quaiquer um dos comandos descritos acima, conforme exemplo abaixo. O final da entrada é determinado pelo final de arquivo (EOF).

Obs: Considere que não serão inseridos elementos repetidos na árvore.

## Saída
Cada linha de entrada, com exceção das linhas que contém o comando "I", deve produzir uma linha de saída. A saída deve ser de acordo com o exemplo fornecido abaixo. Não deve haver espaço em branco após o último caractere de cada linha, caso contrário, sua submissão receberá Presentation Error.

## Resolução

O problema foi resolvido através da implementação de uma árvore de busca binária, na qual utilizamos nós com informações da dado, esquerda e direita, aplicando a lógica necessária para posicionar os mesmos da maneira correta. Após isso usamos os algoritmos para inorder, preorder, postorder e search para, assim realizar as operações com as devidas entradas.
