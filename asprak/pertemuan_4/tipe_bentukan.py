type Point = tuple[float, float]

def MakePoint(x: float, y: float) -> Point:
    return (x, y)

def getAbsis(p: Point) -> float:
    return p[0]

def getOrdinat(p: Point) -> float:
    return p[1]

def JarakTitik(t1: Point, t2: Point) -> float:
    return ((getAbsis(t2) - getAbsis(t1))**2 + (getOrdinat(t2) - getOrdinat(t1))**2)**0.5

def kuadran(p: Point) -> int:
    if getAbsis(p) > 0 and getOrdinat(p) > 0:
        return 1
    elif getAbsis(p) < 0 and getOrdinat(p) > 0:
        return 2
    elif getAbsis(p) < 0 and getOrdinat(p) < 0:
        return 3
    elif getAbsis(p) > 0 and getOrdinat(p) < 0:
        return 4
    else:
        return 0
    
def isTitikOrigin(p: Point) -> bool:
    return getAbsis(p) == 0 and getOrdinat(p) == 0

def isEqualTitik(t1: Point, t2: Point) -> bool:
    return getAbsis(t1) == getAbsis(t2) and getOrdinat(t1) == getOrdinat(t2)

