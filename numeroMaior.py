#recebe dois numeros
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

#escolha o maior
if num1 > num2:
    numMaior = num1
else:
    numMaior = num2

#imprime resultado
print("O numero maior é: ", numMaior)

#outra maneira de fazer
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

numMaior = num1 #assume que o mair é o primeiro

#escolha o maior
if num2 > numMaior: numMaior = num2
if num3 > numMaior: numMaior = num3

#imprime resultado
print("O numero maior é: ", numMaior)


#funcoes em python que ajudam
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

numMaior = max(num1, num2, num3)
numMenor = min(num1, num2, num3)

print("O numero maior é: ", numMaior)
print("O numero menor é: ", numMenor)