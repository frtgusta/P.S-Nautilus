def primo(numero):
    def verificacao(num):
        if num <= 1:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    for i in range(numero, 0, -1):
        if numero % i == 0:
            if verificacao(i):
                return i

def principal():
    try:
        numero = int(input("digite um número inteiro positivo: "))
        if numero <= 0:
            print("por favor, digite um número inteiro positivo.")
        else:
            divisorMaior = primo(numero)
            print(f"o maior divisor primo de {numero} é: {divisorMaior}")
    except ValueError:
        print("por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    principal()

