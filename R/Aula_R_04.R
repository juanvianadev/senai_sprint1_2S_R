#VETOR============================================

#1
vetor <- 1:10
print(vetor)

#2
vetor <- seq(2,2, by=2)
print(vetor)

#3
vetor <- 1:100
soma <- sum(vetor)
print(soma)

#4
vetor <- sample(1:1000, 50, replace = TRUE)
maior <- max(vetor)
menor <- min(vetor)
print(paste("Maior:", maior, "Menor:", menor))

#5
ePrimo <- function(n){
  if(n <= 1){
    return(FALSE)
  }
  for(i in 2:sqrt(n)){
    if(n %% i == 0){
      return(FALSE)
    }
  }
  return(TRUE)
}

primos <- c()
num <- 2
while(length(primos)<10){
  if(ePrimo(num)){
    primos <- c(primos, num)
  }
  num <- num +1
}

print(primos)

#6
vetor <- sample(1:100, 20, replace = TRUE)
vetorInvertido <- rev(vetor)
print(vetor)
print(vetorInvertido)

#MATRIZ============================================

#1
matriz <- matrix(1:9, nrow = 3, ncol = 3)
print(matriz)

#2
matrizIdentidade <- diag(4)
print(matrizIdentidade)

#3
matriz1 <- matrix(c(1,2,3,4), nrow = 2, ncol = 2)
print(matriz1)
matriz2 <- matrix(c(5,6,7,8), nrow = 2, ncol = 2)
print(matriz2)
soma <- matriz1 + matriz2
print(soma)

#4
multiplicacao <- matriz1 %*% matriz2
print(multiplicacao)

#5
matriz <- matrix(1:9, nrow = 3, ncol = 3)
matrizT <- t(matriz)
print(matrizT)

#6
matriz <- matrix(1:9, nrow = 3, ncol = 3)
matrizD <- det(matriz)
print(matrizD)

#FATOR============================================

#1
cores <- factor(c("vermelho", "azul", "verde"))
print(cores)

#2
diasSemana <- factor(c("segunda", "terca", "quarta", "quinta", "sexta"))
print(diasSemana)

#3
niveis <- factor(c("Baixo", "Alto", "Médio"), levels = c("Baixo", "Médio", "Alto"), ordered = TRUE)
print(niveis)

#4
categorias <- factor(c("Baixo", "Alto", "Médio"), levels = c("Baixo", "Médio", "Alto"), ordered = TRUE)
numeros <- as.numeric(categorias)
print(numeros)

#5
tamanhos <- factor(c("Pequeno", "Médio", "Grande"), levels=c("Pequeno", "Médio", "Grande"), ordered = TRUE)
levels(tamanhos) [levels(tamanhos) == "Pequeno"] <- "Extra pequeno"
print(tamanhos)

#6
set.seed(123)
categorias <- c("Baixo", "Médio", "Alto")
vetor <- sample(categorias, 100, replace = TRUE)
fatores <- factor(vetor, levels = categorias, ordered = TRUE)
frequencias <- table(fatores)
print(frequencias)

#7
lista <- list(1, 2, 3, 4, 5)
print(lista)

#8
lista <- list(1, 2, 3, 4, 5)
lista[[6]] <- 6
print(lista)

#9
lista <- list(1, 2, 3, 4, 5)
lista <- lista[-3]
print(lista)

#10
lista <- list(1, 2, 3, 4, 5)
listaInvertida <- rev(lista)
print(listaInvertida)

#11
matriz <- list(c(1,2,3),c(4,5,6),c(7,8,9 ))
soma <- sapply(matriz, sum)
print(soma)

#TUPLA============================================

#1
tupla <- list(1, 2, 3, 4, 5)
print(tupla)

#2
tupla <- list(1, 2, 3, 4, 5)
print(tupla[3])

#3
tupla <- list(list(1,2),list(3,4),list(5,6))
print(tupla)

#4
tupla1 <- list(1,2,3)
tupla2 <- list(4,5,6)
tuplaConcatenada <- c(tupla1, tupla2)
print(tuplaConcatenada)

#5
tupla <- list(1,2,3,4,5)
existe <- 3 %in% tupla
print(existe)

#6
tupla <- list(1,2,3,4,5)
indice <- which(unlist(tupla) == 4)
print(indice)

#7
dicionario <- list(nome="Ana", idade=25, cidade="Sao Paulo")
print(dicionario)

#8
dicionario <- list(nome="Ana", idade=25, cidade="Sao Paulo")
idade <- dicionario$idade
print(idade)