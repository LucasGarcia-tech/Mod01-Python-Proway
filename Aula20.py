numero = int(input("Digite o número da Tabuada que voce deseja saber"))

for i in range(1,11):   
    print("{} x {} = {}".format(numero,i,numero*i))