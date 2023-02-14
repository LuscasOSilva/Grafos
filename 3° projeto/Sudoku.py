#Lucas de Oliveira Silva.
#200022857



from random import randrange

#Cria a tabela para sudoku vázio, onde cada lista será um quadrante do Sudoku em forma de grafo.
sdk = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#sera usada para armazenar os sudokus dados na função escolha()
sdk3 = sdk

#imprime o sudoku
def imprimir():
    global sdk
    print('\n')
    for i in [0, 3, 6]:
        for l in [0, 3, 6]:
            print(f'{sdk[i][l]} {sdk[i][l+1]} {sdk[i][l+2]} | {sdk[i+1][l]} {sdk[i+1][l+1]} {sdk[i+1][l+2]} | {sdk[i+2][l]} {sdk[i+2][l+1]} {sdk[i+2][l+2]}')
        if i in [0, 3]:
            print('---------------------')
            
#retorna a sequencia que deve ser percorrida na horizontal para ver a fileira
def vizinhosHorizontal(n):
    if 0 <= n and n < 3:
        return [0, 1, 2]
    if 3 <= n and n < 6:
        return [3, 4, 5]
    if 6 <= n and n < 9:
        return [6, 7, 8]
    
#retorna a sequencia que deve ser percorrida na vertical para ver a coluna
def vizinhosVertical(n):
    if n in [0, 3, 6]:
        return [0, 3, 6]
    if n in [1, 4, 7]:
        return [1, 4, 7]
    if n in [2, 5, 8]:
        return [2, 5, 8]

#se tiver um vizinho com o digito dado, retornará False
def conferirVizinhos(digito, quadrado, posicao):
    global sdk
    #confere vizinhos horizontais
    for i in vizinhosHorizontal(quadrado):
        for l in vizinhosHorizontal(posicao):
            if [i, l] != [quadrado, posicao]:
                if sdk[i][l] == digito:
                    return False
    
    #confere vizinhos verticais
    for i in vizinhosVertical(quadrado):
        for l in vizinhosVertical(posicao):
            if [i, l] != [quadrado, posicao]:
                if sdk[i][l] == digito:
                    return False
    
    #confere vizinhos do quadrante
    for i in range(len(sdk[quadrado])):
        if posicao != i:
            if digito == sdk[quadrado][i]:
                return False
    return True

#variavel que irá determinar se o sudoku foi completado em algumas funçoes.
cabo = False
#variavel que conta quantos quadrados foram preenchidos durante a função resolverDeFato().
contador = 0

#verifica se o sudoku pode ser resolvido
#algoritmo base pode ser visto nos seguintes links:
#https://www.youtube.com/watch?v=PZJ5mjQyxR8&ab_channel=Pythonenthusiast
#https://github.com/kosta93/Sudoku_Solver
def possivelResolver():
    global sdk
    global cabo
    if not cabo:
        for i in range(0,9):
            for l in range(0,9):
                if sdk[i][l] == ' ':
                    #escolhe um numero para entrar no quadrante i na posição l
                    for n in range(1,10):
                        #confere se é possivel encaixar tal numero na posiçao l
                        if conferirVizinhos(n, i, l):
                            sdk[i][l] = n
                            #chama a função para a proxima posição nao preenchida
                            possivelResolver()
                            #quando algo da errado e nao achamos a soluçao da posição, voltamos e alteramos as anteriores para arrumar
                            sdk[i][l] = ' '

                    return
    cabo = True
#reseta a variavel e chama a função possivelResolver()
def inicioPossivelResolver():
    global cabo
    cabo = False
    possivelResolver()

#insere numeros no sudoku vazio e verifica se ainda podemos resolver depois de cada numero adicionado
def inserir():
    global sdk
    global cabo
    #escolhe aleatoriamente um quadrado, uma posiçao e o numero a ser inserido
    quadr = randrange(0,9)
    posic = randrange(0,9)
    n = randrange(1,10)
    #insere se estiver vario e nao tiver a mesma cor/número nos vizinhos 
    if conferirVizinhos(n, quadr, posic) and sdk[quadr][posic] == ' ':
        sdk2 = sdk
        sdk[quadr][posic] = n
        inicioPossivelResolver()
        if not cabo:
            sdk = sdk2
            inserir()
    else:
        inserir()
        
#Função que resolve o Sudoku caso seja possível e mantem ele inteiro no final
#algoritmo base pode ser visto nos seguintes links:
#https://www.youtube.com/watch?v=PZJ5mjQyxR8&ab_channel=Pythonenthusiast
#https://github.com/kosta93/Sudoku_Solver
def resolve():
    global sdk
    global cabo
    global sdkCompleto
    if not cabo:
        for i in range(0,9):
            for l in range(0,9):
                if sdk[i][l] == ' ':
                    for n in range(1,10):
                        if conferirVizinhos(n, i, l):
                            sdk[i][l] = n
                            resolve()
                            #essa funçao nao apaga as mudanças feitas em um sudoku terminado
                            if not cabo:
                                sdk[i][l] = ' '

                    return
    cabo = True    
