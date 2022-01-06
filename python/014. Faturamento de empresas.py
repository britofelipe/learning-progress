'''
Dado um numero n de empresas, e um numero m de meses,
e o ganho e gastos positivos e inteiros de cada empresa para cada mês,
imprimir se a empresa nesses meses ficou com défict, lucro ou indiferente e
imprimir o valor correspondente a essa balança
'''

n = int(input("Digite o número de empresas: "))
m = int(input("Digite o número de meses: "))

empresas = 1

while empresas <= n:
    meses = 1
    resultado = 0
    print("\nEMPRESA", empresas, ":")
    while meses <= m:
        print("\nMês", meses, ":")
        ganho = int(input("Digite o ganho da empresa para o mês: "))
        gasto = int(input("Digite o gasto da empresa para o mês: "))
        resultado = resultado + ganho - gasto
        meses = meses + 1
    if resultado == 0:
        print("\nA empresa não teve lucro nem prejuízo para o período apresentado.")
    elif resultado > 0:
        print("\nA empresa teve lucro de R$", resultado, "para o período apresentado.")
    elif resultado < 0:
        print("\nA empresa teve prejuízo de - R$", -1*resultado, "para o período apresentado.")
        meses = 0
    empresas = empresas + 1

