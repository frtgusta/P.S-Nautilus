def iguais(lista):
    if not lista:
        return False
    return lista[0] == lista[-1]

lista1 = [5, 3, 1, 0, 5]
lista2 = [1, 0, 0, 6, 2]

if iguais(lista1):
    print("o primeiro item da lista 1 é igual ao último item")
else:
    print("o primeiro item da lista 1 é diferente do último item")

if iguais(lista2):
    print("o primeiro item da lista 2 é igual ao último item.")
else:
    print("o primeiro item da lista 2 é diferente do último item")
