from time import sleep

situacao = "Reprovado"
while situacao == "Reprovado":

    nome = input("Digite Seu nome: ")
    sobrenome = input("Digite Seu Sobrenome: ")
    idade = input("Digite seu Idade: ")
    notas = []

    for i in range(1, 5):
        nota = float(input(f"Digite sua {i} Nota: "))
        notas.append(nota)
    media =sum(notas) / len(notas)

    if(media < 7.0):
        situacao = "Reprovado"

    elif(media >= 7.0):
        situacao = "Aprovado"
        for i in range(10):
            print("*")
            sleep(1)
        print("Parabens voce foi aprovado no curso de Python")

    Aluno = {
                    "Nome": nome,
                    "Sobrenome": sobrenome,
                    "Idade": idade,
                    "Notas": notas,
                    "Media": media,
                    "Situacao": situacao   
            }
    var = input ("Deseja saber os dados completos do aluno ? \nsim \nnao\n >>")
    if var.capitalize() == "Sim":
        print(f'''
{Aluno["Nome"]}
{Aluno["Sobrenome"]}
{Aluno["Idade"]}
{Aluno["Notas"]}
{Aluno["Media"]}
{Aluno["Situacao"]}
''')
    