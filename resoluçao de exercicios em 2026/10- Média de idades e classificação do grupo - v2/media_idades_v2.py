def validar_valor(pergunta, minimo):
    while True:
        try:
            quantidade = int(input(pergunta).strip())
            if quantidade < minimo:
                print("Valor invalido, Digite um valor" \
                f"\nigual ou superior a {minimo}")
            else:
                return quantidade
        except ValueError:
            print("Valor inválido, tente novamente.")

qtd_pessoas = validar_valor("Qual é a quantidade? ", 1)

soma_idades=0
for pessoas in range(qtd_pessoas):
    idade = validar_valor(f"Qual é a idade da pessoa {pessoas+1}? ", 0)
    soma_idades+=idade


media= soma_idades / qtd_pessoas
print(f"Média: {media:.2f}")
if media<18:
    print("Grupo de jovens")
elif media<40:
    print("Grupo de adultos")
else:
    print("Grupo sénior")
