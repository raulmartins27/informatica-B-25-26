qtd_alunos=-1
while qtd_alunos<0:
    qtd_alunos=int(input("Quantos alunos tem a turma? "))
    if qtd_alunos<0:
        print("A quantidade de alunos deve ser positiva. Tente novamente.")

acumulador_nota_1=0
acumulador_nota_2=0
acumulador_nota_3=0
acumulador_nota_4=0
acumulador_nota_5=0
total_notas=0

for i in range(1, qtd_alunos+1):
     classificaçao=-1
     while classificaçao<1 or classificaçao>5:
        classificaçao=int(input(f"Qual foi a classificaçao do aluno {i}? "))
        if classificaçao<1 or classificaçao>5:
            print("A calssificaçao minima é 1 e a máxima é 5, introduza novamente. ")
     if classificaçao==1:
         acumulador_nota_1+=1
         total_notas+=classificaçao
     elif classificaçao==2:
         acumulador_nota_2+=1
         total_notas+=classificaçao
     elif classificaçao==3:
         acumulador_nota_3+=1
         total_notas+=classificaçao
     elif classificaçao==4:
         acumulador_nota_4+=1
         total_notas+=classificaçao
     else:
         acumulador_nota_5+=1
         total_notas+=classificaçao

media=total_notas/qtd_alunos

print(f"\nNível 1: {acumulador_nota_1}")
print(f"Nível 2: {acumulador_nota_2}")
print(f"Nível 3: {acumulador_nota_3}")
print(f"Nível 4: {acumulador_nota_4}")
print(f"Nível 5: {acumulador_nota_5}")

print(f"\nA média final de classificaçoes em TIC foi de: \n{media} valores.")