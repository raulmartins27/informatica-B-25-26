quantidade_alunos=-1
while quantidade_alunos<=0:
    quantidade_alunos=int(input("Quantos alunos tem a turma? "))
 
soma_idade=0
contador_aluno=1
while contador_aluno<=quantidade_alunos:
    idade=0
    while idade <= 0:
        idade=int(input(f"Introduza a idade do aluno {contador_aluno}: "))
    soma_idade=soma_idade+idade
    contador_aluno=contador_aluno+1
 
media_idade=soma_idade/quantidade_alunos
classificacao=""
if media_idade<12:
    classificacao="Turma muito jovem"
else:
    if media_idade<=18:
        classificacao="Turma adolescente"
    else:
        classificacao="Turma adulta"
 
print(f"Média das idades: {round(media_idade, 2)}")
print(f"Classificação: {classificacao}")
print(f"Total de alunos: {quantidade_alunos}")