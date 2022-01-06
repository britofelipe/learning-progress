'''
Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.

Exemplos:
1297: 12 e 97.
5314: 53 e 14.
5314 --> 53*100 + 14
Escreva um programa que imprime todos os milhares (4 algarismos)
1000 <= n < 10000
cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima.
    Exemplo: raiz de 9801 = 99 = 98 + 01.
    Portanto 9801 é um dos números a ser impresso.
'''

n = 1000
cont = 1

while n < 10000:
    x = n // 100
    y = n % 100
    if (x + y) * (x+ y) == n:
        print(n, "->", x, "+", y, "=", (x+y))
    n = n + 1
