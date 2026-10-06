lista_idade=[]
qtd_alunos=-1
acumulador_idades=0
while qtd_alunos<=0:
    qtd_alunos=int(input("Quantos alunos tem a turma? "))
for alunos in range(1, qtd_alunos+1):
    idade=-1
    while idade<=15 or idade >20:
        idade=int(input(f"Qual é a idade do aluno {alunos}? "))
    lista_idade.append(idade)
    acumulador_idades+=idade

media_idades=acumulador_idades/qtd_alunos
print(f"\nA média das idades da turma é de {media_idades:.2f} anos. ")

numero_verificar=-1
while numero_verificar<=0:
    numero_verificar=int(input("Coloque uma determinada idade para verificar\n" \
    "se está na lista ou nao. "))
if numero_verificar in lista_idade:
    print(f"A idade de {numero_verificar} anos está na lista.")
else:
    print(f"A idade de {numero_verificar} anos nao está na lista. ")