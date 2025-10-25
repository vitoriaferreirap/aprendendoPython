# Troca de valores entre variáveis
x = 1
y = 2
z = x     
x = y     
y = z      
print(x, y)  

# Entrada de strings e concatenação
x = input()   
y = input()   
print(x + y)  # concatena as strings pois é um caracter de string

# Entrada de inteiros e divisão normal (float)
x = int(input())
y = int(input())
x = x / y         # divisão normal resposta float
y = y / x         # divisão normal resposta float
print(y)          # imprime float

# Entrada de inteiros e operação módulo
x = int(input())
y = int(input())
x = x % y         # resto da divisão em inteiro
x = x % y         # se x < y, x permanece igual
y = y % x         # resto da divisão e inteiro
print(y)          # imprime resultado

# Entrada de string e inteiro, repetição de string
x = input()       # string
y = int(input())  # inteiro
print(x * y)      # repete a string y vezes

# Atribuição múltipla e print com separador
z = y = x = 1
print(x, y, z, sep='*')  

# Combinação de operadores
x = 1 / 2 + 3 // 3 + 4 ** 2  
print(x)          

# Entrada de inteiros e soma
x = int(input())
y = int(input())
print(x + y)      # imprime soma dos dois inteiros
