#1
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida")

#2    
lista = [1,2,3]
try:
  elemento = lista[5]
except IndexError:
  print("Erro: indice fora dos limites da lista")

#3
dicionario = {"a":1,"b":2,"c":3}
try:
  elemento = dicionario["d"]
except KeyError:
  print("Chave inexistente")

#EXTRA
def main():
  try:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    
    resultado = num1 / num2
  except ZeroDivisionError as e:
    print("Erro: Divisao por zero nao permitida")
  
  except ValueError as e:
    print("Nao e possivel dividir valores em String")
  
  except Exeption as e:
    print(f"Ocorreu um erro inesperado. Tente novamente mais tarde!{e}")
    
  else:
    print(f"O resultado da divisao e: {resultado}")
    
  finally:
    print("Programa Finalizado!")

main()

#4
palavra = "abc"
try:
  palavra = int(palavra)
except ValueError:
  print("Erro: Conversao de string pata inteiro falhou!")

#5
dicionario = {"a":[1,2,3],"b":[4,5,6]}
try:
  elemrnto = dicionario["c"][0]
except KeyError:
  print("Erro: Chave inexistente no dicionario")
except IndexError:
  print("Erro: Indice fora dos limites da lista")

#6
