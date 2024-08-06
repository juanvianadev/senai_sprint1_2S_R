#VETOR============================================

vetor = list(range(1,11))
print(vetor)

vetor = list(range(2,21,2))
print(vetor)

vetor = list(range(1,101))
soma = sum(vetor)
print(soma)

vetor = list(range(1,101))
soma = sum(vetor)
print(soma)

from random import randint

vetor = [randint(1, 1000) for _ in range(50)]
maior = max(vetor)
menor = min(vetor)
print(f"Maior: {maior}, Menor: {menor}")

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

import ramdom
vetor = [random.randint(1,100) for _ in range(20)]
vetorInvertido = vetor[::-1]
print(vetor)
print(vetorInvertido)

#MATRIZ============================================

import numpy as np
matriz = np.arange(1,10).reshape(3,3)
print(matriz)

import numpy as np
matrizIdentidade = np.identity(4)
print(matrizIdentidade)

import numpy as np
matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[5,6],[7,8]])
soma = matriz1 + matriz2
print(soma)

multiplicacao = matriz1 @ matriz2
print(multiplicacao)

import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrizT = np.transpose(matriz)
print(matrizT)

import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrizD = np.linalg.det(matriz)
print(matrizD)
matrizD = np.linalg.det(a)
