from binaryTree import *

def AddX(P, X):
    """
    Add an element to a binary tree.

    :param P: The binary tree.
    :type P: list
    :param X: The element to be added.
    :type X: int
    :return: The binary tree with the element added.
    :rtype: list

    :example:
    >>> AddX([], 50)
    [50, [], []]
    >>> AddX([50, [], []], 75)
    [50, [], [75, [], []]]

    :raises TypeError: If P is not a list or X is not an integer.
    """
    if IsEmpty(P):
        return MakePB(X, [], [])
    else:
        if X > Akar(P):
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))
        else:
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))

def Delete(P, X):
    """
    Delete an element from a binary tree.

    :param P: The binary tree.
    :type P: list
    :param X: The element to be deleted.
    :type X: int
    :return: The binary tree with the element deleted.
    :rtype: list

    :example:
    >>> T = AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 200), 100), 60), 120)
    >>> Delete(T, 50)
    [60, [], [75, [], [200, [100, [], [120, [], []]], []]]]

    :raises TypeError: If P is not a list or X is not an integer.
    """
    if IsEmpty(P):
        return []
    else:
        if Akar(P) == X:
            if IsEmpty(Left(P)) and IsEmpty(Right(P)):
                return []
            else:
                if IsEmpty(Left(P)):
                    return Right(P)
                else:
                    return Left(P)
        elif X >= Akar(P):
            return MakePB(Akar(P), Left(P), Delete(Right(P), X))
        else:
            return MakePB(Akar(P), Delete(Left(P), X), Right(P))

if __name__ == "__main__":
    T = AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 200), 100), 60), 120)
    print(T)
    PrintBinaryTree(T)
    PrintBinaryTree(Delete(T, 50))
    PrintBinaryTree(Delete(T, 40))
    print(Delete(T, 50))