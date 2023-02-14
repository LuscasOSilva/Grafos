#variavel usada como condição de parada
altera = True
while altera:
    altera = False
    for proj in projetos:
        print('cu')
        #se o projeto não estiver cheio ele procura o próximo aluno
        if projetos[proj][0][0] > len(projetos[proj][1]):
            for al in alunos:
                #se o aluno tiver nota para o projeto e tiver interesse no mesmo ele entrará
                if alunos[al][1] >= projetos[proj][0][1] and proj in alunos[al][0]:
                    #se o aluno já estiver em outro projeto vamos ver qual ele tem mais interesse 
                    if len(alunos[al][2]) == 0:
                        alunos[al][2].append(proj)
                        projetos[proj][1].append(al)
                        altera = True
                        break
                    else:
                        if alunos[al][0][alunos[al][2][0]] < alunos[al][0][proj]:
                            #deletando o aluno do projeto de menos interesse
                            for delet in projetos[alunos[al][2][0]][1]:
                                if delet == alunos[al][2][0]:
                                    del delet
                            alunos[al][2].append(proj)
                            projetos[proj][1].append(al)
                            altera = True
                            break
#for proj in projetos:
#    print(f"{proj} : {projetos[proj][1]}")