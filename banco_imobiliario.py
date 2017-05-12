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
casaNome1 = ""
casaNome2 = ""
casaNome3 = ""
casaNome4 = ""
casaNome5 = ""
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
                    print("Digite:")
                    print("1 - Para saber sua posição na galáxia")
                    print("2 - Para saber quantos Spacecoins possui")
                    print("3 - Para ver seus territórios comprados")
                    print("jogar - Para jogar")
                    jogada = input()
                    if (jogada=="1"):
                        print("Posição:" ,posicao1, casaNome1)
                    elif (jogada=="2"):
                        print("Spacecoins:" ,spacecoins)
                    elif (jogada=="3"):
                        print()
                    elif (jogada=="jogar" or jogada=="Jogar"):
                        dado = random.randint(1,6)
                        posicao1 += dado
                        if (posicao1==1):
                            casaNome1 = "Fronteira Intergalática/Portões do Universo"
                            preco = 0
                            aluguel = 0
                            compra = "Não é possível comprar"
                        elif(posicao1==2):
                            casaNome1 = "Base Interplanetária de Vênus"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==3):
                            casaNome1 = "Base Interplanetária da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==4):
                            casaNome1 = "Base Interplanetária de Marte"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==5):
                            casaNome1 = "Base Interplanetária de Júpiter"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==6):
                            casaNome1 = "Base Interplanetária de Saturno"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==7):
                            casaNome1 = "Prisão Univeral/Passagem de Visitantes"
                            preco = 0
                            aluguel = 0
                        elif(posicao1==8):
                            casaNome1 = "Base Lunar da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==9):
                            casaNome1  = "Base Lunar de Fobos"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==10):
                            casaNome1 = "Base Lunar Europa"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==11):
                            casaNome1 = "Base Lunar de Pandora"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==12):
                            casaNome1 = "Base Lunar de Talassa"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==13):
                            casaNome1 = "Satélite da sorte: JACKPOT"
                            preco = 0
                            aluguel = 0
                        elif(posicao1==14):
                            casaNome1 = "Planeta anão: Plutão"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==15):
                            casaNome1 = "Planeta anão: Éris"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==16):
                            casaNome1 = "Planeta anão: Haumea"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==17):
                            casaNome1 = "Planeta anão: Ceres"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==18):
                            casaNome1 = "Planeta anão: Makemake"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==19):
                            casaNome1 = "Vá para a prisão universal!"
                            preco = 0
                            aluguel = 0
                        elif(posicao1==20):
                            casaNome1 = "Base extra-solar Gliese 581 d"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==21):
                            casaNome1 = "Base extra-solar Upsilon Andromedae"
                            preco = 450
                            aluguel = 45
                        elif(posicao1==22):
                            casaNome1 = "Base extra-solar X0-3b"
                            preco = 600
                            aluguel = 60
                        elif(posicao1==23):
                            casaNome1 = "Base extra-solar C0R0T-Exo-1b"
                            preco = 250
                            aluguel = 25
                        elif(posicao1==24):
                            casaNome1 = "Imposto espacial"
                            preco = 0
                            aluguel = 0
                        elif(posicao1>24):
                            posicao1 = 1
                        jogar = "jogar"
            elif(i==1):
                print()
                print(nome2, "sua vez de jogar")
                jogar = ""
                while(jogar != "jogar"):
                    print()
                    print("Digite:")
                    print("1 - Para saber sua posição na galáxia")
                    print("2 - Para saber quantos Spacecoins possui")
                    print("3 - Para ver seus territórios comprados")
                    print("jogar - Para jogar")
                    jogada = input()
                    if (jogada=="1"):
                        print("Posição:" ,posicao2, casaNome2)
                    elif(jogada=="2"):
                        print("Spacecoins:" ,spacecoins)
                    elif(jogada=="3"):
                        print()
                    elif(jogada=="jogar" or jogada=="Jogar"):
                        dado = random.randint(1,6)
                        posicao2 += dado
                        if (posicao2==1):
                            casaNome2 = "Fronteira Intergalática/Portões do Universo"
                            preco = 0
                            aluguel = 0
                            compra = "Não é possível comprar"
                        elif(posicao2==2):
                            casaNome2 = "Base Interplanetária de Vênus"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==3):
                            casaNome2 = "Base Interplanetária da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao2==4):
                            casaNome2 = "Base Interplanetária de Marte"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==5):
                            casaNome2 = "Base Interplanetária de Júpiter"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==6):
                            casaNome2 = "Base Interplanetária de Saturno"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==7):
                            casaNome2 = "Prisão Univeral/Passagem de Visitantes"
                            preco = 0
                            aluguel = 0
                        elif(posicao2==8):
                            casaNome2 = "Base Lunar da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao2==9):
                            casaNome2  = "Base Lunar de Fobos"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==10):
                            casaNome2 = "Base Lunar Europa"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==11):
                            casaNome2 = "Base Lunar de Pandora"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==12):
                            casaNome2 = "Base Lunar de Talassa"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==13):
                            casaNome2 = "Satélite da sorte: JACKPOT"
                            preco = 0
                            aluguel = 0
                        elif(posicao2==14):
                            casaNome2 = "Planeta anão: Plutão"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==15):
                            casaNome2 = "Planeta anão: Éris"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==16):
                            casaNome2 = "Planeta anão: Haumea"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==17):
                            casaNome2 = "Planeta anão: Ceres"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==18):
                            casaNome2 = "Planeta anão: Makemake"
                            preco = 600
                            aluguel = 60
                        elif(posicao2==19):
                            casaNome2 = "Vá para a prisão universal!"
                            preco = 0
                            aluguel = 0
                        elif(posicao2==20):
                            casaNome2 = "Base extra-solar Gliese 581 d"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==21):
                            casaNome2 = "Base extra-solar Upsilon Andromedae"
                            preco = 450
                            aluguel = 45
                        elif(posicao2==22):
                            casaNome2 = "Base extra-solar X0-3b"
                            preco = 600
                            aluguel = 60
                        elif(posicao2==23):
                            casaNome2 = "Base extra-solar C0R0T-Exo-1b"
                            preco = 250
                            aluguel = 25
                        elif(posicao2==24):
                            casaNome2 = "Imposto espacial"
                            preco = 0
                            aluguel = 0
                        elif(posicao2>24):
                            posicao2 = 1
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
                        print("Posição:", posicao3, casaNome3)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao3 += dado
                        if (posicao3==1):
                            casaNome3 = "Fronteira Intergalática/Portões do Universo"
                            preco = 0
                            aluguel = 0
                            compra = "Não é possível comprar"
                        elif(posicao3==2):
                            casaNome3 = "Base Interplanetária de Vênus"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==3):
                            casaNome3 = "Base Interplanetária da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao3==4):
                            casaNome3 = "Base Interplanetária de Marte"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==5):
                            casaNome3 = "Base Interplanetária de Júpiter"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==6):
                            casaNome3 = "Base Interplanetária de Saturno"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==7):
                            casaNome3 = "Prisão Univeral/Passagem de Visitantes"
                            preco = 0
                            aluguel = 0
                        elif(posicao3==8):
                            casaNome3 = "Base Lunar da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao3==9):
                            casaNome3  = "Base Lunar de Fobos"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==10):
                            casaNome3 = "Base Lunar Europa"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==11):
                            casaNome3 = "Base Lunar de Pandora"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==12):
                            casaNome3 = "Base Lunar de Talassa"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==13):
                            casaNome3 = "Satélite da sorte: JACKPOT"
                            preco = 0
                            aluguel = 0
                        elif(posicao3==14):
                            casaNome3 = "Planeta anão: Plutão"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==15):
                            casaNome3 = "Planeta anão: Éris"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==16):
                            casaNome3 = "Planeta anão: Haumea"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==17):
                            casaNome3 = "Planeta anão: Ceres"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==18):
                            casaNome3 = "Planeta anão: Makemake"
                            preco = 600
                            aluguel = 60
                        elif(posicao3==19):
                            casaNome3 = "Vá para a prisão universal!"
                            preco = 0
                            aluguel = 0
                        elif(posicao3==20):
                            casaNome3 = "Base extra-solar Gliese 581 d"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==21):
                            casaNome3 = "Base extra-solar Upsilon Andromedae"
                            preco = 450
                            aluguel = 45
                        elif(posicao3==22):
                            casaNome3 = "Base extra-solar X0-3b"
                            preco = 600
                            aluguel = 60
                        elif(posicao3==23):
                            casaNome3 = "Base extra-solar C0R0T-Exo-1b"
                            preco = 250
                            aluguel = 25
                        elif(posicao3==24):
                            casaNome3 = "Imposto espacial"
                            preco = 0
                            aluguel = 0
                        elif(posicao3>24):
                            posicao3 = 1
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
                        print("Posição:", posicao4, casaNome4)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao4 += dado
                        if (posicao4==1):
                            casaNome4 = "Fronteira Intergalática/Portões do Universo"
                            preco = 0
                            aluguel = 0
                            compra = "Não é possível comprar"
                        elif(posicao4==2):
                            casaNome4 = "Base Interplanetária de Vênus"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==3):
                            casaNome4 = "Base Interplanetária da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao4==4):
                            casaNome4 = "Base Interplanetária de Marte"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==5):
                            casaNome4 = "Base Interplanetária de Júpiter"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==6):
                            casaNome4 = "Base Interplanetária de Saturno"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==7):
                            casaNome4 = "Prisão Univeral/Passagem de Visitantes"
                            preco = 0
                            aluguel = 0
                        elif(posicao4==8):
                            casaNome4 = "Base Lunar da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao4==9):
                            casaNome4  = "Base Lunar de Fobos"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==10):
                            casaNome4 = "Base Lunar Europa"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==11):
                            casaNome4 = "Base Lunar de Pandora"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==12):
                            casaNome4 = "Base Lunar de Talassa"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==13):
                            casaNome4 = "Satélite da sorte: JACKPOT"
                            preco = 0
                            aluguel = 0
                        elif(posicao4==14):
                            casaNome4 = "Planeta anão: Plutão"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==15):
                            casaNome4 = "Planeta anão: Éris"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==16):
                            casaNome4 = "Planeta anão: Haumea"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==17):
                            casaNome4 = "Planeta anão: Ceres"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==18):
                            casaNome4 = "Planeta anão: Makemake"
                            preco = 600
                            aluguel = 60
                        elif(posicao4==19):
                            casaNome4 = "Vá para a prisão universal!"
                            preco = 0
                            aluguel = 0
                        elif(posicao4==20):
                            casaNome4 = "Base extra-solar Gliese 581 d"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==21):
                            casaNome4 = "Base extra-solar Upsilon Andromedae"
                            preco = 450
                            aluguel = 45
                        elif(posicao4==22):
                            casaNome4 = "Base extra-solar X0-3b"
                            preco = 600
                            aluguel = 60
                        elif(posicao4==23):
                            casaNome4 = "Base extra-solar C0R0T-Exo-1b"
                            preco = 250
                            aluguel = 25
                        elif(posicao4==24):
                            casaNome4 = "Imposto espacial"
                            preco = 0
                            aluguel = 0
                        elif(posicao4>24):
                            posicao4 = 1
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
                        print("Posição:", posicao5, casaNome5)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao5 += dado
                        if (posicao5==1):
                            casaNome5 = "Fronteira Intergalática/Portões do Universo"
                            preco = 0
                            aluguel = 0
                            compra = "Não é possível comprar"
                        elif(posicao5==2):
                            casaNome5 = "Base Interplanetária de Vênus"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==3):
                            casaNome5 = "Base Interplanetária da Terra"
                            preco = 600
                            aluguel = 60
                        elif (posicao5==4):
                            casaNome5 = "Base Interplanetária de Marte"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==5):
                            casaNome5 = "Base Interplanetária de Júpiter"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==6):
                            casaNome5 = "Base Interplanetária de Saturno"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==7):
                            casaNome5 = "Prisão Univeral/Passagem de Visitantes"
                            preco = 0
                            aluguel = 0
                        elif(posicao5==8):
                            casaNome5 = "Base Lunar da Terra"
                            preco = 600
                            aluguel = 60
                        elif(posicao5==9):
                            casaNome5  = "Base Lunar de Fobos"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==10):
                            casaNome5 = "Base Lunar Europa"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==11):
                            casaNome5 = "Base Lunar de Pandora"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==12):
                            casaNome5 = "Base Lunar de Talassa"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==13):
                            casaNome5 = "Satélite da sorte: JACKPOT"
                            preco = 0
                            aluguel = 0
                        elif(posicao5==14):
                            casaNome5 = "Planeta anão: Plutão"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==15):
                            casaNome5 = "Planeta anão: Éris"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==16):
                            casaNome5 = "Planeta anão: Haumea"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==17):
                            casaNome5 = "Planeta anão: Ceres"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==18):
                            casaNome5 = "Planeta anão: Makemake"
                            preco = 600
                            aluguel = 60
                        elif(posicao5==19):
                            casaNome5 = "Vá para a prisão universal!"
                            preco = 0
                            aluguel = 0
                        elif(posicao5==20):
                            casaNome5 = "Base extra-solar Gliese 581 d"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==21):
                            casaNome5 = "Base extra-solar Upsilon Andromedae"
                            preco = 450
                            aluguel = 45
                        elif(posicao5==22):
                            casaNome5 = "Base extra-solar X0-3b"
                            preco = 600
                            aluguel = 60
                        elif(posicao5==23):
                            casaNome5 = "Base extra-solar C0R0T-Exo-1b"
                            preco = 250
                            aluguel = 25
                        elif(posicao5==24):
                            casaNome5 = "Imposto espacial"
                            preco = 0
                            aluguel = 0
                        elif(posicao5>24):
                            posicao5 = 1
                        jogar = "jogar"