def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def soma(limite):
    somaprimos = 0
    for num in range(2, limite):
        if primo(num):
            somaprimos += num
    return somaprimos

limite = 1000
resultado = soma(limite)
print("A soma de todos os números primos menores que", limite, "é:", resultado)
