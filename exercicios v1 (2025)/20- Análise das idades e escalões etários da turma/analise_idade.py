num_alunos = -1
while num_alunos <= 0:
    num_alunos = int(input("Introduza o número de alunos da turma: "))
 
soma_idades = 0
contador_menos_12 = 0
contador_entre_12_18 = 0
contador_mais_18 = 0
 
contador = 1
while contador <= num_alunos:
    idade = 0
    while idade <= 0:
        idade = int(input(f"Introduza a idade do aluno {contador}: "))
        if idade <=0:
            print("A idade tem de ser um número positivo")
    soma_idades = soma_idades+idade
 
    if idade < 12:
        contador_menos_12 += 1
    else:
        if idade <= 18:
            contador_entre_12_18 += 1
        else:
            contador_mais_18 += 1
 
    contador = contador + 1
 
media = soma_idades / num_alunos
if media < 12:
    classificacao = "Turma muito jovem"
else:
    if media <= 18:
        classificacao = "Turma adolescente"
    else:
        classificacao = "Turma adulta"
 
print("\n--- Resultados ---")
print(f"Média das idades: {media}")
print(f"Classificação da turma: {classificacao}")
print(f"Total de alunos analisados: {num_alunos}")
print(f"Alunos com menos de 12 anos: {contador_menos_12}")
print(f"Alunos entre 12 e 18 anos: {contador_entre_12_18}")
print(f"Alunos com mais de 18 anos: {contador_mais_18}")