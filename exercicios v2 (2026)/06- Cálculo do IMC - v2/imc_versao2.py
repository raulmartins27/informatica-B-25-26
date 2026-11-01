#funçao obriga o usuario a digitar um valor valido.
def pedir_numero_positivo(pergunta, valor_minimo):
        while True:
            try:
                valor=float(input(pergunta))
                if valor<valor_minimo:
                    print(f"Digite um valor válido, sendo maior ou igual a {valor_minimo}. ")
                else: return valor
            except ValueError:
                print("Digite um número válido. ")

#peso + unidade de peso
peso=pedir_numero_positivo("Qual é a peso? ", 0)
unidade_peso= input("Qual é a unidade de peso? (kg ou lb) ").lower() 
if unidade_peso=="lb":
     peso*=0.453592



#altura + unidade de medida
altura=pedir_numero_positivo("Qual é a altura? ", 0.01)
unidade_medida= input("Qual é a unidade de medida? (cm ou m) ").lower()
if unidade_medida=="cm":
    altura/=100


           
imc=peso/altura**2


if imc<20:
    print(f"O teu IMC é de {imc} valores, estás abaixo do peso.")
elif imc<30:
    print(f"O teu IMC é de {imc} valores, estás com o peso adequado.")
else:
    print(f"O teu IMC é de {imc} valores, estás obeso.")