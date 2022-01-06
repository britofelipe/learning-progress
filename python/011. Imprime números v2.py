'''Faça um programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo'''

numero=int(input("Digite o número desejado: "))

if 0 < numero < 1000:
    if numero//100 >= 0:
        centenas = numero//100
        numero = numero % 100
    if numero//10 >= 0:
        dezenas = numero//10
        numero = numero % 10
    if numero//1 >= 0:
        unidades = numero

    if centenas > 1:
        if dezenas > 1:
            if unidades > 1:
                print("O número possui", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", centenas, "centenas e", dezenas, "dezenas.")
        elif dezenas == 1:
            if unidades > 1:
                print("O número possui", centenas, "centenas,", dezenas, "dezena e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", centenas, "centenas,", dezenas, "dezena e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", centenas, "centenas e", dezenas, "dezenas.")
        elif dezenas == 0:
            if unidades > 1:
                print("O número possui", centenas, "centenas e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", centenas, "centenas e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", centenas, "centenas.")
    elif centenas == 1:
        if dezenas > 1:
            if unidades > 1:
                print("O número possui", centenas, "centena,", dezenas, "dezenas e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", centenas, "centena,", dezenas, "dezenas e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", centenas, "centena e", dezenas, "dezenas.")
        elif dezenas == 1:
            if unidades > 1:
                print("O número possui", centenas, "centena,", dezenas, "dezena e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", centenas, "centena,", dezenas, "dezena e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", centenas, "centena e", dezenas, "dezenas.")
        elif dezenas == 0:
            if unidades > 1:
                print("O número possui", centenas, "centena e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", centenas, "centena e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", centenas, "centena.")
    elif centenas == 0:
        if dezenas > 1:
            if unidades > 1:
                print("O número possui", dezenas, "dezenas e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", dezenas, "dezenas e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", dezenas, "dezenas.")
        elif dezenas == 1:
            if unidades > 1:
                print("O número possui", dezenas, "dezena e", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", dezenas, "dezena e", unidades, "unidade.")
            elif unidades == 0:
                print("O número possui", dezenas, "dezenas.")
        elif dezenas == 0:
            if unidades > 1:
                print("O número possui", unidades, "unidades.")
            elif unidades == 1:
                print("O número possui", unidades, "unidade.")
else:
    print("O número é inválido")

