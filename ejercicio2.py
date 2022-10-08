from collections.abc import Sequence

def decimal_to_binary(no_of_variable: int, minterms: Sequence[float])-> list[str]:
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """ 
    temp = []#? O(1)
    for minterm in minterms:#? O(n)
        string = ""#? O(1)
        for i in range(no_of_variable): #? O(n) * O(n) = O(n^2)
            string = str(minterm % 2) + string#? O(1)
            minterm //= 2#? O(1)
        temp.append(string)#? O(1)
    return temp

    #No necesita ser refactorizado cumple con el correcto funcionamiento de notación Big-o

print(decimal_to_binary(3, [1.5]))