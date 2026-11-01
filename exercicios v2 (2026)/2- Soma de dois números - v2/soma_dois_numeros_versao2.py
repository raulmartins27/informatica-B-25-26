#pergunta o numero 1
numero1 = float(input("Qual é o valor do primeiro número? ").replace(",", "."))

#pergunta o numero 2
numero2 = float(input("Qual é o valor do segundo número? ").replace(",", "."))

#calculo
resultado = numero1 + numero2

#remover a casa decimal .0 se o numero 1 for inteiro
if numero1.is_integer():
    numero1=int(numero1)

#remover a casa decimal .0 se o numero 2 for inteiro
if numero2.is_integer():
    numero2=int(numero2)    

#remover a casa decimal .0 se o resultado final for um número inteiro
if resultado.is_integer():
    resultado=int(resultado)

#apresentar o resultado
print(f"{numero1} + {numero2} = {resultado}")