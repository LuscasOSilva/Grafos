#recebe projetos e alunos em 2 dicionários
for n in range(3):
    a = input()
projetos = {}
for i in range(30):
    a = (input().split())
    #monta o dicionário com os projetos na seguinte ordem:
    #código projeto : (número de vagas, requisito mínimo de notas para vagas) [alunos no projeto]
    projetos[a[0][1:-1]] = (int(a[1][:-1]), int(a[2][:-1])), []
for n in range(4):
    a = input()
alunos = {}
for i in range(100):
    a = input().split(':')
    a[1] = a[1].split()
    #monta o dicionário com os alunos na seguinte ordem:
    #código aluno : (projetos preferenciais na ordem na forma de dicionário com os pesos dos projetos), (Nota do aluno), [projeto que o aluno conseguiu vaga]
    alunos[a[0][1:-1]] = {a[1][0][1:-1] : 3, a[1][1][:-1] : 2, a[1][2][:-1] : 1}, (int(a[1][3][1:-1])), []
#variavel usada como condição de parada
altera = True
contador = 0 
while altera:
    altera = False
    for proj in projetos:
        for al in alunos:
            #se o projeto não estiver cheio ele procura o próximo aluno
            if projetos[proj][0][0] > len(projetos[proj][1]):
                #se o aluno tiver nota para o projeto e tiver interesse no mesmo ele pode entrar no atual projeto
                if alunos[al][1] >= projetos[proj][0][1] and proj in alunos[al][0]:
                    #se o aluno não tiver em outro projeto ele apenas é cadastrado no atual
                    if len(alunos[al][2]) == 0:
                        alunos[al][2].append(proj)
                        projetos[proj][1].append(al)
                        altera = True
                        def mostrar():
                            global contador
                            global al
                            global proj
                            global projetos
                            contador += 1
                            #mostrar as 10 primeiras interações até o resultado final
                            if contador <= 10:
                                print(f'\n{contador}° modificação: O aluno {al} entrou no projeto {proj}')
                                print(f'Projetos com alunos:')
                                for i in projetos:
                                    if len(projetos[i][1]) > 0:
                                        print(f"{i} : {projetos[i][1]}")
                        mostrar()
                        break
                    #se o aluno já estiver em outro projeto vamos ver qual ele tem mais interesse 
                    else:
                        #caso ele tenha interesse no atual ele é trocado de projeto
                        if alunos[al][0][alunos[al][2][0]] < alunos[al][0][proj]:
                            #deletando o aluno do projeto de menos interesse
                            for delet in range(len(projetos[alunos[al][2][0]][1])):
                                if projetos[alunos[al][2][0]][1][delet] == al:
                                    del projetos[alunos[al][2][0]][1][delet]
                                    break
                            #adicionando o aluno no projeto atual
                            alunos[al][2][0] = proj
                            projetos[proj][1].append(al)
                            altera = True
                            mostrar()
                            break
            else:
                #se o projeto estiver cheio vamos conferir se ele pode trocar um aluno por outro mais qualificado
                #nota aluno >= nota mínima para o projeto e o aluno tem interesse no projeto
                if alunos[al][1] >= projetos[proj][0][1] and proj in alunos[al][0]:
                    #variável para conferir se ouve troca de alunos 
                    aumenta = False
                    #procura um aluno menos qualificado para ser substituido
                    for i in projetos[proj][1]:
                        #se a nota de um aluno já cadastrado for menor que o aluno atual vamos pegar o aluno atual
                        if alunos[i][1] < alunos[al][1]:
                            #se o aluno não tiver em outro projeto ele apenas é cadastrado no atual
                            if len(alunos[al][2]) == 0:
                                #deletando o cadastro do aluno menos qualificado
                                for delet in range(len(projetos[alunos[i][2][0]][1])):
                                    if projetos[alunos[i][2][0]][1][delet] == i:
                                        del projetos[alunos[i][2][0]][1][delet]
                                        break
                                #tirando o projeto do cadastro dele
                                alunos[i] = alunos[i][:-1] + tuple([[]])
                                #cadastrando novo aluno
                                alunos[al][2].append(proj)
                                projetos[proj][1].append(al)
                                altera = True
                                aumenta = True
                                mostrar()
                                break
                            #se o aluno já estiver em outro projeto vamos ver qual ele tem mais interesse 
                            else:
                                #caso ele tenha interesse no atual ele é trocado de projeto
                                if alunos[al][0][alunos[al][2][0]] < alunos[al][0][proj]:
                                    #deletando o aluno do projeto de menos interesse
                                    for delet in range(len(projetos[alunos[al][2][0]][1])):
                                        if projetos[alunos[al][2][0]][1][delet] == al:
                                            del projetos[alunos[al][2][0]][1][delet]
                                            break
                                    #deletando o aluno anterior (menos qualificado) do projeto atual
                                    for delet in range(len(projetos[alunos[i][2][0]][1])):
                                        if projetos[alunos[i][2][0]][1][delet] == i:
                                            del projetos[alunos[i][2][0]][1][delet]
                                            break
                                    #tirando o projeto do cadastro dele
                                    alunos[i] = alunos[i][:-1] + tuple([[]])
                                    #cadastrando novo aluno
                                    alunos[al][2][0] = proj
                                    projetos[proj][1].append(al)
                                    altera = True
                                    aumenta = True
                                    mostrar()
                                    break
                    #se tiver ocorrido troca de alunos vamos para o próximo projeto
                    if aumenta:
                        break

#variável que conta quantos projetos estão cheios e podem acontecer.
completos = 0

#imprimir todos os projetos com os devidos alunos que estão nele, projetos cheios teram um "COMPLETO".
print('\nProjetos com seus devidos alunos cadastrados:')
for proj in projetos:
    if projetos[proj][0][0] > len(projetos[proj][1]):
        print(f"{proj} : {projetos[proj][1]}")
    else:
        #soma +1 ao total de projetos completos
        completos += 1
        print(f"{proj} : {projetos[proj][1]} COMPLETO")
#imprimir todos os alunos com o projeto que cada aluno está
print('\nAlunos com o projeto que vão participar:')
for al in alunos:
    print(f"{al} : {alunos[al][2]}")
    
#imprime o número de projetos completos
print(f'\nNúmero de projetos que podem ser realizados: {completos}')