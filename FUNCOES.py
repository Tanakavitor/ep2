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



    

