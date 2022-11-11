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
    

