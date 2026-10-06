limite_inferior = -1
while limite_inferior < 0:
    limite_inferior = int(input("Qual é o limite inferior do intervalo? "))

limite_superior = -1
while limite_superior < limite_inferior:
    limite_superior = int(input("Qual é o limite superior do intervalo? "))

multiplo3 = 0
contador = limite_inferior

print("Múltiplos de 3:")
while contador <= limite_superior:
    if contador % 3 == 0:
        print(contador)
        multiplo3 += 1
    contador += 1

print(f"Quantidade de múltiplos de 3: {multiplo3}")