import random
import colorama
from colorama import Fore

from FUNCOES import *
quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

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
    print(Fore.RED + questao_para_texto(x,1))
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
        print(Fore.RED + questao_para_texto(x,2))
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
        print(Fore.RED + questao_para_texto(x,3))
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
        print(Fore.BLUE + questao_para_texto(x,4))
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
    if per5 == 1:
        fir = 0
        fir1 = 0
        x = sorteia_questao_inedida(s,'medio',sort)
        print(Fore.BLUE + questao_para_texto(x,5))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'medio',sort)
                    print(questao_para_texto(x,5))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,5))
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
                    print(questao_para_texto(x,5))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'medio',sort)
                    print(questao_para_texto(x,5))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,5))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 50000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per6 = 1
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
    if per6 == 1:
        print("parabens voce avancou para a fase dificil")
        fir = 0
        fir1 = 0
        x = sorteia_questao_inedida(s,'dificil',sort)
        print(Fore.GREEN + questao_para_texto(x,6))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,6))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,6))
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
                    print(questao_para_texto(x,6))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,6))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,6))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 100000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per7 = 1
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
    if per7 == 1:
        fir = 0
        fir1 = 0
        x = sorteia_questao_inedida(s,'dificil',sort)
        print(Fore.GREEN + questao_para_texto(x,7))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,7))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,7))
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
                    print(questao_para_texto(x,7))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,7))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,7))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 200000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per8 = 1
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
    if per8 == 1:
        fir = 0
        fir1 = 0
        x = sorteia_questao_inedida(s,'dificil',sort)
        print(Fore.GREEN + questao_para_texto(x,8))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,8))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,8))
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
                    print(questao_para_texto(x,8))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,8))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,8))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                dinheiro = 500000
                print("Você tem", dinheiro, "reais \n")
                fir = 1
                fir1 = 1
                per9 = 1
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
    if per9 == 1:
        fir = 0
        fir1 = 0
        x = sorteia_questao_inedida(s,'dificil',sort)
        print(Fore.GREEN + questao_para_texto(x,9))
        while fir1 != 1:
            resp = input(" \n Qual é a resposta? ")
            if resp.upper() == "PULAR":
                if pular > 0 and pular1 > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,9))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    pular1 = pular1 - 1
                    fir = 1
                    fir1 = 1
                elif pular == 0:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,9))
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
                    print(questao_para_texto(x,9))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 =1
            if resp.upper() == "PULAR":
                if pular > 0:
                    x = sorteia_questao_inedida(s,'dificil',sort)
                    print(questao_para_texto(x,9))
                    resp = input(" \n Qual é a resposta? ")
                    pular = pular - 1
                    fir = 1
                    fir1 = 1
                else:
                    print("Você não tem mais pulos\n")
                    print(questao_para_texto(x,9))
                    resp = input(" \n Qual é a resposta? ")
                    fir = 1
                    fir1 = 1
            if resp.upper() == x['correta']:
                print("Você acertou! \n")
                print("voce ganhou o jogo \n")
                dinheiro = 1000000
                print("Você tem", dinheiro, "reais \n")
                cont = input("Deseja jogar novamente? S/N ")
                if cont.upper() == "S":
                    fir = 0
                    fir1 = 1
                else:
                    fir = 0
                    fir1 = 0
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