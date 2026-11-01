alunos = int(input("Introduza o número de alunos da turma: "))
while alunos <= 0:
        alunos = int(input("Introduza novamente o número de alunos: "))
 
soma_idades = 0
for i in range(1, alunos + 1):
    idade = int(input(f"Introduza a idade do aluno {i}: "))
    soma_idades += idade
 
media = soma_idades / alunos
print(f"\nA média de idades da turma é: {media:.2f} anos")