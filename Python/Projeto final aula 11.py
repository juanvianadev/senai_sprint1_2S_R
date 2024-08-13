#Imprima os elementos de um dicionário até encontrar um valor específico.

dicionario = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}

valor_indicado = 2

for chave,valor in dicionario.items():
  print(f"Chave: {chave}, Valor{valor}")
  if valor == valor_indicado:
    break
