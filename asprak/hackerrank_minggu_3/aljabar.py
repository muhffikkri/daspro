def fxabs(x:int)->int:
    return (x if x >=0 else -x)
def akar1(a:int,b:int,c:int)->float:
    return (-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)
def akar2(a:int,b:int,c:int)->float:
    return (-b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)

def Aljabar(a:int,b:int,c:int)->float:
    if (b ** 2 - (4 * a * c)) >= 0:
        if fxabs(akar1(a,b,c)) <= fxabs(akar2(a,b,c)):
            return round(fxabs(akar1(a,b,c) / akar2(a,b,c)),5)
        elif fxabs(akar1(a,b,c)) > fxabs(akar2(a,b,c)):
            return round(fxabs(akar2(a,b,c) / akar1(a,b,c)),5)
    else:
        return -999

#JANGAN DIUBAH!
print(eval(input()))