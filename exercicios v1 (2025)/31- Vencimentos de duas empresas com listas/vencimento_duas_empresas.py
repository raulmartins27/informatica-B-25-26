empresa_A=3
empresa_B=4
lista_salario_A=[]
lista_salario_B=[]
acumulo_salario_A=0
acumulo_salario_B=0

for trabalhador in range(empresa_A):
    salario_A=-1
    while salario_A<=0:
        salario_A=float(input(f"Qual é o salário do trabalhador {trabalhador+1}? "))
    lista_salario_A.append(salario_A)

for trabalhador in range(empresa_B):
    salario_B=-1
    while salario_B<=0:
        salario_B=float(input(f"Qual é o salário do trabalhador {trabalhador+1}? "))
    lista_salario_B.append(salario_B)

#somar e acumular teto salarial de cada empresa + media salarial
for salarios in lista_salario_A:
    acumulo_salario_A+=salarios
media_salario_A= acumulo_salario_A/3

for salarios in lista_salario_B:
    acumulo_salario_B+=salarios
media_salario_B= acumulo_salario_B/4

maior_custo=0
frase=""
if acumulo_salario_A>acumulo_salario_B:
    maior_custo=acumulo_salario_A 
    frase="A"
elif acumulo_salario_A<acumulo_salario_B:
    maior_custo=acumulo_salario_B
    frase="B"
else:
    maior_custo=acumulo_salario_A
    frase="Nenhuma, as despesas de ambas as empresas com os vencimentos sao iguais."


print("\nTOTAL DOS VENCIMENTOS")
print(f"Empresa A: {acumulo_salario_A} cve.")
print(f"Empresa B: {acumulo_salario_B} cve.")

print("\nMÉDIA DOS VENCIMENTOS DE CADA EMPRESA")
print(f"Empresa A: {media_salario_A:.2f}")
print(f"Empresa B: {media_salario_B:.2f}")

print(f"A empresa que tem o maior custo\
\ncom os vencimentos é a empresa: {frase} com {maior_custo} cve.")