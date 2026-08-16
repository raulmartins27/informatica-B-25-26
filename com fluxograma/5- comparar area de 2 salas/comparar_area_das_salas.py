print("Seja bem vindo ao programa de comparar a área de duas salas retangulares")
umc= input("Qual é a unidade de medida? ")
comp1= float(input("Qual é o comprimento da sala 1? "))
larg1= float(input("Qual é a largura da sala 1? "))
area1= comp1*larg1
print(f"A área da sala 1 é de {area1} {umc}.  ")
comp2= float(input("Qual é o comprimento da sala 2? "))
larg2= float(input("Qual é a largura da sala 2? "))
area2= comp2*larg2
print(f"A área da sala 2 é de {area2} {umc}.  ")
if area1>area2:
    print("A maior área é a área da sala 1")
else: 
    print("A maior área é a área da sala 2")