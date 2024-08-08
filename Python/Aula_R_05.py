#VETOR============================================

#1
vetor = list(range(1,11))
print(vetor)

#2
vetor = list(range(2,21,2))
print(vetor)

#3
vetor = list(range(1,101))
soma = sum(vetor)
print(soma)

#4
vetor = list(range(1,101))
soma = sum(vetor)
print(soma)

#5
from random import randint
vetor = [randint(1, 1000) for _ in range(50)]
maior = max(vetor)
menor = min(vetor)
print(f"Maior: {maior}, Menor: {menor}")

#6
def ePrimo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
    return True

primos = []
num = 2

while len(primos) < 10:
  if ePrimo(num):
    primos.append(num)
  num += 1
print(primos)

#7
import ramdom
vetor = [random.randint(1,100) for _ in range(20)]
vetorInvertido = vetor[::-1]
print(vetor)
print(vetorInvertido)

#MATRIZ============================================

#1
import numpy as np
matriz = np.arange(1,10).reshape(3,3)
print(matriz)

#2
import numpy as np
matrizIdentidade = np.identity(4)
print(matrizIdentidade)

#3
import numpy as np
matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[5,6],[7,8]])
soma = matriz1 + matriz2
print(soma)

#4
multiplicacao = matriz1 @ matriz2
print(multiplicacao)

#5
import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrizT = np.transpose(matriz)
print(matrizT)

#6
import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrizD = np.linalg.det(matriz)
print(matrizD)
matrizD = np.linalg.det(a)

#FATOR============================================

#1
import pandas as pd
cores = pd.Categorical(['vermelho', 'azul', 'verde'])
print(cores)

#2
import pandas as pd
diasSemana = pd.Categorical(['segunda', 'terca', 'quarta', 'quinta', 'sexta'])
print(diasSemana)

#3
import pandas as pd
niveis = pd.Categorical(["Baixo", "Alto", "Médio"], categories = ["Baixo", "Médio", "Alto"], ordered = True)
print(niveis)

#4
import pandas as pd
categorias = pd.Categorical(["Baixo", "Alto", "Médio"], categories = ["Baixo", "Médio", "Alto"], ordered = True)
numeros = categorias.codes
print(numeros)

#5
import pandas as pd
tamanhos = pd.Categorical(["Pequeno", "Médio", "Grande"], categories = ["Pequeno", "Médio", "Grande"], ordered = True)
tamanhos2 = tamanhos.rename_categories({"Pequeno":"Extra pequeno"})
print(tamanhos2)

#6
import pandas as pd
import random
categorias = ["Baixo", "Médio", "Alto"]
vetor = [random.choice(categorias) for _ in range(100)]
fatores = pd.Categorical(vetor, categories = categorias, ordered = True)
frequencias = pd.value_counts(fatores)
print(frequencias)

#7
lista = [1, 2, 3, 4, 5]
print(lista)

#8
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)

#9
lista = [1, 2, 3, 4, 5]
lista.pop(2)
print(lista)

#10
lista = [1, 2, 3, 4, 5]
listaInvertida = lista[::-1]
print(listaInvertida)

#11
matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma = [sum(linha) for linha in matriz]
print(soma)

#TUPLA============================================

#1
tupla = (1,2,3,4,5)
print(tupla)

#2
tupla = (1, 2, 3, 4, 5)
print(tupla[2])

#3
tupla = ((1,2),(3,4),(5,6))
print(tupla)
type(tupla)

#4
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tuplaConcatenada = tupla1 + tupla2
print(tuplaConcatenada)

#5
tupla = (1,2,3,4,5)
existe = 3 in tupla
print(existe)

#6
tupla = (1,2,3,4,5)
indice = tupla.index(4)
print(indice)

#7
dicionario = {"nome":"Ana",
              "idade":"25",
              "cidade":"Sao Paulo"}
print(dicionario)

#8
dicionario = {"nome":"Ana",
              "idade":"25",
              "cidade":"Sao Paulo"}
idade = dicionario["idade"]
print(idade)

#9
dicionario = {"nome":"Ana",
              "idade":"25",
              "cidade":"Sao Paulo"}
profissao = {'profissao': "Engenheira"}
dicionario.update(profissao)
print(dicionario)

#10
dicionario = {"nome":"Ana",
              "idade":"25",
              "cidade":"Sao Paulo"}
dicionario.pop("cidade")
print(dicionario)

#11
dicionario = {
  "pessoa1":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"},
  "pessoa2":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"},
  "pessoa3":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"},
  "pessoa4":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"}
}
print(dicionario)

#12
dicionario = {
    "pessoa1":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"},
  "pessoa2":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"},
  "pessoa3":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"},
  "pessoa4":{"nome":"Ana",
             "idade":"25",
             "cidade":"Sao Paulo"}
}
for chave, valor in dicionario.items():
    print(f"Nome: {valor['nome']}, Idade: {valor['idade']}, Cidade: {valor['cidade']}")

#OPERADORES============================================

#1
soma = 10 + 20
print(soma)

#2
subtracao = 30 - 15
print(subtracao)

#3
mult = 6 * 7
print(mult)

#4
divisao = 81 / 9
print(divisao)

#5
exp =  2 ^ 10
print(exp)

#6
resto = 29 % 5
print(resto)

#LOGICOS============================================

#1
resultado = 8 > 5
print(resultado)

#2
resultado = 3 <= 10
print(resultado)

#3
resultado = 7 > 5 & 7 < 10
print(resultado)

#4
resultado = (12 % 2 == 0) and (12 > 10 & 12 < 5)
print(resultado)

#5
num = 25
resultado = (num % 3 == 0 or num % 5 == 0) and (20 < num < 30)
print(resultado)

#6
def elegivelParaPremio(idade, membroAtivo):
  return(idade > 18 and membroAtivo) or (idade > 60)
print(elegivelParaPremio(25, True))
print(elegivelParaPremio(65, False))
print(elegivelParaPremio(30, False))
