#VETOR============================================
vetor <- 1:10
print(vetor)

vetor <- seq(2,2, by=2)
print(vetor)

vetor <- 1:100
soma <- sum(vetor)
print(soma)

vetor <- sample(1:1000, 50, replace = TRUE)
maior <- max(vetor)
menor <- min(vetor)
print(paste("Maior:", maior, "Menor:", menor))

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

vetor <- sample(1:100, 20, replace = TRUE)
vetorInvertido <- rev(vetor)
print(vetor)
print(vetorInvertido)

#MATRIZ============================================

matriz <- matrix(1:9, nrow = 3, ncol = 3)
print(matriz)

matrizIdentidade <- diag(4)
print(matrizIdentidade)

matriz1 <- matrix(c(1,2,3,4), nrow = 2, ncol = 2)
print(matriz1)
matriz2 <- matrix(c(5,6,7,8), nrow = 2, ncol = 2)
print(matriz2)
soma <- matriz1 + matriz2
print(soma)

multiplicacao <- matriz1 %*% matriz2
print(multiplicacao)

matriz <- matrix(1:9, nrow = 3, ncol = 3)
matrizT <- t(matriz)
print(matrizT)

matriz <- matrix(1:9, nrow = 3, ncol = 3)
matrizD <- det(matriz)
print(matrizD)
