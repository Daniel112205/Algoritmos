def bin_exp_mod(a,n,b):
    """
    >>> bin_exp_mod(3, 4, 5)
    1
    >>> bin_exp_mod(7, 13, 10)
    7
    """
    #! mod b
    assert not (b == 0), "This cannot accept modulo that is == 0"#? O(1)
    if n == 0:#? O(1)
        return 1
    if n % 2 == 1:
        return (bin_exp_mod(a, n - 1, b) * a) % b#? O(1)

    r = bin_exp_mod(a, n / 2, b)#? O(1)
    return (r * r) % b#? O(1)

    #No necesita ser optimizado porque esta correcto el algoritmo
    #Realiza su ejecución correctamente

print(bin_exp_mod(3, 4, 5))
print(bin_exp_mod(7, 13, 10))