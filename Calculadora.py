numero1 = float(input('Digite o primeiro Número: '))
numero2 = float(input('Digite o segundo Número: '))


print('1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão')
EscolhaDeOperacoes = int(input('Qual operação o usuário deseja? '))

def case1():
    return numero1 + numero2

def case2():
    return numero1 - numero2

def case3():
    return numero1 * numero2

def case4():
    if numero2 == 0:
        print('Impossível dividir o número por 0')
        return None
    else:
        return numero1 / numero2

def default():
    print('Opção Inválida!')

switch = {
    1: case1,
    2: case2,
    3: case3,
    4: case4,
}


resultado = switch.get(EscolhaDeOperacoes, default)()
if resultado is not None:
    print('Resultado:', resultado)