#da o reset nas variaveis e chama a função resolve()
def inResolve():
    global cabo
    cabo = False
    resolve()

#retira um numero do Sudoku pronto
def retirar():
    global sdk
    quadr = randrange(0,9)
    posic = randrange(0,9)
    if sdk[quadr][posic] != ' ':
        sdk[quadr][posic] = ' '
    else:
        retirar()

#Cria um novo Sudoku com números iniciais
def Criar():
    global sdk
    #escolher a dificuldade do Sudoku(quanto mais difícil, menos números vamos ter no fim)
    try:
        escolha = int(input('\nDigite o número da dificuldade desejada para o Sudoku:\n1 - Fácil.\n2 - Normal.\n3 - Difícil.\n'))
    except:
        print('Entrada inválida.')
        return Criar()
    if escolha not in [1, 2, 3]:
        print('Entrada inválida.')
        return Criar()
    q = randrange(6,8)
    for i in range(q):
        inserir()
    inResolve()
    #apaga a maior parte do sudoku para terminar de construir a proposta que funciona
    #dependendo da dificuldade ele apaga tamanhos diferentes
    if escolha == 1:
        q = randrange(41,45)
        for i in range(q):
            retirar()
    if escolha == 2:
        q = randrange(48,52)
        for i in range(q):
            retirar()
    if escolha == 3:
        q = randrange(53,56)
        for i in range(q):
            retirar()
        
#insere número por número nas posições
def recebeDado():
    global sdk
    #recebe a posição do quadrante e a posição dentro do quadrante escolhido, além do numero que irá ser colocado lá
    try:
        quadrado = int(input('\nDigite a posição do quadrante que deseja inserir o número(de acordo com a disposição):\n'))
        posicao = int(input(f'Digite a posição do número no quadrante {quadrado} que deseja inserir o número(de acordo com a disposição):\n'))
        n = int(input('Digite o número que deseja inserir:\n'))
    except:
        return recebeDado()
    if quadrado in [1, 2, 3, 4, 5, 6, 7, 8, 9] and posicao in [1, 2, 3, 4, 5, 6, 7, 8, 9] and n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        #coloca o numero na posiçao do sudoku decidida
        sdk[quadrado - 1][posicao - 1] = n
        #mostra o estado atual do sudoku
        print('\nResultado:')
        imprimir()
        #confere se há mais para entrar
        q = input('\nDeseja inserir outro número? Digite:\n "S" para Sim.\n "N" para Não.\n(Sem aspas)\n')
        if q == 'S' or q == 's':
            recebeDado()
        else:
            #mostra a resultado final
            print('\nSugestão montada:')
            imprimir()
    else:
        print('Entrada inválida.')
        recebeDado()

#escolha de como será recebido os dados e receber
def receber():
    global sdk
    global sdk3
    
    try:
        q = int(input('\nComo deseja dar entrada dos números da proposta?\n(Digite o numero da operação)\n1 - Manualmente, número por número.\n2 - Proposta criada pelo app ao usar a opção 3 do menu principal.\nDigite qualquer outra coisa para voltar ao menu anterior.\n'))
    except:
        return
    #se a escolha for 1 ele recebera numero por numero e colocará no grafo em forma de sudoku
    if q == 1:
        #informa como as posiçoes funcionam
        print('\nTemos a seguinte disposição de quadrantes:\n 1  |  2  |  3 \n _______________ \n 4  |  5  |  6 \n _______________ \n 7  |  8  |  9 ')
        print('As posições para números dentro dos quadrantes tem a mesma sequência de endereço.')
        #chama a funcão que recebe dados ate o usuario parar
        recebeDado()
    #se a escolha for 2 vamos verificar se ja temos uma proposta em sdk3
    if q == 2:
        #se houver, nos iremos recebela no grafo principal
        if sdk != sdk3:
            sdk = sdk3
            #imprime a sugestao 
            print('\nSugestão montada:')
            imprimir()
        else:
            #se nao tivermos rodado a opçao 3 anteriormente, nao recebemos nada e retornamos falso para saber que nada foi retornado
            print('\nNão há nada salvo da opção 3 do menu principal.')
            return False
    #caso tenhamos recebido algo, retonamos true, e false caso nao tenhamos recebido nada.
    if q in [1, 2]:
        return True
    return False

ver = True

