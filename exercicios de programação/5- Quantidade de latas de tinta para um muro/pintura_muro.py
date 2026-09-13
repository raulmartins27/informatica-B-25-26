comprimento = float(input("Qual é o comprimento do muro? "))

while True:
    unidade_comprimento = input("Qual é a unidade de medida do comprimento? (m, cm, mm): ").lower()
    if unidade_comprimento == "m":
        comprimento_m = comprimento
        break
    elif unidade_comprimento == "cm":
        comprimento_m = comprimento / 100
        break
    elif unidade_comprimento == "mm":
        comprimento_m = comprimento / 1000
        break
    else:
        print("Unidade inválida! Digite novamente.")


altura = float(input("Qual é a altura do muro? "))

while True:
    unidade_altura = input("Qual é a unidade de medida da altura? (m, cm, mm): ").lower()
    if unidade_altura == "m":
        altura_m = altura
        break
    elif unidade_altura == "cm":
        altura_m = altura / 100
        break
    elif unidade_altura == "mm":
        altura_m = altura / 1000
        break
    else:
        print("Unidade inválida! Digite novamente.")

area = comprimento_m * altura_m

lata_tinta = 6
qtd_lata = int(area // lata_tinta)
resto = area % lata_tinta
if resto != 0:
    qtd_lata += 1

print(f"Área do muro: {area:.2f} m²")
print(f"Quantidade de latas necessárias: {qtd_lata}")