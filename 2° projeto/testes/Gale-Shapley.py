
#recebe projetos e alunos em 2 dicionários
projetos = {}
for i in range(30):
    a = (input().split())
    #monta o dicionário com os projetos na seguinte ordem:
    #código projeto : (número de vagas, requisito mínimo de notas para vagas) [alunos no projeto]
    projetos[a[0][1:-1]] = (int(a[1][:-1]), int(a[2][:-1])), []
alunos = {}
#alunosorted = {}
for i in range(100):
    a = input().split(':')
    a[1] = a[1].split()
    #monta o dicionário com os alunos na seguinte ordem:
    #código aluno : (projetos preferenciais na ordem na forma de dicionário com os pesos dos projetos), (Nota do aluno), [projeto que o aluno conseguiu vaga]
    alunos[a[0][1:-1]] = {a[1][0][1:-1] : 3, a[1][1][:-1] : 2, a[1][2][:-1] : 1}, (int(a[1][3][1:-1])), []
    #dicionário para ordenar pelas médias de cada aluno
#    alunosorted[a[0][1:-1]] = int(a[1][3][1:-1])
#ordenando o dicionário de alunos pelas médias de cada aluno  
#alu = {}
#for i in sorted(alunosorted, key = alunosorted.get, reverse=True):
#    alu[i] = alunos[i]
#alunos = alu

#variavel usada como condição de parada
altera = True
while altera:
    altera = False
    for proj in projetos:
        #se o projeto não estiver cheio ele procura o próximo aluno
        if projetos[proj][0][0] > len(projetos[proj][1]):
            for al in alunos:
                #se o aluno tiver nota para o projeto e tiver interesse no mesmo ele entrará
                if alunos[al][1] >= projetos[proj][0][1] and proj in alunos[al][0]:
                    #se o aluno não tiver em outro projeto ele apenas é cadastrado no atual
                    if len(alunos[al][2]) == 0:
                        alunos[al][2].append(proj)
                        projetos[proj][1].append(al)
                        altera = True
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
                            alunos[al][2][0] = proj
                            projetos[proj][1].append(al)
                            altera = True
                            break
                        
completos = 0
for proj in projetos:
    if projetos[proj][0][0] > len(projetos[proj][1]):
        print(f"{proj} : {projetos[proj][1]}")
    else:
        completos += 1
        print(f"{proj} : {projetos[proj][1]} COMPLETO")
for al in alunos:
    print(f"{al} : {alunos[al][2]}")
    
print(completos)