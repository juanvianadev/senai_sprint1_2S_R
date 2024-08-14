#1
tryCatch({
  resultado <- 10/0
}, error = function(e){
  print("Erro: Divisão por zero não é permitida")
})

#2
lista <- c(1,2,3)
tryCatch({
  elemento <- lista[5]
}, error = function(e){
   print("Erro: indice fora dos limites da lista")
})

#3
dicionario <- list(a=1, b=2, c=3)
tryCatch({
  elemento <- dicionario[["d"]]
},error = function(e){
  print("Erro: essa chave não existe no dicionário")
})

#4
palavra <- "abc"
tryCatch({
  palavra <- as.integer(palavra)
},warning = function(w){
  print("Erro: Conversao de string pata inteiro falhou!")
})

#5
dicionario <- list(a=c(1,2,3), b=c(4,5,6))
tryCatch({
  dicionario <- dicionario[["c"]][1]
},error = function(e){
  if(inherits(e,"simpleError")){
    print("Erro: Chave inexistente no dicionario ou indice fora dos limites da lista")
  }
})

#6
