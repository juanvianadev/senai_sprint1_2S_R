#1
soma <- function(a,b){
  return (a+b)
}
print(soma(1,2))

#2
par <- function(numero){
  return(numero %% 2 == 0)
}
print(par(10))

#3
media <- function(lista){
  return(mean(lista))
}
print(media (c(1,2,3,4,5)))

#4
soma_matriz <- function(matriz){
  return(sum(matriz))
}
matriz <- matrix(1:9, nrow = 3, ncol = 3)
print(soma_matriz(matriz))

#5
palindromo <- function(palavra){
  return(palavra == paste(rev(strsplit(palavra, NULL)[[1]]),collapse = ""))
}
print(palindromo("ovo"))
print(palindromo("bala"))

#6
contaVogais <- function(string){
  vogais <- c("a","e","i","o","u")
  return(sum(tolower(strsplit(string,NULL)[[1]]) %in% vogais))
}
print(contaVogais("Python"))

#7
matriz1 <- matrix(c(1,2,3,4), nrow = 2, ncol = 2)
matriz2 <- matrix(c(5,6,7,8), nrow = 2, ncol = 2)

print(matriz1)
print(matriz2)

prodMatriz <- function(matriz1,matriz2){
  return(matriz1 %*% matriz2)
}

print(prodMatriz(matriz1,matriz2))

#8
fatorial <- function(n){
    resultado <- 1
    if(n == 0){
      return(1)
}
    return(n * fatorial(n - 1))
} 
print(fatorial(5))

#9
somaN <- function(n){
  if(n == 0){
    return(0)
  }
  return(n + somaN(n - 1))
} 
print(somaN(10))