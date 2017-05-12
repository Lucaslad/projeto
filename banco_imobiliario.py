import random

#VARIÁVEIS DO PROGRAMA
nCasas = 24 #Número de casas no tabuleiro
scInicial = 10000 #Número de Space Coins iniciais
statusJogadores = "" #Variável que mostra o estado atual  dos jogadores (0 = Livre; 1 = Preso por 1 turno; 2 = Preso por 2 turnos; 3 = Preso por 3 turnos; 4 = Falido)
posicaoJogadores = "" #Variável que mostra a posição dos jogadores no tabuleiro (de 0 = ponto inicial, até 24 = ultima casa)
spacecoins = "" #Variável que mostra a quantia de Space Coins de cada jogador, formatada com 6 espaços, possibilitando o jogador conseguir acumular até 999.999$C
casaNome = "" #Variável que mostra o nome da cada do tabuleiro
terrenos = "" #Variável que mostra os respectivos terrenos, com seu id, preço e aluguel, formatado em (00)ID, (000)Preço, (000)Aluguel
#IDs = 00 = Sem proprietário / 06 = Ponto de partida / 01~05 = Reservado a jogadores / 07 = Imposto / 08 = Vá para prisão / 09 = Prisão / 10 = Jackpot

#ARTRIBUIÇÃO DAS CASAS
casaNome = ("Fronteira Intergalática/Portões do Universo"+
            "Base Interplanetária de Vênus"+
            "Base Interplanetária da Terra"+
            "Base Interplanetária de Marte"+
            "Base Interplanetária de Júpiter"+
            "Base Interplanetária de Saturno"+
            "Prisão Univeral/Passagem de Visitantes"+
            "Base Lunar da Terra"+
            "Base Lunar de Fobos"+
            "Base Lunar Europa"+
            "Base Lunar de Pandora"+
            "Base Lunar de Talassa"+
            "Satélite da sorte: JACKPOT"+
            "Planeta anão: Plutão"+
            "Planeta anão: Éris"+
            "Planeta anão: Haumea"+
            "Planeta anão: Ceres"+
            "Planeta anão: Makemake"+
            "Vá para a prisão universal!"+
            "Base extra-solar Gliese 581 d"+
            "Base extra-solar Upsilon Andromedae"+
            "Base extra-solar X0-3b"+
            "Base extra-solar C0R0T-Exo-1b"+
            "Imposto espacial")

terrenos = ("06000000"+
            "00250025"+
            "00600060"+
            "00450045"+
            "00450045"+
            "00250025"+
            "09000000"+
            "00600060"+
            "00250025"+
            "00450045"+
            "00450045"+
            "00250025"+
            "10000000"+
            "00250025"+
            "00450045"+
            "00250025"+
            "00450045"+
            "00600060"+
            "08000000"+
            "00250025"+
            "00450045"+
            "00600060"+
            "00250025"+
            "07000000")

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
statusJogadores = "00000"
posicaoJogadores = "0000000000"
spacecoins = scInicial
gameover = False
while not gameover:
    for i in range (0, numJogadores):
        if statusJogadores[i] != "4":
            if(i==0):
                print(nome1, "sua vez de jogar")
                jogar = ""
                while(jogar != "jogar"):
                    posicao = int(posicaoJogadores[(i * 2):((i * 2) + 2)])
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar digite jogar")
                    jogada = input()
                    if (jogada=="1"):
                        print("Posição:" ,posicao)
                    elif (jogada=="2"):
                        print("Spacecoins:" ,spacecoins)
                    elif (jogada=="3"):
                        print()
                    elif (jogada=="jogar" or jogada=="Jogar"):
                        dado = random.randint(1,6)
                        posicao += dado
                        jogar = "jogar"
            elif(i==1):
                print(nome2, "sua vez de jogar")
                jogar = ""
                while(jogar != "jogar"):
                    posicao = int(posicaoJogadores[(i * 2):((i * 2) + 2)])
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada=="1"):
                        print("Posição:" ,posicao)
                    elif(jogada=="2"):
                        print("Spacecoins:" ,spacecoins)
                    elif(jogada=="3"):
                        print()
                    elif(jogada=="jogar" or jogada=="Jogar"):
                        dado = random.randint(1,6)
                        posicao += dado
                        jogar = "jogar"
            elif(i==2):
                print(nome3, "sua vez de jogar")
                jogar = ""
                while (jogar != "jogar"):
                    posicao = int(posicaoJogadores[(i * 2):((i * 2) + 2)])
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada == "1"):
                        print("Posição:", posicao)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao += dado
                        jogar = "jogar"
            elif(i==3):
                print(nome4, "sua vez de jogar")
                jogar = ""
                while (jogar != "jogar"):
                    posicao = int(posicaoJogadores[(i * 2):((i * 2) + 2)])
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada == "1"):
                        print("Posição:", posicao)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao += dado
                        jogar = "jogar"
            elif(i==4):
                print(nome5, "sua vez de jogar")
                jogar = ""
                while (jogar != "jogar"):
                    posicao = int(posicaoJogadores[(i * 2):((i * 2) + 2)])
                    print("Para saber sua posição na galaxia digite 1")
                    print("Para saber quantos spacecoins você tem digite 2")
                    print("Para ver seus territórios digite 3")
                    print("Para jogar os dados digite jogar")
                    jogada = input()
                    if (jogada == "1"):
                        print("Posição:", posicao)
                    elif (jogada == "2"):
                        print("Spacecoins:", spacecoins)
                    elif (jogada == "3"):
                        print()
                    elif (jogada == "jogar" or jogada == "Jogar"):
                        dado = random.randint(1, 6)
                        posicao += dado
                        jogar = "jogar"