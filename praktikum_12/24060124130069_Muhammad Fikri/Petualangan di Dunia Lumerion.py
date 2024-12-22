# NAMA: Muhammad Fikri 
# NIM : 24060124130069

def IsEmpty(L) :
    return L == []

def FirstElmt(L) :
    return L[0]

def LastElmt(L) :
    return L[-1]

def Tail(L) :
    return L[1:]

def Head(L) :
    return L[:-1]

def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

def operateVar(operator, S) : 
    if IsOneElmt(S) : 
        return FirstElmt(S)
    if operator == '+':
        return FirstElmt(S) + operateVar(operator, Tail(S))
    elif operator == '-':
        return FirstElmt(S) - operateVar(operator, Tail(S))
    elif operator == '*':
        return FirstElmt(S) * operateVar(operator, Tail(S))
    elif operator == '/':
        return FirstElmt(S) / operateVar(operator, Tail(S))


def EvaluateExpression(S) : 
    if IsEmpty(S) : 
        return []
    
    if FirstElmt(S) == "+" : 
        return operateVar(FirstElmt(S), Tail(S))
    elif FirstElmt(S) == "-" : 
        return operateVar(FirstElmt(S), Tail(S))
    elif FirstElmt(S) == "/" :
        return operateVar(FirstElmt(S), Tail(S))
    elif FirstElmt(S) == "*" :
        return operateVar(FirstElmt(S), Tail(S))
    
print(eval(input()))