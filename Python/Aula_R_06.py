#1
numero = 5

if numero > 0:
  print("O numero e positivo")
else:
  print("O numero e negativo")

#2  
palavra = "banana"

if len(palavra) > 5:
  print("A palavra tem mais que cinco letras")
else:
  print("A palavra tem menos que cinco letras")

#3
ano = 2024
if(ano % 4 == 0 and ano % 100 != 0):
  print("Ano e bissexto")
else:
  print("Ano nao e bissexto")
  
#4
numero = 15
if(numero >= 10 and numero <= 20):
  print("O numero esta entre 10 e 20")
else:
  print("O numero nao esta entre 10 e 20")

#5
palavra = "palavra123"
if any(c.isalpha() for c in palavra) and any(c.isdigit() for c in palavra):
  print("A palavra contem letras e numeros")
else:
  print("A palavra nao contem letras e numeros")

#6
idade = 25
if idade < 13:
  print("Crianca")
elif idade < 18:
  print("Adolescnte")
elif idade < 60:
  print("Adulto")
else:
  print("Idoso")

#7
mes = 5
if mes in [6,7,8]:
  print("Inverno")
elif mes in [9,10,11]:
  print("Primavera")
elif mes in [12,1,2]:
  print("Verao")
elif mes in [2,4,5]:
  print("Outono")
else:
  Print("Mes invalido")

#8
for i in range(1,11):
  print(i)

#9
lista = [1,2,3,4,5]
for elemento in lista:
  print(elemento)

#10
dicionario = {"a":1,"b":2,"c":3}
for chave,valor in dicionariorio.items():
  print(f"Chave: {chave}, Valor{valor}")
  
for c in dicionario: print(dicionario[c])

#11
i = 1
while i <= 10:
  print(i)
  i += 1
  
#12
