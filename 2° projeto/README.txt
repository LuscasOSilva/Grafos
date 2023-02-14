Para rodar o projeto, digite no prompt:
O caminho da pasta com os arquivos do projeto
e em seguida a seguinte linha (type entradaProj2TAG.txt | python "Gale_Shapley.py")
obviamente sem os parenteses
------------------------------------------------------------------------
Algoritmo

Primeiro recebemos os projetos e os alunos nos seguintes formatos de
dicionário respectivamente:
código projeto : (número de vagas, requisito mínimo de notas para vagas) [alunos no projeto]
código aluno : (projetos desejados na forma de dicionário com os pesos dos projetos pela importância pro aluno), (Nota do aluno), [projeto que o aluno conseguiu vaga]
os ultimos 2 campos de cada um começa vazio.

Teremos 2 FOR que passaram pelos projetos e pelos alunos, sempre que 
encontramos um aluno qualificado e com interesse no projeto 
verificamos se o aluno já está em outro projeto mas tem interesse 
maior no atual, se ele tiver mais interesse no atual ou não estiver em 
nenhum outro projeto ele pode entra no atual, então quebramos a busca 
e vamos para o próximo projeto.

Quando temos projetos cheios também verificam se há um aluno mais 
qualificado do que os que já estão nele, se ouver um aluno com interesse
e mais qualificado ele entra no lugar do aluno com a nota menor que a dele.

Por fim o algoritmo imprime os resultados dos projetos e alunos, em 
projetos que podem ser realizados por atingirem o limite máximo de alunos
haverá um "COMPLETO" ao lado.