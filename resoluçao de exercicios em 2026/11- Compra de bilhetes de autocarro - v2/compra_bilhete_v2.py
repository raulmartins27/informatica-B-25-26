def validar_qtd_minimo(pergunta, minimo):
    while True:
        try:
            valor = int(input(pergunta).strip())

            if valor < minimo:
                print(
                    f"Valor inválido.\n"
                    f"O valor deve ser igual ou superior a {minimo}."
                )
            else:
                return valor

        except ValueError:
            print("Valor inválido, tente novamente. ")


def validar_destino(pergunta, minimo, maximo):
    while True:
        try:
            valor = int(input(pergunta).strip())

            if valor < minimo or valor > maximo:
                print(
                    f"Valor inválido.\n"
                    f"Digite um valor entre {minimo} e {maximo}."
                )
            else:
                return valor

        except ValueError:
            print("Valor inválido, tente novamente.")


def main():
    precos_destino = {
        1: ("Assomada", 250),
        2: ("Praia_Baixo", 300),
        3: ("Tarrafal", 400)
    }

    for numero, (destino, preco) in precos_destino.items():
        print(f"{numero} - {destino}: {preco}$")

    qtd_bilhetes = validar_destino(
        "Deseja comprar quantos bilhetes? "
        "(digite 1, 2 ou 3): ",
        1,
        3
    )

    totais = {
        1: 0,
        2: 0,
        3: 0
    }

    for numero_bilhete in range(1, qtd_bilhetes + 1):
        destino = validar_destino(
            f"Qual é o destino do bilhete {numero_bilhete}? ",
            1,
            3
        )

        preco = precos_destino[destino][1]
        totais[destino] += preco

    total_geral = sum(totais.values())

    print(f"\nTotal Assomada: {totais[1]}$")
    print(f"Total Praia_Baixo: {totais[2]}$")
    print(f"Total Tarrafal: {totais[3]}$")
    print(f"Total geral: {total_geral}$")


main()