print('-----Calculadora------')

operacao = input('''Selecione a operação e insira os valores: 
+ para adição
- para subtração 
x para multiplicação
/ para divisão
% para percentual:     ''')

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

if operacao == '+':
    print(n1 + n2)

elif operacao == '-':
    print(n1 - n2)

elif operacao == 'x':
    print(n1 * n2)

elif operacao == '/':
    print(n1 / n2)

elif operacao == '%':
    print(n1 / 100,'%')
    print(n2 / 100,'%')

else:
    print('Operação inválida')