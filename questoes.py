s = transforma_base(quest)
pular = 3
pular1 = 1
ajuda = 2
dinheiro = 0
sort = []
opcresp = ["A", "B", "C", "D"]
opcresp1 = ["A", "B", "C", "D","PULAR", "AJUDA", "PARAR"]
fcil = 0
mdio = 0
dficil = 0
t = "notcotn"
fir = 0
fir1 = 0
per2 = 0
per3 = 0
per4 = 0
per5 = 0
per6 = 0
per7 = 0
per8 = 0
per9 = 0
import colorama
from colorama import Fore
#instrutuceos
#jogador informa o nome
#iniciar o jogo
# 4 sorteios de perguntas
# 5 caso repsosta seja ajuda gerrar ajuda
# 6 caso resposta seja pular volte para o passo 4
#7 caso resposta seja correta aumente o premio e volte para o passo 4
#8 caso resposta seja incorreta o jogo acaba
print("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer! \n")
nome = input("Qual é o seu nome? ")

while fir != 1:
    print("Olá!", nome, "Você está na Fortuna DesSoft e terá a oportunidade de enriquecer! \n")
    print("Olá", nome, "voce tem direito de pular 3 vezes e usar 2 ajudas \n")
    print("Vamos começar! \n")
    fir1 = 0
    pular = 3
    pular1 = 1
    ajuda = 2
    dinheiro = 0
    sort = []
    per2 = 0
    per3 = 0
    per4 = 0
    per5 = 0
    per6 = 0
    per7 = 0
    per8 = 0
    per9 = 0
    x = sorteia_questao_inedida(s,'facil',sort)
    print(questao_para_texto(x,1))
    while fir1 != 1:
        resp = input(" \n Qual é a resposta? ")
        if resp.upper() == "PULAR":
            if pular > 0 and pular1 > 0:
                x = sorteia_questao_inedida(s,'facil',sort)
                print(questao_para_texto(x,1))
                resp = input(" \n Qual é a resposta? ")
                pular = pular - 1
                pular1 = pular1 - 1
                fir = 1
                fir1 = 1
            elif pular == 0:
                print("Você não tem mais pulos\n")
                print(questao_para_texto(x,1))
                resp = input(" \n Qual é a resposta? ")
                fir = 1
                fir1 = 1
            else:
                print("Voce ja pulou uma vez nessa rodada\n")
        if resp.upper() == "AJUDA":
            
            if ajuda > 0:
                ajuda = ajuda - 1
                print("Você tem", ajuda, "ajudas")
                print(gera_ajuda(x))
                resp = input(" \n Qual é a resposta? ")
                fir = 1
                fir1 =1
            else:
                print("Você não tem mais ajudas\n")
                print(questao_para_texto(x,1))
                resp = input(" \n Qual é a resposta? ")
                fir = 1
                fir1 =1
        if resp.upper() == "PULAR":
            if pular > 0:
                x = sorteia_questao_inedida(s,'facil',sort)
                print(questao_para_texto(x,1))
                resp = input(" \n Qual é a resposta? ")
                pular = pular - 1
                fir = 1
                fir1 = 1
            else:
                print("Você não tem mais pulos\n")
                print(questao_para_texto(x,1))
                resp = input(" \n Qual é a resposta? ")
                fir = 1
                fir1 = 1
        if resp.upper() == x['correta']:
            print("Você acertou! \n")
            dinheiro = 1000
            print("Você tem", dinheiro, "reais \n")
            fir = 1
            fir1 = 1
            per2 = 1
        elif resp.upper() in opcresp:
            print("Você errou! \n")
            print("Você não ganhou nada \n")
            contin = input("Deseja continuar? S/N ")
            if contin.upper() == "S":
                fir = 0
                fir1 = 1
            else:
                fir = 0
                fir1 = 0
        if resp.upper() not in opcresp1:
            print("opcao invalida tente novamente! \n")
            fir = 1
            fir1 = 0
    if per2 == 1:
        fir = 0
        fir1 = 0
        x = sorteia_questao_inedida(s,'facil',sort)
        print(questao_para_texto(x,2))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'medio',sort)
                    print(questao_para_texto(x,2))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,2))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
                else:
                    print("Voce ja pulou uma vez nessa rodada\n")
            if resp.upper() == "AJUDA":
                    
                if ajuda > 0:
                    ajuda = ajuda - 1
                    print("Você tem", ajuda, "ajudas")
                    print(gera_ajuda(x))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
                else:
                    print("Você não tem mais ajudas\n")
                    print(questao_para_texto(x,2))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'medio',sort)
                    print(questao_para_texto(x,2))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,2))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 5000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per3 = 1
            elif resp.upper() == 'PARAR':
                print("voce ganhaou {0} reais \n".format(dinheiro))
                fir = 0
                fir1 = 0
                contin = input("Deseja jogar novamente? S/N ")
                if contin.upper() == "S":
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
                
            elif resp.upper() in opcresp:
                print("Você errou! \n")
                print("Você não ganhou nada \n")
                contin = input("Deseja continuar? S/N ")
                if contin.upper() == "S":
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
            if resp.upper() not in opcresp1:
                print("opcao invalida tente novamente! \n")
                fir = 1
                fir1 =0

    if per3 == 1:
        fir = 0
        fir1 = 0
        
        x = sorteia_questao_inedida(s,'facil',sort)
        print(questao_para_texto(x,3))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'facil',sort)
                    print(questao_para_texto(x,3))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,3))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
                else:
                    print("Voce ja pulou uma vez nessa rodada\n")
            if resp.upper() == "AJUDA":
                    
                if ajuda > 0:
                    ajuda = ajuda - 1
                    print("Você tem", ajuda, "ajudas")
                    print(gera_ajuda(x))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
                else:
                    print("Você não tem mais ajudas\n")
                    print(questao_para_texto(x,3))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'facil',sort)
                    print(questao_para_texto(x,3))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,3))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 10000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per4 = 1
            elif resp.upper() == 'PARAR':
                print("voce ganhaou {0} reais \n".format(dinheiro))
                fir = 0
                fir1 = 0
                contin = input("Deseja jogar novamente? S/N ")
                if contin.upper() == "S":
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
            elif resp.upper() in opcresp1:
                print("Você errou! \n")
                print("Você não ganhou nada \n")
                contin = input("Deseja continuar? S/N ")
                if contin.upper() == "S":
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
            if resp.upper() not in opcresp1:
                print("opcao invalida tente novamente! \n")
                fir = 1
                fir1 = 0
    if per4 == 1:
        print("Parabens voce ganhou avancou para o nivel medio")
        fir = 0
        fir1 = 0
        
        x = sorteia_questao_inedida(s,'medio',sort)
        print(questao_para_texto(x,4))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'medio',sort)
                    print(questao_para_texto(x,4))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,4))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
                else:
                    print("Voce ja pulou uma vez nessa rodada\n")
            if resp.upper() == "AJUDA":
                    
                if ajuda > 0:
                    ajuda = ajuda - 1
                    print("Você tem", ajuda, "ajudas")
                    print(gera_ajuda(x))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
                else:
                    print("Você não tem mais ajudas\n")
                    print(questao_para_texto(x,4))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'medio',sort)
                    print(questao_para_texto(x,4))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,4))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 30000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per5 = 1
            elif resp.upper() == 'PARAR':
                print("voce ganhaou {0} reais \n".format(dinheiro))
                fir = 0
                fir1 = 0
                contin = input("Deseja jogar novamente? S/N ")
                if contin.upper() == "S":
                    
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
            elif resp.upper() in opcresp1:
            
                print("Você errou! \n")
                print("Você não ganhou nada \n")
                contin = input("Deseja continuar? S/N ")
                if contin.upper() == "S":
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
            if resp.upper() not in opcresp1:
                print("opcao invalida tente novamente! \n")
                fir = 1
                fir1 = 0