quantidade = -1
while quantidade <=0:
    quantidade=int(input('Quantas pessoas?'))
qtd=1
Soma=0
while qtd<=quantidade:
    idade = -1 
    while idade<0:
        idade=int(input('Qual a idade?'))
        Soma=Soma+idade
    qtd=qtd+1
Media=Soma/quantidade
print('A média das idades é:')
if Media<18:
    print('Grupo de Jovens')
else:
    if Media<40:
        print('Grupo Adulto')
    else:
        print('Grupo Sénior')