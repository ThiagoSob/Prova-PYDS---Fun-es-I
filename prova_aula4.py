# Desenvolva um programa em Python que funcione como uma calculadora simples, 
# permitindo ao usuário realizar as seguintes operações matemáticas:

# Soma
# Subtração
# Multiplicação
# Divisão
# Sair do programa
# Requisitos:
# O programa deve exibir um menu de opções, permitindo ao usuário escolher qual operação ele deseja realizar 
# (soma, subtração, multiplicação, divisão ou sair).
# Para cada operação escolhida, o programa deve solicitar ao usuário dois números e exibir o resultado 
# da operação entre eles.
# As operações matemáticas (soma, subtração, multiplicação e divisão) devem ser implementadas em funções separadas. 
# Cada função deve receber dois argumentos (números) e retornar o resultado da operação.
# O programa deve funcionar indefinidamente, permitindo ao usuário realizar quantas operações quiser, 
# até que ele escolha a opção de sair.
# Caso o usuário selecione a divisão, o programa deve garantir que a divisão por zero seja evitada, 
# exibindo uma mensagem de erro apropriada e solicitando novos valores.
# Use condicionais e laços de repetição para controlar o fluxo do programa e garantir que ele continue até 
# o usuário escolher a opção de sair.

##Funções:

###Soma:
def soma(x , y):
    return x+y

###Subtração:
def subtracao(x , y):
    return x - y

###Multiplicação:
def multiplicacao(x , y):
    return x * y

###Divisão:
def divisao(x , y):
    return x / y


##Variáveis:

op = '' #Variável de escolha

##Calculadora:

print('====='*10)
print('\n\n')
print('CALCULADORA')
print('\n\n')

while True: #Loop infinito de escolha
    print('====='*10)
    print('\n\n')
    print('Menu:\n\n[SO] Somar\n[SU] Subtrair\n[ML] Multiplicar\n[DV] Dividir\n[SR]Sair')
    print('\n')
    op = input('Qual opção deseja executar: ')
    opl = op.lower()
    print('\n\n')
    print('====='*10)
    print('\n\n')
    if opl == 'so':
        x = float(input('Qual o primeiro valor a ser somado: '))
        y = float(input('Qual o segundo valor a ser somado: '))
        print(f'{x:.2f} + {y:.2f} = {soma(x , y):.2f}')
        print('\n\n')
        print('====='*10)

    elif opl == 'su':
        x = float(input('Qual o primeiro valor a ser subtraido: '))
        y = float(input('Qual o segundo valor a ser subtraido: '))
        print(f'{x:.2f} - {y:.2f} = {subtracao(x , y):.2f}')
        print('\n\n')
        print('====='*10)
    elif opl == 'ml':
        x = float(input('Qual o primeiro valor a ser multiplicado: '))
        y = float(input('Qual o segundo valor a ser multiplicado: '))
        print(f'{x:.2f} x {y:.2f} = {multiplicacao(x , y):.2f}')
        print('\n\n')
        print('====='*10)
    elif opl == 'dv':
        x = float(input('Qual o primeiro valor a ser divisão: '))
        y = float(input('Qual o segundo valor a ser divisão: '))
        while y == 0:
            print('Erro, nâo existe divisão por 0')
            print('\n')
            y = float(input('Qual o segundo valor a ser divisão: '))
            print('\n\n')
        print(f'{x:.2f} / {y:.2f} = {divisao(x , y):.2f}')
        print('\n\n')
        print('====='*10)
    elif opl== 'sr':
        print('SAINDO...')
        print('\n\n')
        print('====='*10)
        break
    else:
        print('Opção Inválida!\nTente Novamente...')
        print('\n\n')
        print('====='*10)
        continue