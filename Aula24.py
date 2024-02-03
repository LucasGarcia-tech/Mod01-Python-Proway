from time import sleep
valor = int(input("Digite o valor que deseja inserir: ")) 
nomes = []

for i in range(1,valor+1):
  nome = input(f"Digite o {i} Nome: ")
  nomes.append(nome)
for i in range(10):
     print("*") 
     sleep(1)
for nome in nomes:
        print(nomes)

