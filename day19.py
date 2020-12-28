input_file = open("day19.txt", 'r') # 147 pour la partie 1 
input_file = open("day19ex.txt", 'r') # 3 pour la partie 1, 12 pour la partie 2 
myinput = input_file.read().split(sep = '\n\n') 

rules = myinput[0].split(sep = '\n') 
messages = myinput[1].split(sep = '\n')

def findRule(rules, nbRule): 
    for i in range(len(rules)): 
        if rules[i].split(sep = ':')[0] == str(nbRule): 
            return i  

def followRule(nbRule, message): 
    global rules 
    
    rule = rules[findRule(rules, nbRule)].split(sep = ': ')
    contentRule = rule[1] 
    
    # Cas où la règle est simple. exemple : 4: "a" 
    if '"' in contentRule: 
        i = 0 
        ideb = 0 
        ifin = 0 
        while i < len(contentRule) and ifin == 0: 
            if contentRule[i] == '"': 
                if ideb == 0: 
                    ideb = i+1 
                else: 
                    ifin = i 
            i += 1 
        
        # On checke si la portion du message correspond à la règle simple 
        n = ifin - ideb 
        return contentRule[ideb:ifin] == message[:n], n 
    
    else: 
        getRules = contentRule.split(sep = ' | ')
        
        # On regarde chaque possible règle à suivre et on vérifie qu'elle est respectée. 
        
        for regle in getRules: 
            idxToCheck = 0 
            follow = True 
            rind = 0 
            rinddeb = -1  
            while rind < len(regle) and follow: 
                r = regle[rind] 
                if r != ' ': 
                    if rinddeb == -1: # Cas où on trouve le début d'un chiffre 
                        rinddeb = rind 
                    if rind == len(regle)-1: # Correction permettant de prendre en compte le dernier chiffre 
                        follow, lengthMsg = followRule(int(regle[rinddeb:]), message[idxToCheck:])  
                        idxToCheck += lengthMsg 
                        rinddeb = -1 
                        
                if r == ' ' and rinddeb != -1: # Cas où on trouve la fin d'un chiffre 
                    follow, lengthMsg = followRule(int(regle[rinddeb:rind]), message[idxToCheck:]) 
                    idxToCheck += lengthMsg 
                    rinddeb = -1 
                rind += 1 
            if follow: 
                return True, idxToCheck 
        return False, idxToCheck             

count = 0 
for msg in messages: 
    follow, n = followRule(0, msg) 
    if follow and len(msg) == n: 
        count += 1 
        print(msg)
print(count)
