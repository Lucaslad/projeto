import random

#VARIÁVEIS DO PROGRAMA
statusJogadores = "" #Variável que mostra o estado atual  dos jogadores (0 = Livre; 1 = Preso por 1 turno; 2 = Preso por 2 turnos; 3 = Preso por 3 turnos; 4 = Falido)
casaNome = "" #Variável que mostra o nome da cada do tabuleiro
terrenos = "" #Variável que mostra os respectivos terrenos, com seu id, preço e aluguel, formatado em (00)ID, (000)Preço, (000)Aluguel
#IDs = 00 = Sem proprietário / 06 = Ponto de partida / 01~05 = Reservado a jogadores / 07 = Imposto / 08 = Vá para prisão / 09 = Prisão / 10 = Jackpot

#CÓDIGO
numJogadores = int(input("Digite o número de jogadores (De 2 a 5 jogadores): "))
while(numJogadores<2 or numJogadores>5):
    print("Apenas 2 a 5 jogadores")
    numJogadores = int(input("Digite o número de jogadores (De 2 a 5 jogadores): "))
for i in range(0, numJogadores):
    print("Digite o nome do" ,(i+1), "jogador")
    nome = input()
    if(i==0):
        nome1 = nome
    elif(i==1):
        nome2 = nome
    elif(i==2):
        nome3 = nome
    elif (i==3):
        nome4 = nome
    elif(i==4):
        nome4 = nome
    elif(i==5):
        nome5 = nome
