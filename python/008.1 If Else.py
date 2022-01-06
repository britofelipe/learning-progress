idade = int(input("Digite a sua idade: "))
resp=idade>=18
if resp == True:
    print("Você pode beber à vontade.\n")
if resp == False:
    print("Você só pode beber refrigerante. \n")

idade = int(input("Digite a idade do seu amigo: "))
resp=idade>=18
if resp:
    print("Seu amigo pode beber à vontade.\n")
if resp != True:
    print("Seu amigo só pode beber refrigerante.\n")

idade = int(input("Digite a idade da sua amiga: "))
if idade>=18:
    print("Sua amiga pode beber à vontade.\n")
if idade<18:
    print("Sua amiga só pode beber refrigerante.\n")

idade = int(input("Digite novamente a sua idade, a fim de que possamos verificar se é cliente VIP: "))
if idade>=18:
    print("Você pode beber à vontade.")
if idade>=21:
    print("Você é cliente VIP.")
if idade<18:
    print("Você só pode beber refrigerante. Você não é cliente VIP.")

idade = int(input("Digite novamente a sua idade, a fim de que possamos verificar se é cliente VIP: "))
if idade>=18:
    print("Você pode beber à vontade.")
    if idade>=21:
        print("Você é cliente VIP.")
if idade<18:
    print("Você só pode beber refrigerante. Você não é cliente VIP.")

idade = int(input("Digite novamente a sua idade, a fim de que possamos verificar se é cliente VIP: "))
if idade>=18:
    print("Você pode beber à vontade.")
    if idade>=21:
        print("Você é cliente VIP.")
else:
    print("Você só pode beber refrigerante. Você não é cliente VIP.")

print("\n")