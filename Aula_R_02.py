nome = "Juan"
idade = 21
altura = 1.83
brasileiro = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Brasileiro:", brasileiro)

print(type(nome))
print(type(idade))
print(type(altura))
print(type(brasileiro))

PI = 3.14159

mensagem = "Olá"
print(mensagem)
print(type(mensagem))

numero = 100
print(type(numero))

from datetime import datetime
data_atual = datetime.now()
print(data_atual)

from enum import Enum

class DiasDaSemana(Enum):
  Segunda = 1
  Terca = 2
  Quarta = 3
  Quinta = 4
  Sexta = 5

print(DiasDaSemana.Quarta.value)
print(DiasDaSemana.Quarta.name)
