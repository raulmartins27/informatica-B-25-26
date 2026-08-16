larg=float(input('Qual é a largura da sala? '))
compr=float(input('Qual é o comprimento da sala?'))
area=larg*compr
if area>30:
    print(f'A area da sala é de {area} centimetros. A sala é grande.')
else:
    print(f'A area da sala é de {area} centimetros. A sala é pequena.')
