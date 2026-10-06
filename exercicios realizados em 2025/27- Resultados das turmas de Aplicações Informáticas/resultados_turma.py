turma1=0
acumulo_nota_turma_1=0

turma2=0
acumulo_nota_turma_2=0

turma3=0
acumulo_nota_turma_3=0


qtd_turma_1=-1
while qtd_turma_1<=0:
    qtd_turma_1=int(input("Quantos alunos tem a turma 1? "))
for i in range(1, qtd_turma_1+1):
    nota1=-1
    while nota1<0 or nota1>20:
        nota1=int(input(f"Qual foi a nota do aluno {i}? "))
    acumulo_nota_turma_1+=nota1

media_turma_1=acumulo_nota_turma_1/qtd_turma_1

qtd_turma_2=-1
while qtd_turma_2<=0:
    qtd_turma_2=int(input("Quantos alunos tem a turma 2? "))
for i in range(1, qtd_turma_2+1):
    nota2=-1
    while nota2<0 or nota2>20:
        nota2=int(input(f"Qual foi a nota do aluno {i}? "))
    acumulo_nota_turma_2+=nota2

media_turma_2=acumulo_nota_turma_2/qtd_turma_2


qtd_turma_3=-1
while qtd_turma_3<=0:
    qtd_turma_3=int(input("Quantos alunos tem a turma 3? "))
for i in range(1, qtd_turma_3+1):
    nota3=-1
    while nota3<0 or nota3>20:
        nota3=int(input(f"Qual foi a nota do aluno {i}? "))
    acumulo_nota_turma_3+=nota3

media_turma_3=acumulo_nota_turma_3/qtd_turma_3


media_geral=(media_turma_1+media_turma_2+media_turma_3)/3

melhor_media=0
if media_turma_1>media_turma_2 and media_turma_1>media_turma_3:
    melhor_media=media_turma_1
    melhor_turma=1

elif media_turma_1==media_turma_2 and media_turma_1>media_turma_3:
    melhor_media=media_turma_1
    melhor_turma="1 e 2"

elif media_turma_1>media_turma_2 and media_turma_1==media_turma_3:
    melhor_media=media_turma_1
    melhor_turma="1 e 3"

elif media_turma_2>media_turma_1 and media_turma_2>media_turma_3:
    melhor_media=media_turma_2
    melhor_turma=2

elif media_turma_2==media_turma_1 and media_turma_2>media_turma_3:
    melhor_media=media_turma_2
    melhor_turma="1 e 2"

elif media_turma_2>media_turma_1 and media_turma_2==media_turma_3:
    melhor_media=media_turma_2
    melhor_turma="2 e 3"

elif media_turma_3>media_turma_1 and media_turma_3>media_turma_2:
    melhor_media=media_turma_3
    melhor_turma=3

elif media_turma_3==media_turma_1 and media_turma_3>media_turma_2:
    melhor_media=media_turma_3
    melhor_turma="1 e 3"

elif media_turma_3>media_turma_1 and media_turma_3==media_turma_2:
    melhor_media=media_turma_3
    melhor_turma="2 e 3"

else:
    melhor_media=media_turma_1
    melhor_turma="1, 2 e 3"


print(f"Melhor turma: {melhor_turma}")
print(f"Melhor média: {melhor_media:.2f}")
print(f"Média geral: {media_geral:.2f}")