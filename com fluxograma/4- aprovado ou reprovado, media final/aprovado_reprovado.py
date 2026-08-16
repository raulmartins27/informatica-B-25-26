print("seja bem vindo ao programa de cálculo da média final que decide se o aluno está reprovado ou aprovado.")
NE= float(input("Qual é a nota escrita do aluno?"))
NO= float(input("Qual é a nota oral do aluno?"))
NF= NE*0.75 + NO*0.25
print(f"A nota final é de {NF} valores.")
if NF>=10:
    print("O aluno está aprovado")
else:
    print("O aluno está reprovado.")