#Função que mostra todas as possíveis resoluções de sudoku com seus passos.
#algoritmo base pode ser visto nos seguintes links:
#https://www.youtube.com/watch?v=PZJ5mjQyxR8&ab_channel=Pythonenthusiast
#https://github.com/kosta93/Sudoku_Solver
def resolverDeFato():
    global sdk
    global cabo
    global ver
    global contador
    #se o usuario ainda quiser ver os resultados
    if ver:
        for i in range(0,9):
            for l in range(0,9):
                if sdk[i][l] == ' ':
                    for n in range(1,10):
                        if conferirVizinhos(n, i, l):
                            contador += 1
                            sdk[i][l] = n
                            #imprime alguns passos do sudoku
                            if contador%9 == 0 and ver:
                                print(f'\nSequencia com {contador} números colocados:')
                                imprimir()
                            resolverDeFato()
                            contador -= 1
                            sdk[i][l] = ' '

                    return
        
        if ver:
            print('\n1 Solução possivel completa:')
            imprimir()
            q = input('\nDeseja ver a próxima solução? Digite:\n "S" para Sim.\n "N" para Não.\n(Sem aspas)\n')
            if not(q == 'S' or q == 's'):
                ver = False
        cabo = True

#reseta as variaveis necessarias e chama a funçao resolverDeFato()
def inResolverDeFato():
    global cabo
    global ver
    ver = True
    cabo = False
    resolverDeFato()
    
#função que passa por todo o grafo verificando se não há nenhum digito que torna impossivel, nas propostas dadas pelo usuario
def conferirPossivel():
    global sdk
    for i in range(len(sdk)):
        for l in range(len(sdk)):
            if sdk[i][l] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if not conferirVizinhos(sdk[i][l], i, l):
                    return False
    return True

#Parte de interação com o usuário
def escolha():
    global sdk
    global sdk3
    global cabo
    global ver
    sdk = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    try:
        q = int(input('\nDigite o número da operação que deseja realizar:\n1 - Checar se uma proposta numérica é válida.\n2 - Gerar soluções para um jogo dado.\n3 - Gerar uma proposta aleatória para futuro jogo.\n(Na opção 3 você pode gerar uma proposta para ser usada nas outras 2 opções.)\n'))
    except:
        print('Entrada inválida.')
        return escolha()
    if q == 1:
        #recebe uma proposta ou usa a da opção 3 anterior
        esc = receber()
        #se a proposta foi recebida com sucesso vamos conferir se é possivel resolver
        if esc:
            #verifica se nao temos nenhum vizinho igual para todos os digitos colocados
            if conferirPossivel():
                #caso possamos, os resultados possiveis de resolução sao pesquisados
                inicioPossivelResolver()
                if cabo:
                    print('A proposta é válida, tem solução.')
                    #oportunidade de resolver a proposta válida
                    oportunidade = input('\nDeseja conferir a resolução da proposta acima? Digite:\n "S" para Sim.\n "N" para Não.\n(Sem aspas)\n')
                    if oportunidade == 'S' or oportunidade == 's':
                        #caso possamos, os resultados possiveis de resolução sao pesquisados
                        inResolverDeFato()
                        #se achamos todas as propostas e queremos ver mais, sendo que nao existe mais as resoluçoes temos a seguinte mensagem
                        if cabo:
                            if ver:
                                print('Não há mais soluções.')
                else:
                    print('A proposta é invalida, não tem solução.')
            else:
                print('A proposta é invalida, não tem solução.')
    if q == 2:
        #recebe uma proposta ou usa a da opção 3 anterior
        esc = receber()
        #se a proposta foi recebida com sucesso vamos conferir se é possivel resolver
        if esc:
            #verifica se nao temos nenhum vizinho igual para todos os digitos colocados
            if conferirPossivel():
                #caso possamos, os resultados possiveis de resolução sao pesquisados
                inResolverDeFato()
                #se achamos todas as propostas e queremos ver mais, sendo que nao existe mais as resoluçoes temos a seguinte mensagem
                if cabo:
                    if ver:
                        print('Não há mais soluções.')
                else:
                    print('A proposta é invalida, não tem solução.')
            #se houver vizinhos iguais a proposta é invalida
            else:
                print('A proposta é invalida, não tem solução.')
                
    if q == 3:
        #cria uma proposta inicial aleatoria
        Criar()
        print('Proposta válida criada:')
        imprimir()
        copia = input('\nDeseja usar a proposta dada acima para usar nas próximas operações? Digite:\n "S" para Sim.\n "N" para Não.\n(Sem aspas)\n')
        if copia == 'S' or copia == 's':
            sdk3 = sdk
        
    if q not in [1, 2, 3]:
        print('Entrada inválida.')
        escolha()
    q = input('\nDeseja fazer outra operação no menu principal? Digite:\n "S" para Sim.\n "N" para Não.\n(Sem aspas)\n')
    if q == 'S' or q == 's':
        escolha()
    else:
        print('\nAté a próxima!!!\n░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█ \n░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█ \n░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█ \n░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌ \n░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█ \n▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌ \n█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█ \n█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█ \n▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌ \n▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌ \n█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█ ')


escolha()