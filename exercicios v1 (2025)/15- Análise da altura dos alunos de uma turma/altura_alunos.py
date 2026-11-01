Alunos=-1
while Alunos<0:
    Alunos=int(input("Quantos alunos existem na turmna? "))

contador_alunos=0
soma_altura=0

while contador_alunos<Alunos:
    altura=-1
    while altura<0:
        altura=float(input(f"Qual é a altura do aluno {contador_alunos+1}? (em centímetros) "))
    contador_alunos+=1
    soma_altura=soma_altura+altura

media_alt=soma_altura/Alunos

classificaçao=0
if media_alt<140:
    classificaçao=print("Turma baixa")
elif media_alt<170:
    classificaçao=print("Turma de altura média")
else:
    classificaçao=print("Turma alta")

print ("\nRESULTADOS FINAIS:")
print(f"A média de altura é de {media_alt} centímetros.")
print(f"A classifiçao atribuída à turma foi: {classificaçao} ")
print(f"O número total de analisados foi: {Alunos}")