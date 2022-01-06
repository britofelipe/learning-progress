print("Bem-vindo ao caixa eletrônico")
saque = int(input("Digite o valor do seu saque: "))

n100 = 0
n50 = 0
n20 =0
n10 = 0
n5 = 0
n1 = 0
valor_remanescente = 0

if 10 <= saque <= 600:
        n100 = saque // 100
        valor_remanescente = saque % 100

        if valor_remanescente > 0:
                n50 = valor_remanescente // 50
                valor_remanescente = valor_remanescente % 50

                if valor_remanescente > 0:
                        n50 = valor_remanescente // 50
                        valor_remanescente = valor_remanescente % 50
                        if valor_remanescente > 0:
                                n20 = valor_remanescente // 20
                                valor_remanescente = valor_remanescente % 20
                                if valor_remanescente > 0:
                                        n10 = valor_remanescente // 10
                                        valor_remanescente = valor_remanescente % 10
                                        if valor_remanescente > 0:
                                                n5 = valor_remanescente // 5
                                                valor_remanescente = valor_remanescente % 5
                                                if valor_remanescente > 0:
                                                        n1 = valor_remanescente // 1
                                                        valor_remanescente = valor_remanescente % 1

        print("\nVocê irá receber:")
        print("\t", n100, "notas de R$ 100,00")
        print("\t", n50, "notas de R$ 50,00")
        print("\t", n20, "notas de R$ 20,00")
        print("\t", n10, "notas de R$ 10,00")
        print("\t", n5, "notas de R$ 5,00")
        print("\t", n1, "notas de R$ 1,00")

else:
        print("O valor informado para o seu saque não é possível")
        print("Por favor, informe um valor entre R$ 10,00 e R$ 600,00")