# input_file : fichier texte contenant le puzzle input 

input_file = open("day18.txt", 'r') # 8298263963837 pour la partie 1 
# input_file = open("day18ex.txt", 'r') # 26 335 pour la partie 1 
myinput = input_file.read().split(sep = '\n') 


def operate(ope, mb1, mb2): 
    if ope == '*': 
        return mb1 * mb2 
    if ope == '+': 
        return mb1 + mb2 

def byeExces(exp): 
    i = 0 
    while i < len(exp) and exp[i] == ' ': 
        i += 1 
    
    j = len(exp)-1 
    while j > 0 and exp[j] == ' ': 
        j -= 1 
    
    k = 0 
    pc = 0 
    ipp, ifp = 0, 0 
    samePara = False 
    while not samePara and k < len(exp): 
        if exp[k] == '(': 
            samePara = True 
            pc += 1 
            ipp = k+1 
        k += 1 
        
    while pc != 0 and k < len(exp): 
        if exp[k] == '(': 
            pc += 1 
        elif exp[k] == ')': 
            pc -= 1 
            ifp = k-1
        k += 1 
    
    if k < len(exp) and k < j: 
        samePara = False 
    
    if not samePara: 
        # print('youhou')
        ideb = i 
        ifin = j 
    else: 
        ideb = ipp
        ifin = ifp
   
    return exp[ideb:ifin+1]

def lesMembres(exp, i_ope): 
    ideb = 0 
    pc = 0 
    i = i_ope-1 
    while i > 0 and ideb == 0: 
        if exp[i] == '(': 
            if pc == 0: 
                ideb = i 
            pc += 1 
        if exp[i] == ')': 
            pc -= 1 
        if pc == 0 and (exp[i] == '+' or exp[i] == '*'): 
            ideb = i+1
        i -= 1 
    
    n = len(exp)
    ifin = n 
    pc = 0 
    i = i_ope+1 
    while i < n and ifin == n: 
        if exp[i] == '(': 
            pc += 1 
        if exp[i] == ')': 
            if pc == 0: 
                ifin = i 
            pc -= 1 
        if pc == 0 and (exp[i] == '+' or exp[i] == '*'): 
            ifin = i-1
        i += 1 
    
    # print(i_ope, ideb, ifin)
    return ideb, i_ope, i_ope+1, ifin 

def calcul(exp): 
    
    n = len(exp)
    plus = False 
    fois = False 
    ope = plus or fois 
    
    i = 0
    iplus = 0 
    ifois = 0 
    pc = 0 
    
    while i < n and not plus: # while i < n and not ope: # pour la partie 1 
        if pc == 0: 
            if exp[i] == '+': 
                plus = True 
                iplus = i 
            elif exp[i] == '*': 
                fois = True 
                ifois = i 
                
        if exp[i] == '(': 
            pc += 1 
        if exp[i] == ')': 
            pc -= 1 
        i += 1 
        # ope = plus or fois # pour la partie 1 
    ope = plus or fois 
    
    if not ope: 
        return int(exp) 
    
    else: 
        # iope = max(ifois, iplus) # Utile pour la partie 1 seulement 
    
        # Modification pour partie 2 
        if plus: 
            iope = iplus 
        else: 
            iope = ifois
            
        idebg, ifing, idebd, ifind = lesMembres(exp, iope) 
        mbg = exp[idebg:ifing]
        mbd = exp[idebd:ifind]
        
        mbg = calcul( byeExces(mbg) )
        mbd = calcul( byeExces(mbd) ) 
        
        primeCalculus = operate(exp[iope], mbg, mbd) 
        
        recurs = exp[:idebg] + ' ' + str(primeCalculus) + ' ' + exp[ifind:]
        
        return calcul(recurs)
    
somme = 0 
for exp in myinput: 
    res = calcul(exp)
    somme += res 
print('somme', somme)
