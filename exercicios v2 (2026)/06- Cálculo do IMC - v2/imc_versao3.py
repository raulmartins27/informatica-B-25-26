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


#funçao obriga o usuario a digitar uma unidade válida.
def pedir_unidade(pergunta, unidades_validas):
      while True:
           unidade=input(pergunta).strip().lower()

           if unidade in unidades_validas:
             return unidades_validas[unidade]
           else:
               print("Unidade inválida. Tente novamente! ")

#pedir peso
peso=pedir_numero_positivo("Qual é o peso? ",0)
unidade_peso= pedir_unidade ("Qual é a unidade do peso? (kg ou lb) ", 
                            {"kg": "kg",
                             "quilo": "kg",
                              "quilos": "kg",
                              "quilograma": "kg",
                              "quilogramas": "kg",
                              "lb": "lb",
                              "lbs": "lb",
                              "libras": "lb",
                              "libra": "lb"}) 


#pedir altura
altura=pedir_numero_positivo("Qual é a altura? ", 0.01)
unidade_altura = pedir_unidade("Qual é a unidade da altura? (m ou cm) ",
                               {   "m": "m",
                                   "metro": "m",
                                   "metros": "m",
                                   "cm": "cm",
                                   "centimetro": "cm",
                                   "centimetros": "cm",
                                   "centímetro": "cm",
                                   "centímetros": "cm"})

if unidade_peso == "lb":
    peso = peso * 0.453592

if unidade_altura == "cm":
    altura = altura / 100


imc=peso/altura**2


if imc<20:
    print(f"O teu IMC é de {imc} valores, \nabaixo do peso.")
elif imc<30:
    print(f"O teu IMC é de {imc} valores, \npeso adequado.")
else:
    print(f"O teu IMC é de {imc} valores, \nobeso.")