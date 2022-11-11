import random

def gera_ajuda(x):
    certa = x["correta"]
    new  = []
    for i in x['opcoes']:
        if i != certa:
            new.append(i)
    ss = random.randint(0,len(new)-1)
    qt = random.randint(1, 2)
    if qt == 1:
        s =  new[ss]
        pp = x['opcoes'][s]
        return 'DICA:\nOpções certamente erradas: {0}'.format(pp)
    if qt == 2:
        s =  new[ss]
        ss = random.randint(0,len(new)-1)
        tt = new[ss]
        pp = x['opcoes'][tt]
        ii = x['opcoes'][s]
        return 'DICA:\nOpções certamente erradas: {0} e {1}'.format(ii, pp)


def sorteia_questao(dicionario,nivel):
    #f=facilidade
    lista=[]
    lista=dicionario[nivel]
    x=random.randint(0,len(lista)-1)
    return lista[x]

def transforma_base(lista):
    lista_facil=[]
    lista_medio=[]
    lista_dificil=[]
    dicionario={}
    for i in range(0,len(lista)):
        if lista[i]['nivel']=='facil':
            lista_facil.append(lista[i])
        elif lista[i]['nivel']=='medio':
            lista_medio.append(lista[i])
        else:
            lista_dificil.append(lista[i])
    if len(lista_facil)>0:
        dicionario['facil']=lista_facil
    if len(lista_medio)>0:
        dicionario['medio']=lista_medio
    if len(lista_dificil)>0:
        dicionario['dificil']=lista_dificil
    return dicionario 

def sorteia_questao_inedida(dicionario,nivel,lista_sort):
    questao_sorteada = sorteia_questao(dicionario, nivel)
    while questao_sorteada in lista_sort:
        questao_sorteada=sorteia_questao(dicionario,nivel)
    lista_sort.append(questao_sorteada)
    return questao_sorteada

def valida_questao(dic):
    new = {}
    answer = ['A','B','C','D']
    aa = 0
    bb = 0
    cc = 0
    dd = 0

    if len(dic) != 4:
        if 'titulo' not in dic:
            new['titulo'] = 'nao_encontrado'
        if 'nivel' not in dic:
            new['nivel'] = 'nao_encontrado'
        if 'opcoes' not in dic:
            new['opcoes'] = 'nao_encontrado'
        if 'correta' not in dic:
            new['correta'] = 'nao_encontrado'
        new['outro'] = 'numero_chaves_invalido'
    if 'correta' in dic:
        if dic['correta'] not in answer:
            new['correta'] = 'valor_errado'
    if 'nivel' in dic:
        if dic['nivel'] not in ['facil','medio','dificil']:
            new['nivel'] = 'valor_errado'
    if 'titulo' in dic:
        if dic['titulo'].strip() == '':
            new['titulo'] = 'vazio'
    if 'opcoes' in dic:
        new2 = {}
        if len(dic['opcoes']) != 4:
            new['opcoes'] = 'tamanho_invalido'
        else:
            if 'A' in dic['opcoes']:
                if dic['opcoes']['A'].strip() == '':
                    new2['A'] = 'vazia'
                    aa = 1
            else:
                new2['A'] = 'nao_encontrada'
                aa = 1
            if 'B' in dic['opcoes']:
                if dic['opcoes']['B'].strip() == '':
                    new2['B'] = 'vazia'
                    bb = 1
            else:
                new2['B'] = 'nao_encontrada'
                bb = 1
            if 'C' in dic['opcoes']:
                if dic['opcoes']['C'].strip() == '':
                    new2['C'] = 'vazia'
                    cc = 1
            else:
                new2['C'] = 'nao_encontrada'
                cc = 1
            if 'D' in dic['opcoes']:
                if dic['opcoes']['D'].strip() == '':
                    new2['D'] = 'vazia'
                    dd = 1
            else:
                new2['D'] = 'nao_encontrada'
                dd = 1
            if len(new2) != 0:
                new['opcoes'] = new2
    if len(new) == 0:
        return {}
    else:
        return new

def questao_para_texto(quest,n):
    x = f'''----------------------------------------
QUESTAO {n}

{quest['titulo']}

RESPOSTAS:
A: {quest['opcoes']['A']}
B: {quest['opcoes']['B']}
C: {quest['opcoes']['C']}
D: {quest['opcoes']['D']}'''
    return x



def valida_questoes(question):
    new = []
    for i in question:
        new.append(valida_questao(i))
    return new



    

