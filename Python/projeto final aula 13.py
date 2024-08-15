def trataValores():
    c = 1
    quantidade = 0
    numeros = []
    numerosPar = []
    numerosImpar = []
    
    try:
        quantidade = int(input("Digite quantos números você deseja inserir: "))
    except ValueError:
        print("PRECISA SER UM NUMERO INTEIRO!")

    while(c <= quantidade):
        try:
            n = float(input(f"Digite o número {c}: "))
            numeros.append(n)
            c+=1
        except ValueError:
            print("PRECISA SER UM NÚMERO!")

    print(f"A lista ficou assim {numeros}")

    for n in numeros:
        if n % 2 == 0:
            numerosPar.append(n)
        else:
            numerosImpar.append(n)

    print(f"Pares: {numerosPar}")
    print(f"Ímpares: {numerosImpar}")

    print(f"Soma pares: {sum(numerosPar)}")
    print(f"Soma ímpares: {sum(numerosImpar)}")

    print(f"Média: {sum(numeros)/quantidade}")

trataValores()