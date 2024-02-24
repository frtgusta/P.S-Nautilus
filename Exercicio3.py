def palindromo(numero):
    num_str = str(numero)
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def principal():
    try:
        num1 = int(input("por favor, insira um número para verificar se é um palíndromo: "))
        
        if palindromo(num1):
            print("O número", num1, "é um palíndromo!")
        else:
            print("O número", num1, "não é um palíndromo.")
    except ValueError:
        print("por favor, insira um número válido.")

if __name__ == "__main__":
    principal()
