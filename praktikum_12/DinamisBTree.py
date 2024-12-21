from binaryTree import *

def AddX(P, X):
    if IsEmpty(P):
        return MakePB(X, [], [])
    else:
        if X > Akar(P):
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))
        else:
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))

def Delete(P, X):
    if IsEmpty(P):
        return []
    else:
        if Akar(P) == X:
            if IsEmpty(Left(P)) and IsEmpty(Right(P)):
                return []
            #elif not IsEmpty(Left(P)) and not IsEmpty(Right(P)) :

            else:
                if IsEmpty(Left(P)):
                    return Right(P)
                    #return MakePB(Akar(Right(P)), Left(P), Right(Right(P)))
                else:
                    return Left(P)
                    #return MakePB(Akar(Left(P)), Left(Left(P)), Right(P))

        elif X >= Akar(P):
            return MakePB(Akar(P), Left(P), Delete(Right(P), X))
        else:
            return MakePB(Akar(P), Delete(Left(P), X), Right(P)) 
 
T = AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 200), 100),60),120)
print(T)
PrintBinaryTree(T)
PrintBinaryTree(Delete(T, 50))
PrintBinaryTree(Delete(T, 40))
print(Delete(T, 50))
