#1
def soma(a,b):
    return a+b
print(soma(3,5))

#2
def par(numero):
  return numero % 2 == 0
print(par(11))

#
def media(lista):
  return sum(lista) / len(lista)
print(media([1,2,3,4,5]))

#4
def somaMatriz(matriz):
  return sum(sum(linha) for linha in matriz)
matriz = [[1,2,3],[4,5,6],[7,8,9]]  
print(somaMatriz(matriz))

#5
def palindromo(palavra):
  return palavra == palavra[::-1]
print(palindromo("ovo"))
print(palindromo("bala"))

#6
def contaVogais(string):
  vogais = "aeiou"
  return sum(1 for char in string if char.lower() in vogais)
print(contaVogais("Python"))

#7
matriz1 = [[1, 2],[3,4]]
matriz2 = [[5, 6],[7,8]]

print(matriz1)
print(matriz2)

def produto_matrizes(matriz_a, matriz_b):
  resultado = [[sum(a * b for a,b in zip(linha_a,coluna_b)) for coluna_b in zip(*matriz_b)] for linha_a in matriz_a]
  return resultado
print(produto_matrizes(matriz1,matriz2))

#8  
def fatorial(n):
  resultado = 1
  if n == 0:
    return 1
  return n * fatorial(n - 1)

print(fatorial(5))

#9
def somaN(n):
  if n == 0:
    return 0
return n + somaN(n-1)
print(somaN(10))
