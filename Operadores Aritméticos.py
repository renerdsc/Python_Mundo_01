# OPERADORES ARITMÉTICOS
5 + 2 # Adição
5 - 2 # Subtração
5 * 2 # Multiplicação
5 / 2 # Divisão
5 ** 2 # Potência
5 // 2 # Divisão inteira
5 % 2 # Resto da divisão

# ORDEM DE PRECEDÊNCIA
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

'''num1 = float(input('Digite um número:'))
num2 = float(input('Digite mais um número:'))
s = (num1 + num2) % 2
print('Você digitou o número {} e {} e o resto da divisão é {:.1f}'.format(num1, num2, s))'''

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma  e {} \n o produto é {} \n a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} \n e a potência e {}'.format(di, e))