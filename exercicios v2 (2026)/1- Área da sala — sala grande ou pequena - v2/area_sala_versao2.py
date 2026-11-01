#pergunta a largura
while True:
    try:
        largura = float(input("Largura da sala: ").replace(",", "."))
        break
    except ValueError:
        print("Digite um número válido.")


#pergunta o comprimento
while True:
    try:
        comprimento = float(input("Comprimento da sala: ").replace(",", "."))
        break
    except ValueError:
        print("Digite um número válido.")


#unidade de medida
unidade = input("As medidas estão em metros ou centímetros? (m/cm): ").lower()

if unidade in ("cm", "centímetro", "centimetro", "centímetros", "centimetros"):
    largura /= 100
    comprimento /= 100


#calcula area
area = largura * comprimento
print(f"A área da sala é de {area} m².")


#definiçao da sala
if area > 30:
    print("Sala grande.")
else:
    print("Sala pequena.")