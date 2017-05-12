import random

#VARIÁVEIS DO PROGRAMA
nCasas = 24 #Número de casas no tabuleiro
scInicial = 10000 #Número de Space Coins iniciais
statusJogadores = "" #Variável que mostra o estado atual  dos jogadores (0 = Livre; 1 = Preso por 1 turno; 2 = Preso por 2 turnos; 3 = Preso por 3 turnos; 4 = Falido)
spacecoins = "" #Variável que mostra a quantia de Space Coins de cada jogador, formatada com 6 espaços, possibilitando o jogador conseguir acumular até 999.999$C
casaNome = "" #Variável que mostra o nome da cada do tabuleiro
terrenos = "" #Variável que mostra os respectivos terrenos, com seu id, preço e aluguel, formatado em (00)ID, (000)Preço, (000)Aluguel
#IDs = 00 = Sem proprietário / 06 = Ponto de partida / 01~05 = Reservado a jogadores / 07 = Imposto / 08 = Vá para prisão / 09 = Prisão / 10 = Jackpot

#ARTRIBUIÇÃO DAS CASAS
casaNome = ("1 Fronteira Intergalática/Portões do Universo"+
            "2 Base Interplanetária de Vênus"+
            "3 Base Interplanetária da Terra"+
            "4 Base Interplanetária de Marte"+
            "5 Base Interplanetária de Júpiter"+
            "6 Base Interplanetária de Saturno"+
            "7 Prisão Univeral/Passagem de Visitantes"+
            "8 Base Lunar da Terra"+
            "9 Base Lunar de Fobos"+
            "10 Base Lunar Europa"+
            "11 Base Lunar de Pandora"+
            "12 Base Lunar de Talassa"+
            "13 Satélite da sorte: JACKPOT"+
            "14 Planeta anão: Plutão"+
            "15 Planeta anão: Éris"+
            "16 Planeta anão: Haumea"+
            "17 Planeta anão: Ceres"+
            "18 Planeta anão: Makemake"+
            "19 Vá para a prisão universal!"+
            "20 Base extra-solar Gliese 581 d"+
            "21 Base extra-solar Upsilon Andromedae"+
            "22 Base extra-solar X0-3b"+
            "23 Base extra-solar C0R0T-Exo-1b"+
            "24 Imposto espacial")

terrenos = ("1 06000000"+
            "2 00250025"+
            "3 00600060"+
            "4 00450045"+
            "5 00450045"+
            "6 00250025"+
            "7 09000000"+
            "8 00600060"+
            "9 00250025"+
            "10 00450045"+
            "11 00450045"+
            "12 00250025"+
            "13 10000000"+
            "14 00250025"+
            "15 00450045"+
            "16 00250025"+
            "17 00450045"+
            "18 00600060"+
            "19 08000000"+
            "20 00250025"+
            "21 00450045"+
            "22 00600060"+
            "23 00250025"+
            "24 07000000")

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
spacecoins = scInicial
gameover = False
while not gameover:
    for i in range (0, numJogadores):
        if statusJogadores[i] != "4":
            if(i==0):
                print()
                print(nome1, "sua vez de jogar")
                jogar = ""
                while(jogar != "jogar"):
                    print()
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar digite jogar")
                    jogada = input()
                    if (jogada=="1"):
                        print("Posição:" ,posicao1)
                    elif (jogada=="2"):
                        print("Spacecoins:" ,spacecoins)
                    elif (jogada=="3"):
                        print()
                    elif (jogada=="jogar" or jogada=="Jogar"):
                        dado = random.randint(1,6)
                        posicao1 += dado
                        if (posicao1==1):
                            casaNome = "Fronteira Intergalática/Portões do Universo"
                            preco = 0
                            aluguel = 0
                            compra = "Não é possível comprar"
                        elif(posicao1==2):
                            casaNome = "Base Interplanetária de Vênus"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==3):
                            casaNome = "Base Interplanetária da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==4):
                            casaNome = "Base Interplanetária de Marte"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==5):
                            casaNome = "Base Interplanetária de Júpiter"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==6):
                            casaNome = "Base Interplanetária de Saturno"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==7):
                            casaNome = "Prisão Univeral/Passagem de Visitantes"
                            preco = 0
                            aluguel = 0
                        elif(posicao1==8):
                            casaNome = "Base Lunar da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==9):
                            casaNome  = "Base Lunar de Fobos"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==10):
                            casaNome = "Base Lunar Europa"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==11):
                            casaNome = "Base Lunar de Pandora"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==12):
                            casaNome = "Base Lunar de Talassa"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==13):
                            casaNome = "Satélite da sorte: JACKPOT"
                            preco = 0
                            aluguel = 0
                        elif(posicao1==14):
                            casaNome = "Planeta anão: Plutão"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==15):
                            casaNome = "Planeta anão: Éris"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==16):
                            casaNome = "Planeta anão: Haumea"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==17):
                            casaNome = "Planeta anão: Ceres"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==18):
                            casaNome = "Planeta anão: Makemake"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==19):
                            casaNome = "Vá para a prisão universal!"
                            preco = 0
                            aluguel = 0
                        elif(posicao1==20):
                            casaNome = "Base extra-solar Gliese 581 d"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==21):
                            casaNome = "Base extra-solar Upsilon Andromedae"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==22):
                            casaNome = "Base extra-solar X0-3b"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==23):
                            casaNome = "Base extra-solar C0R0T-Exo-1b"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==24):
                            casaNome = "Imposto espacial"
                            preco = 0
                            aluguel = 0
                        jogar = "jogar"
            elif(i==1):
                print()
                print(nome2, "sua vez de jogar")
                jogar = ""
                while(jogar != "jogar"):
                    print()
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada=="1"):
                        print("Posição:" ,posicao2)
                    elif(jogada=="2"):
                        print("Spacecoins:" ,spacecoins)
                    elif(jogada=="3"):
                        print()
                    elif(jogada=="jogar" or jogada=="Jogar"):
                        dado = random.randint(1,6)
                        posicao2 += dado
                        jogar = "jogar"
            elif(i==2):
                print()
                print(nome3, "sua vez de jogar")
                jogar = ""
                while (jogar != "jogar"):
                    print()
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada == "1"):
                        print("Posição:", posicao3)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao3 += dado
                        jogar = "jogar"
            elif(i==3):
                print()
                print(nome4, "sua vez de jogar")
                jogar = ""
                while (jogar != "jogar"):
                    print()
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada == "1"):
                        print("Posição:", posicao4)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao4 += dado
                        jogar = "jogar"
            elif(i==4):
                print()
                print(nome5, "sua vez de jogar")
                jogar = ""
                while (jogar != "jogar"):
                    print()
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada == "1"):
                        print("Posição:", posicao5)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao5 += dado
                        jogar = "jogar"