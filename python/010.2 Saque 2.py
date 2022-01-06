print("Bem-vindo ao caixa eletrônico")
saque = int(input("Digite o valor do seu saque: "))

if 10 <= saque <= 600:
        n100 = saque // 100
        saque = saque % 100

        n50 = saque // 50
        saque = saque % 50

        n20 = saque // 20
        saque = saque % 20

        n10 = saque // 10
        saque = saque % 10

        n5 = saque // 5
        saque = saque % 5

        n1 = saque // 1

        print("\nVocê irá receber:")
        if n100> 0:
                print("\t", n100, "notas de R$ 100,00")
        if n50 > 0:
                print("\t", n50, "notas de R$ 50,00")
        if n20 > 0:
                print("\t", n20, "notas de R$ 20,00")
        if n10 > 0:
                print("\t", n10, "notas de R$ 10,00")
        if n5 > 0:
                print("\t", n5, "notas de R$ 5,00")
        if n1 > 0:
                print("\t", n1, "notas de R$ 1,00")

        saque = 100

else:
        print("O valor informado para o seu saque não é possível")
        print("Por favor, informe um valor entre R$ 10,00 e R$ 600,00")