statusJogadores = "00000"
posicao1 = 0
posicao2 = 0
posicao3 = 0
posicao4 = 0
posicao5 = 0
casaNome1 = ""
casaNome2 = ""
casaNome3 = ""
casaNome4 = ""
casaNome5 = ""
spacecoins1 = 10000
spacecoins2 = 10000
spacecoins3 = 10000
spacecoins4 = 10000
spacecoins5 = 10000
pertence1=""
pertence2=""
pertence3=""
pertence4=""
pertence5=""
pertence6=""
pertence7=""
pertence8=""
pertence9=""
pertence10=""
pertence11=""
pertence12=""
pertence13=""
pertence14=""
pertence15=""
pertence16=""
pertence17=""
pertence18=""
pertence19=""
pertence20=""
pertence21=""
pertence22=""
pertence23=""
pertence24=""
gameover = False
while not gameover:
    for i in range (0, numJogadores):
        if(i==0):
            print()
            print(nome1, "sua vez de jogar")
            jogar = ""
            while(jogar != "encerrar"):
                print()
                print(nome1, ", digite:")
                print("1 - Para saber sua posição na galáxia")
                print("2 - Para saber quantos Spacecoins possui")
                print("3 - Para ver seus territórios comprados")
                print("jogar - Para jogar os dados")
                jogada = input()
                if (jogada=="1"):
                    print("Posição:" ,posicao1,casaNome1)
                elif (jogada=="2"):
                    print("Spacecoins:" ,spacecoins1)
                elif (jogada=="3"):
                    print()
                elif (jogada=="jogar" or jogada=="Jogar"):
                    dado = random.randint(1,6)
                    posicao1 += dado
                    if (posicao1==1):
                        casaNome1 = "- Fronteira Intergalática/Portões do Universo"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if(pertence1=="" or pertence1==nome1):
                            print("Você deseja comprar este território por" ,preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if(comprar=="sim"):
                                if(preco!=0):
                                    if(pertence1==nome1):
                                        print("Esse território já é seu")
                                        while(jogar!="encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif(pertence1==""):
                                        spacecoins1-=preco
                                        pertence1=nome1
                                        print("Território adquirido")
                                        print("Agora você possui" ,spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é" ,aluguel, "Spacecoins")
                            spacecoins1-=aluguel
                            print("Agora você possui" ,spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==2):
                        casaNome1 = "- Base Interplanetária de Vênus"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence2 == "" or pertence2 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence2 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence2 == ""):
                                        spacecoins1 -= preco
                                        pertence2 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==3):
                        casaNome1 = "- Base Interplanetária da Terra"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence3 == "" or pertence3 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence3 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence3 == ""):
                                        spacecoins1 -= preco
                                        pertence3 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==4):
                        casaNome1 = "- Base Interplanetária de Marte"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence4 == "" or pertence4 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence4 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence4 == ""):
                                        spacecoins1 -= preco
                                        pertence4 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==5):
                        casaNome1 = "- Base Interplanetária de Júpiter"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence5 == "" or pertence5 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence5 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence5 == ""):
                                        spacecoins1 -= preco
                                        pertence5 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==6):
                        casaNome1 = "- Base Interplanetária de Saturno"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence6 == "" or pertence6 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence6 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence6 == ""):
                                        spacecoins1 -= preco
                                        pertence6 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==7):
                        casaNome1 = "- Prisão Univeral/Passagem de Visitantes"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence7 == "" or pertence7 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence7 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence7 == ""):
                                        spacecoins1 -= preco
                                        pertence7 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==8):
                        casaNome1 = "- Base Lunar da Terra"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence8 == "" or pertence8 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence8 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence8 == ""):
                                        spacecoins1 -= preco
                                        pertence8 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==9):
                        casaNome1  = "- Base Lunar de Fobos"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence9 == "" or pertence9 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence9 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence9 == ""):
                                        spacecoins1 -= preco
                                        pertence9 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==10):
                        casaNome1 = "- Base Lunar Europa"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence10 == "" or pertence10 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence10 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence10 == ""):
                                        spacecoins1 -= preco
                                        pertence10 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==11):
                        casaNome1 = "- Base Lunar de Pandora"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence11 == "" or pertence11 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence11 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence11 == ""):
                                        spacecoins1 -= preco
                                        pertence11 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==12):
                        casaNome1 = "- Base Lunar de Talassa"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence12 == "" or pertence12 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence12 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence12 == ""):
                                        spacecoins1 -= preco
                                        pertence12 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==13):
                        casaNome1 = "- Satélite da sorte: JACKPOT"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence13 == "" or pertence13 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence13 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence13 == ""):
                                        spacecoins1 -= preco
                                        pertence13 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==14):
                        casaNome1 = "- Planeta anão: Plutão"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence14 == "" or pertence14 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence14 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence14 == ""):
                                        spacecoins1 -= preco
                                        pertence14 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==15):
                        casaNome1 = "- Planeta anão: Éris"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence15 == "" or pertence15 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence15 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence15 == ""):
                                        spacecoins1 -= preco
                                        pertence15 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==16):
                        casaNome1 = "- Planeta anão: Haumea"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence16 == "" or pertence16 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence16 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence16 == ""):
                                        spacecoins1 -= preco
                                        pertence16 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==17):
                        casaNome1 = "- Planeta anão: Ceres"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence17 == "" or pertence17 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence17 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence17 == ""):
                                        spacecoins1 -= preco
                                        pertence17 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==18):
                        casaNome1 = "- Planeta anão: Makemake"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence18 == "" or pertence18 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence18 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence18 == ""):
                                        spacecoins1 -= preco
                                        pertence18 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==19):
                        casaNome1 = "- Vá para a prisão universal!"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence19 == "" or pertence19 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence19 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence19 == ""):
                                        spacecoins1 -= preco
                                        pertence19 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==20):
                        casaNome1 = "- Base extra-solar Gliese 581 d"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence20 == "" or pertence20 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence20 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence20 == ""):
                                        spacecoins1 -= preco
                                        pertence20 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==21):
                        casaNome1 = "- Base extra-solar Upsilon Andromedae"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence21 == "" or pertence21 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence21 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence21 == ""):
                                        spacecoins1 -= preco
                                        pertence21 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==22):
                        casaNome1 = "- Base extra-solar X0-3b"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence22 == "" or pertence22 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence22 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence22 == ""):
                                        spacecoins1 -= preco
                                        pertence22 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==23):
                        casaNome1 = "- Base extra-solar C0R0T-Exo-1b"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence23 == "" or pertence23 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence23 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence23 == ""):
                                        spacecoins1 -= preco
                                        pertence23 = nome1
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins1 -= aluguel
                            print("Agora você possui", spacecoins1, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao1==24):
                        casaNome1 = "- Imposto espacial"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao1, casaNome1)
                        if (pertence24 == "" or pertence24 == nome1):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence24 == nome1):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                elif (pertence24 == ""):
                                    spacecoins1 -= preco
                                    pertence24 = nome1
                                    print("Território adquirido")
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                print("Este terreno não pode ser comprado")
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    else:
                        print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                        spacecoins1 -= aluguel
                        print("Agora você possui", spacecoins1, "Spacecoins")
                        while (jogar != "encerrar"):
                            print("Digite encerrar para encerrar sua jogada")
                            jogar = input()
                elif(posicao1>24):
                    posicao1 = 1

        elif(i==1):
            print()
            print(nome2, "sua vez de jogar")
            jogar = ""
            while(jogar != "encerrar"):
                print()
                print(nome2, ", digite:")
                print("1 - Para saber sua posição na galáxia")
                print("2 - Para saber quantos Spacecoins possui")
                print("3 - Para ver seus territórios comprados")
                print("jogar - Para jogar os dados")
                jogada = input()
                if (jogada=="1"):
                    print("Posição:" ,posicao2,casaNome2)
                elif(jogada=="2"):
                    print("Spacecoins:" ,spacecoins2)
                elif(jogada=="3"):
                    print()
                elif(jogada=="jogar" or jogada=="Jogar"):
                    dado = 4
                    posicao2 += dado
                    if (posicao2==1):
                        casaNome2 = "- Fronteira Intergalática/Portões do Universo"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence1 == "" or pertence1 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence1 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence1 == ""):
                                        spacecoins2 -= preco
                                        pertence1 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==2):
                        casaNome2 = "- Base Interplanetária de Vênus"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence2 == "" or pertence2 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence2 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence2 == ""):
                                        spacecoins2 -= preco
                                        pertence2 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==3):
                        casaNome2 = "- Base Interplanetária da Terra"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence3 == "" or pertence3 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence3 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence3 == ""):
                                        spacecoins2 -= preco
                                        pertence3 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==4):
                        casaNome2 = "- Base Interplanetária de Marte"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence4 == "" or pertence4 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence4 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence4 == ""):
                                        spacecoins2 -= preco
                                        pertence4 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==5):
                        casaNome2 = "- Base Interplanetária de Júpiter"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence5 == "" or pertence5 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence5 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence5 == ""):
                                        spacecoins2 -= preco
                                        pertence5 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==6):
                        casaNome2 = "- Base Interplanetária de Saturno"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence6 == "" or pertence6 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence6 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence6 == ""):
                                        spacecoins2 -= preco
                                        pertence6 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==7):
                        casaNome2 = "- Prisão Univeral/Passagem de Visitantes"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence7 == "" or pertence7 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence7 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence7 == ""):
                                        spacecoins2 -= preco
                                        pertence7 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==8):
                        casaNome2 = "- Base Lunar da Terra"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence8 == "" or pertence8 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence8 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence8 == ""):
                                        spacecoins2 -= preco
                                        pertence8 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==9):
                        casaNome2  = "- Base Lunar de Fobos"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence9 == "" or pertence9 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence9 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence9 == ""):
                                        spacecoins2 -= preco
                                        pertence9 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==10):
                        casaNome2 = "- Base Lunar Europa"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence10 == "" or pertence10 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence10 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence10 == ""):
                                        spacecoins2 -= preco
                                        pertence10 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==11):
                        casaNome2 = "- Base Lunar de Pandora"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence11 == "" or pertence11 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence11 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence11 == ""):
                                        spacecoins2 -= preco
                                        pertence11 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==12):
                        casaNome2 = "- Base Lunar de Talassa"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence12 == "" or pertence12 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence12 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence12 == ""):
                                        spacecoins2 -= preco
                                        pertence12 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==13):
                        casaNome2 = "- Satélite da sorte: JACKPOT"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence13 == "" or pertence13 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence13 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence13 == ""):
                                        spacecoins2 -= preco
                                        pertence13 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==14):
                        casaNome2 = "- Planeta anão: Plutão"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence14 == "" or pertence14 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence14 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence14 == ""):
                                        spacecoins2 -= preco
                                        pertence14 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==15):
                        casaNome2 = "- Planeta anão: Éris"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence15 == "" or pertence15 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence15 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence15 == ""):
                                        spacecoins2 -= preco
                                        pertence15 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==16):
                        casaNome2 = "- Planeta anão: Haumea"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence16 == "" or pertence16 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence16 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence16 == ""):
                                        spacecoins2 -= preco
                                        pertence16 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==17):
                        casaNome2 = "- Planeta anão: Ceres"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence17 == "" or pertence17 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence17 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence17 == ""):
                                        spacecoins2 -= preco
                                        pertence17 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==18):
                        casaNome2 = "- Planeta anão: Makemake"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence18 == "" or pertence18 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence18 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence18 == ""):
                                        spacecoins2 -= preco
                                        pertence18 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==19):
                        casaNome2 = "- Vá para a prisão universal!"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence19 == "" or pertence19 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence19 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence19 == ""):
                                        spacecoins2 -= preco
                                        pertence19 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==20):
                        casaNome2 = "- Base extra-solar Gliese 581 d"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence20 == "" or pertence20 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence20 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence20 == ""):
                                        spacecoins2 -= preco
                                        pertence20 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==21):
                        casaNome2 = "- Base extra-solar Upsilon Andromedae"
                        preco = 450
                        aluguel = 45
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence21 == "" or pertence21 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence21 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence21 == ""):
                                        spacecoins2 -= preco
                                        pertence21 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==22):
                        casaNome2 = "- Base extra-solar X0-3b"
                        preco = 600
                        aluguel = 60
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence22 == "" or pertence22 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence22 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence22 == ""):
                                        spacecoins2 -= preco
                                        pertence22 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==23):
                        casaNome2 = "- Base extra-solar C0R0T-Exo-1b"
                        preco = 250
                        aluguel = 25
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence23 == "" or pertence23 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence23 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence23 == ""):
                                        spacecoins2 -= preco
                                        pertence23 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2==24):
                        casaNome2 = "- Imposto espacial"
                        preco = 0
                        aluguel = 0
                        print("Você caiu na posição:", posicao2, casaNome2)
                        if (pertence24 == "" or pertence24 == nome2):
                            print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                            comprar = input()
                            if (comprar == "sim"):
                                if (preco != 0):
                                    if (pertence24 == nome2):
                                        print("Esse território já é seu")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                    elif (pertence24 == ""):
                                        spacecoins2 -= preco
                                        pertence24 = nome2
                                        print("Território adquirido")
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Este terreno não pode ser comprado")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            else:
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()
                        else:
                            print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                            spacecoins2 -= aluguel
                            print("Agora você possui", spacecoins2, "Spacecoins")
                            while (jogar != "encerrar"):
                                print("Digite encerrar para encerrar sua jogada")
                                jogar = input()
                    elif(posicao2>24):
                        posicao2 = 1

        elif(i==2):
            print()
            print(nome3, "sua vez de jogar")
            jogar = ""
            while (jogar != "jogar"):
                print()
                print(nome3, ", digite:")
                print("1 - Para saber sua posição na galáxia")
                print("2 - Para saber quantos Spacecoins possui")
                print("3 - Para ver seus territórios comprados")
                print("jogar - Para jogar os dados")
                jogada = input()
                if (jogada == "1"):
                    print("Posição:", posicao3,casaNome3)
                elif (jogada == "2"):
                    print("Spacecoins:", spacecoins3)
                elif (jogada == "3"):
                    print()
                elif (jogada == "jogar" or jogada == "Jogar"):
                    dado = random.randint(1, 6)
                    posicao3 += dado
                    if (posicao3==1):
                        casaNome3 = "- Fronteira Intergalática/Portões do Universo"
                        preco = 0
                        aluguel = 0
                    elif(posicao3==2):
                        casaNome3 = "- Base Interplanetária de Vênus"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==3):
                        casaNome3 = "- Base Interplanetária da Terra"
                        preco = 600
                        aluguel = 60
                    elif(posicao3==4):
                        casaNome3 = "- Base Interplanetária de Marte"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==5):
                        casaNome3 = "- Base Interplanetária de Júpiter"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==6):
                        casaNome3 = "- Base Interplanetária de Saturno"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==7):
                        casaNome3 = "- Prisão Univeral/Passagem de Visitantes"
                        preco = 0
                        aluguel = 0
                    elif(posicao3==8):
                        casaNome3 = "- Base Lunar da Terra"
                        preco = 600
                        aluguel = 60
                    elif(posicao3==9):
                        casaNome3  = "- Base Lunar de Fobos"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==10):
                        casaNome3 = "- Base Lunar Europa"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==11):
                        casaNome3 = "- Base Lunar de Pandora"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==12):
                        casaNome3 = "- Base Lunar de Talassa"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==13):
                        casaNome3 = "- Satélite da sorte: JACKPOT"
                        preco = 0
                        aluguel = 0
                    elif(posicao3==14):
                        casaNome3 = "- Planeta anão: Plutão"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==15):
                        casaNome3 = "- Planeta anão: Éris"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==16):
                        casaNome3 = "- Planeta anão: Haumea"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==17):
                        casaNome3 = "- Planeta anão: Ceres"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==18):
                        casaNome3 = "- Planeta anão: Makemake"
                        preco = 600
                        aluguel = 60
                    elif(posicao3==19):
                        casaNome3 = "- Vá para a prisão universal!"
                        preco = 0
                        aluguel = 0
                    elif(posicao3==20):
                        casaNome3 = "- Base extra-solar Gliese 581 d"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==21):
                        casaNome3 = "- Base extra-solar Upsilon Andromedae"
                        preco = 450
                        aluguel = 45
                    elif(posicao3==22):
                        casaNome3 = "- Base extra-solar X0-3b"
                        preco = 600
                        aluguel = 60
                    elif(posicao3==23):
                        casaNome3 = "- Base extra-solar C0R0T-Exo-1b"
                        preco = 250
                        aluguel = 25
                    elif(posicao3==24):
                        casaNome3 = "- Imposto espacial"
                        preco = 0
                        aluguel = 0
                    elif(posicao3>24):
                        posicao3 = 1
                    print("Você caiu na posição:", posicao3,casaNome3)
                    jogar = "jogar"
        elif(i==3):
            print()
            print(nome4, "sua vez de jogar")
            jogar = ""
            while (jogar != "jogar"):
                print()
                print(nome4, ", digite:")
                print("1 - Para saber sua posição na galáxia")
                print("2 - Para saber quantos Spacecoins possui")
                print("3 - Para ver seus territórios comprados")
                print("jogar - Para jogar os dados")
                jogada = input()
                if (jogada == "1"):
                    print("Posição:", posicao4,casaNome4)
                elif (jogada == "2"):
                    print("Spacecoins:", spacecoins4)
                elif (jogada == "3"):
                    print()
                elif (jogada == "jogar" or jogada == "Jogar"):
                    dado = random.randint(1, 6)
                    posicao4 += dado
                    if (posicao4==1):
                        casaNome4 = "- Fronteira Intergalática/Portões do Universo"
                        preco = 0
                        aluguel = 0
                    elif(posicao4==2):
                        casaNome4 = "- Base Interplanetária de Vênus"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==3):
                        casaNome4 = "- Base Interplanetária da Terra"
                        preco = 600
                        aluguel = 60
                    elif(posicao4==4):
                        casaNome4 = "- Base Interplanetária de Marte"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==5):
                        casaNome4 = "- Base Interplanetária de Júpiter"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==6):
                        casaNome4 = "- Base Interplanetária de Saturno"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==7):
                        casaNome4 = "- Prisão Univeral/Passagem de Visitantes"
                        preco = 0
                        aluguel = 0
                    elif(posicao4==8):
                        casaNome4 = "- Base Lunar da Terra"
                        preco = 600
                        aluguel = 60
                    elif(posicao4==9):
                        casaNome4  = "- Base Lunar de Fobos"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==10):
                        casaNome4 = "- Base Lunar Europa"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==11):
                        casaNome4 = "- Base Lunar de Pandora"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==12):
                        casaNome4 = "- Base Lunar de Talassa"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==13):
                        casaNome4 = "- Satélite da sorte: JACKPOT"
                        preco = 0
                        aluguel = 0
                    elif(posicao4==14):
                        casaNome4 = "- Planeta anão: Plutão"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==15):
                        casaNome4 = "- Planeta anão: Éris"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==16):
                        casaNome4 = "- Planeta anão: Haumea"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==17):
                        casaNome4 = "- Planeta anão: Ceres"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==18):
                        casaNome4 = "- Planeta anão: Makemake"
                        preco = 600
                        aluguel = 60
                    elif(posicao4==19):
                        casaNome4 = "- Vá para a prisão universal!"
                        preco = 0
                        aluguel = 0
                    elif(posicao4==20):
                        casaNome4 = "- Base extra-solar Gliese 581 d"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==21):
                        casaNome4 = "- Base extra-solar Upsilon Andromedae"
                        preco = 450
                        aluguel = 45
                    elif(posicao4==22):
                        casaNome4 = "- Base extra-solar X0-3b"
                        preco = 600
                        aluguel = 60
                    elif(posicao4==23):
                        casaNome4 = "- Base extra-solar C0R0T-Exo-1b"
                        preco = 250
                        aluguel = 25
                    elif(posicao4==24):
                        casaNome4 = "- Imposto espacial"
                        preco = 0
                        aluguel = 0
                    elif(posicao4>24):
                        posicao4 = 1
                    print("Você caiu na posição:", posicao4,casaNome4)
                    jogar = "jogar"
        elif(i==4):
            print()
            print(nome5, "sua vez de jogar")
            jogar = ""
            while (jogar != "jogar"):
                print()
                print(nome5, ", digite:")
                print("1 - Para saber sua posição na galáxia")
                print("2 - Para saber quantos Spacecoins possui")
                print("3 - Para ver seus territórios comprados")
                print("jogar - Para jogar os dados")
                jogada = input()
                if (jogada == "1"):
                    print("Posição:", posicao5,casaNome5)
                elif (jogada == "2"):
                    print("Spacecoins:", spacecoins5)
                elif (jogada == "3"):
                    print()
                elif (jogada == "jogar" or jogada == "Jogar"):
                    dado = random.randint(1, 6)
                    posicao5 += dado
                    if (posicao5==1):
                        casaNome5 = "- Fronteira Intergalática/Portões do Universo"
                        preco = 0
                        aluguel = 0
                    elif(posicao5==2):
                        casaNome5 = "- Base Interplanetária de Vênus"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==3):
                        casaNome5 = "- Base Interplanetária da Terra"
                        preco = 600
                        aluguel = 60
                    elif (posicao5==4):
                        casaNome5 = "- Base Interplanetária de Marte"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==5):
                        casaNome5 = "- Base Interplanetária de Júpiter"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==6):
                        casaNome5 = "- Base Interplanetária de Saturno"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==7):
                        casaNome5 = "- Prisão Univeral/Passagem de Visitantes"
                        preco = 0
                        aluguel = 0
                    elif(posicao5==8):
                        casaNome5 = "- Base Lunar da Terra"
                        preco = 600
                        aluguel = 60
                    elif(posicao5==9):
                        casaNome5  = "- Base Lunar de Fobos"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==10):
                        casaNome5 = "- Base Lunar Europa"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==11):
                        casaNome5 = "- Base Lunar de Pandora"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==12):
                        casaNome5 = "- Base Lunar de Talassa"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==13):
                        casaNome5 = "- Satélite da sorte: JACKPOT"
                        preco = 0
                        aluguel = 0
                    elif(posicao5==14):
                        casaNome5 = "- Planeta anão: Plutão"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==15):
                        casaNome5 = "- Planeta anão: Éris"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==16):
                        casaNome5 = "- Planeta anão: Haumea"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==17):
                        casaNome5 = "- Planeta anão: Ceres"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==18):
                        casaNome5 = "- Planeta anão: Makemake"
                        preco = 600
                        aluguel = 60
                    elif(posicao5==19):
                        casaNome5 = "- Vá para a prisão universal!"
                        preco = 0
                        aluguel = 0
                    elif(posicao5==20):
                        casaNome5 = "- Base extra-solar Gliese 581 d"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==21):
                        casaNome5 = "- Base extra-solar Upsilon Andromedae"
                        preco = 450
                        aluguel = 45
                    elif(posicao5==22):
                        casaNome5 = "- Base extra-solar X0-3b"
                        preco = 600
                        aluguel = 60
                    elif(posicao5==23):
                        casaNome5 = "- Base extra-solar C0R0T-Exo-1b"
                        preco = 250
                        aluguel = 25
                    elif(posicao5==24):
                        casaNome5 = "- Imposto espacial"
                        preco = 0
                        aluguel = 0
                    elif(posicao5>24):
                        posicao5 = 1
                    print("Você caiu na posição:", posicao5,casaNome5)
                    jogar = "jogar"