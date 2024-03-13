def case1(numeros):
    numeros.sort()
    print("\nNúmeros em ordem crescente: ", numeros)

def case2(numeros):
    numeros.sort(reverse=True)
    print("\nNúmeros em ordem decrescente: ", numeros)

def default():
    print('Opção inválida')

entrada = input("Digite os números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]
print("Vetor de números inseridos:", numeros)

escolha = int(input("Escolha a opção (1 para crescente, 2 para decrescente): "))

switch = {
    1: lambda: case1(numeros),
    2: lambda: case2(numeros),
    
    3: default
}

switch.get(escolha, default)()
