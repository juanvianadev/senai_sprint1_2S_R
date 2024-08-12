#Crie um sistema simples de gerenciamento de contatos que permita adicionar novos 
#contatos, remover contatos e listar todos os contatos com seus detalhes. O
#sistema deve utilizar variáveis e operações diretamente, sem a utilização de funções.

contatos <- list(
  "pessoa1"<-list(nome="Juan", numero="11999999999", cidade="SP")
)

contatos$pessoa2 <- list(nome="Joao", numero="11999999999", cidade="SP")
print(dicionario)

dicionario$pessoa2 <- NULL
print(dicionario)

for(pessoa in dicionario){
  print(paste("Nome:", pessoa$nome, "Idade", pessoa$idade, "Cidade", pessoa$cidade))
}