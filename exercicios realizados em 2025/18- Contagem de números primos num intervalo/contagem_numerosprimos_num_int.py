limite_inferior=-1
while limite_inferior<0:
    limite_inferior=int(input("Qual é o limite inferior do intervalo? "))

limite_superior=-1
while limite_superior<limite_inferior:
    limite_superior=int(input("Qual é o limite superior do intervalo? "))

primos=0
numero=limite_inferior

print("Os números primos deste intervalo são:")
while numero<=limite_superior:
    if numero>=2:
     divisor=2
     qtd_resto_0=0
     while numero>divisor:
            if numero%divisor==0:
                qtd_resto_0+=1
            divisor+=1
     if qtd_resto_0==0:
        primos+=1
        print(numero)
    numero+=1

print("\n---RESULTADOS---")
print(f"Intervalo analisado:[{limite_inferior}, {limite_superior}] ")
print(f"Quantidade de números primos encontrados: {primos}.")