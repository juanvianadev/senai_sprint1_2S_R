trataValores <- function(){
    c <- 1
    quantidade <- 1
    numeros <- c()
    numerosPar <- c()
    numerosImpar <- c()
    
    tryCatch({
        quantidade <- as.integer(readline(prompt = "Digite um valor: ")) 
    }, error={
        print("PRECISA SER UM NUMERO INTEIRO!")
    })

    while(c <= quantidade){
        tryCatch({
            n <- as.double(readline(prompt = paste("Digite o número", c, ": ")))
            append(numeros, n)
            c <- c+1
        },error={
            print("PRECISA SER UM NÚMERO!")
        })
    }

    print(paste("A lista ficou assim", numeros))

    for(n in numeros){
        if(n %% 2 == 0){
            append(numerosPar, n)
        }else{
            append(numerosImpar, n)
        }
    }

    print(paste("Pares:", numerosPar))
    print(paste("Ímpares:", numerosImpar))
    print(paste("Soma pares:", sum(numerosPar)))
    print(paste("Soma ímpares:", sum(numerosImpar)))
    print(paste("Média:", sum(numeros)/quantidade))
}

trataValores()