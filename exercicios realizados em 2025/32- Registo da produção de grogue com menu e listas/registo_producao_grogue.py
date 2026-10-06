#menu
while True:
    print("REGISTO DA PRODUÇÃO DE GROGUE NA ILHA DE SANTIAGO E DE SANTO ANTÃO.")
    print("O QUE DESEJA FAZER?")
    print("1. INTRODUZIR  OS DADOS")
    print("2. CONSULTAR UMA POSIÇÃO NA LISTA")
    print("3. ALTERAR O VALOR DE UM ELEMENTO DA LISTA")
    print("4. CONSULTAR O TOTAL DE PRODUÇÃO POR ILHA")
    print("5. CONSULTAR A MÉDIA DA PRODUÇÃO POR ILHA")
    print("6. JUNTAR AS DUAS LISTAS")
    print("7. CONSULTAR QUAL FOI A ILHA QUE PRODUZIU MAIS")
    print("8. SAIR")
    opcao_menu=-1
    while opcao_menu<1 or opcao_menu>8:
        opcao_menu=int(input("\nEscolha uma opçao entre 1 e 8: "))
    produçao_ilha_santiago=[]
    produçao_ilha_snt_antao=[]

    #opcao 1 (introduzir dados):
    if opcao_menu==1:
        #producao ilha de santiago
        produçao_ilha_santiago=-1
        while produçao_ilha_santiago<0:
            produçao_ilha_santiago=int(input("\nQuantos produtores existem na ilha de Santiago? "))
        for produtor in range(produçao_ilha_santiago):
            qtd_producao_santiago=-1
            while qtd_producao_santiago<0:
                qtd_producao_santiago=float(input("Qual é a quantidade em litros produzida" \
                f"pelo produtor {produtor+1}? "))
                produçao_ilha_santiago.append(qtd_producao_santiago)


                #contabilizar qtd elementos da lista A:
                for elemento in qtd_producao_santiago:
                    contagem_A+=1

        
        #producao ilha do Santo Antao
        produçao_ilha_snt_antao=-1
        while produçao_ilha_snt_antao<0:
            produçao_ilha_snt_antao=int(input("\nQuantos produtores existem na ilha do Santo Antao? "))
        for produtores in range(produçao_ilha_snt_antao):
            qtd_producao_santo_antao=-1
            while qtd_producao_santo_antao<0:
                qtd_producao_santo_antao=float(input("Qual é a quantidade em litros produzida" \
                f"pelo produtor {produtores+1}? "))
                produçao_ilha_snt_antao.append(qtd_producao_santo_antao)


                #contabilizar qtd elementos da lista B:
                for elementos in qtd_producao_santo_antao:
                    contagem_B+=1




    #opcao 2(consultar uma posiçao na lista):
    if opcao_menu==2:
        print("Escolhe uma lista das seguintes ilhas" \
        "\n para consultar uma posiçao:")
        print("1. Ilha de Santiago")
        print("2. Ilha do Santo Antao")


        escolha_de_lista=-1
        while escolha_de_lista<1 or escolha_de_lista>2:
            escolha_de_lista=int(input("Qual ilha? "))
        if escolha_de_lista==1:
            lista=produçao_ilha_santiago
            contagem=contagem_A
        else:
            lista=produçao_ilha_snt_antao
            contagem=contagem_B

    
        pos=-1
        if pos<1 or pos>contagem:
            pos=int(input("Qual é a posiçao que deseja verificar? "))
        else: print("Valor inválida, digite um número" \
        f"\n entre 1 e {contagem}.")

        print(f"Valor na posiçao {pos}: {lista[pos]}")




    #opcao 3 (alterar o valor de um elemento na lista):
    if opcao_menu==3:
        print("Escolha uma lista das seguintes ilhas" \
        "\n para alterar o valor:")
        print("1. Ilha de Santiago")
        print("2. Ilha do Santo Antao")


        escolha_de_lista=-1
        while escolha_de_lista<1 or escolha_de_lista>2:
            escolha_de_lista=int(input(" "))
        if escolha_de_lista==1:
            lista=produçao_ilha_santiago
            contagem=contagem_A
        else:
            lista=produçao_ilha_snt_antao
            contagem_B

        pos=-1
        if pos<1 or pos>contagem:
            pos=int(input("Qual é a posiçao em que deseja alterar o valor? "))
        else: print("Valor inválida, digite um número" \
        f"\n entre 1 e {contagem}.")

        novo_valor=-1    
        while novo_valor<-1:
            novo_valor=float(input("Qual é o novo valor que deseja introduzir? "))
        lista[pos]=novo_valor




    #opcao 4 (consultar o total de produçao por ilha):
    if opcao_menu==4:
        total_Santiago=0
        total_Santo_Antao=0

        for valor in produçao_ilha_santiago:
            total_Santiago+=valor

        for valor in produçao_ilha_snt_antao:
            total_Santo_Antao+=valor

        print(f"Total de produçao na ilha de Santiago: {total_Santiago} litros. ")
        print(f"Total de produçao na ilha do Santo Antao: {total_Santiago} litros. ")



    #opcao 5 (Consultar a média da produçao por ilha):
    if opcao_menu==5:
        total_Santiago=0
        media_Santiago=0
        total_Santo_Antao=0
        media_Santo_Antao=0

        #ilha de Santiago:
        for valor in produçao_ilha_santiago:
            total_Santiago+=valor
        media_Santiago=total_Santiago/contagem_A
        

        #ilha do Santo Antao:
        for valor in produçao_ilha_snt_antao:
            total_Santo_Antao+=valor
        media_Santo_Antao=total_Santo_Antao/contagem_B
        

        print(f"A média de produçao na ilha de Santiago é de: {media_Santiago} litros.")
        print(f"A média de produçao na ilha do Santo Antao é de: {media_Santo_Antao} litros.")




    #opcao 6 (Juntar as duas listas):
    if opcao_menu==6:
        lista_mesclada=[]
        lista_mesclada= produçao_ilha_santiago + produçao_ilha_snt_antao

        print(f"As duas listas combinadas: {lista_mesclada}. ")




    #opcao 7 (Consultar qual foi a lista que produziu mais):
    if opcao_menu==7:
        if total_Santiago>total_Santo_Antao:
            print("A ilha de Santiago produziu mais com um total" \
            f"\nde {total_Santiago} litros de grogue.")
        elif total_Santo_Antao>total_Santiago:
            print("A ilha do Santo Antao produziu mais com um" \
            f"\ntotal de {total_Santo_Antao} litros de grogue. ")
        else:
            print("Ambas as ilhas tiveram a mesma quantidade " \
            f"\nde produçao com {total_Santo_Antao} litros de grogue. ")




    #opcao 8 (sair)
    if opcao_menu==8:
        print("Programa terminado. Obrigado pela sua visita, volte sempre!")
        print("....")
        print("....")
        print("A sair...")
        break