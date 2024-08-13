#Imprima os elementos de um dicionário até encontrar um valor específico.

valor_indicado = 2

dicionario <- list(a=1, b=2, c=3, d=4, e=5, f=6)
for(chave in names(dicionario)){
  print(paste("Chave", chave, "Valor", dicionario[[chave]]))
  if(dicionario[[chave]] == valor_indicado){
    break
  }
}