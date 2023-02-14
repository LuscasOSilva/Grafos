Lucas de Oliveira Silva.
200022857

Para rodar o projeto, digite no prompt:
O caminho da pasta com os arquivos do projeto
e em seguida a seguinte linha (python Sudoku.py)
sem os parenteses
------------------------------------------------------------------------
Algoritmo

Para construir o Sudoku como um grafo eu usei uma lista de lista,
onde cada lista/vetor representava um quadrante do Sudoku e cada 
um dos 9 itens na lista que são endereçados de 0 a 8 são uma posição 
do Sudoku ou um nó do grafo.

Para associar os vizinhos, que são os nós adjacentes eu fiz a função
'conferirVizinhos' que usa as funções 'vizinhosHorizontal' e 
'vizinhosVertical' para passar por toda a linha, toda a coluna e todo 
o quadrante de cada posição, sempre verificando se há já a o valor 
proposto nesses vizinhos e retorna False caso já tivermos o número 
proposto nos nós vizinhos/adjacentes.

A função 'imprimir' nos da uma imagem do grafo na forma de um Sudoku
com a seguinte disposição das listas de 0 a 8:
 0  |  1  |  2 
----------------
 3  |  4  |  5 
----------------
 6  |  7  |  8 

Sendo que cada uma dessas listas também tem espaços de 0 a 8 na 
seguinte disposição:
0 1 2
3 4 5
6 7 8

Para a resolução do Sudoku, eu utilizei a forma mais conhecida de 
resolver como um grafo, que é assumindo que todas as cores/valores 
são possiveis e coferir de um a um quais dos realmente possiveis 
podem ser usados, colocando todos os possiveis na ordem de 0 a 8 no 
grafo, ao encontrar uma posição sem escolha possivel, voltamos até
a ultima posição que tem outra possibilidade, então trocamos ela pela
próxima possível e continuamos, assim podemos achar todas as combinações
possível de Sudokus possíveis para cada proposta inicial.
claro que quanto menos posições iniciais tivermos mais esse algoritmo
irá demorar, pois ele percorre todas as possibilidades.

Tal algoritmo base pode ser visto nos seguintes links:
https://www.youtube.com/watch?v=PZJ5mjQyxR8&ab_channel=Pythonenthusiast
https://github.com/kosta93/Sudoku_Solver
eles foram alterados de diversas maneiras para que fossem implementados
de acordo com o desejado no meu código.

A função 'escolha' nos dá 3 opções básicas:

1 - Checar se uma proposta numérica é válida.

Onde podemos inserir uma proposta de jogo posição por posição (ou usar
a opção 3 para inserir uma proposta aleatória valida aqui) e depois 
verificar se ela é válida, podendo também visualizar todas as soluções
possíveis dessa tela proposta.

DURANTE AS RESOLUÇÕES SÃO MOSTRADOS ALGUNS DOS MILHARES DE PASSOS
DA RESOLUÇÃO, COM AS TELAS SENDO PREENCHIDAS

2 - Gerar soluções para um jogo dado.

Aqui podemos inserir uma proposta assim como na primeira opção, porem
teremos instantaneamente as possíveis resoluções dessa proposta de tela
caso ela seja válida.

DURANTE AS RESOLUÇÕES SÃO MOSTRADOS ALGUNS DOS MILHARES DE PASSOS
DA RESOLUÇÃO, COM AS TELAS SENDO PREENCHIDAS
 
3 - Gerar uma proposta aleatória para futuro jogo.

Nessa opção podemos criar uma proposta aleatória de tela com um bônus
de escolher a dificuldade da proposta, quando mais difícil, menos números
iniciais teremos na proposta. Podemos também salvar cada proposta criada
para usar nas outras 2 primeiras opções.

Em casos de propostas invalidas, as opções 1 e 2 apenas retornaram que 
são invalidas.