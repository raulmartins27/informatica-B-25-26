limite_inferior=-1
while limite_inferior<0:
    limite_inferior=int(input("Qual é o limite inferior do intervalo? "))

limite_superior=-1
while limite_superior<limite_inferior:
    limite_superior=int(input("Qual é o limite superior do intervalo? "))


pares=0
impares=0
contagem_numeros=limite_inferior

while contagem_numeros<=limite_superior:
    if contagem_numeros % 2 ==0:
        pares+=1
    else:
        impares+=1
    contagem_numeros+=1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")