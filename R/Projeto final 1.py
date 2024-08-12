#Crie um sistema simples de gerenciamento de contatos que permita adicionar novos 
#contatos, remover contatos e listar todos os contatos com seus detalhes. O
#sistema deve utilizar variáveis e operações diretamente, sem a utilização de funções.

contatos = {
  "contato" : {
    "nome": "Juan",
    "numero": "11999999999",
    "estado": "SP"
  }
}

#adicionando
contatos["contato2"] = {
    "nome": "Joao",
    "numero": "11999999999",
    "estado": "SP"
}

print(contatos)

#apagando
del contatos["contato2"]

print(contatos)

#listando
for chave, valor in contatos.items():
    print(f"Nome: {valor['nome']}, Numero: {valor['numero']}, Estado: {valor['estado']}")
