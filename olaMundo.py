#print por padrão adiciona uma quebra de linha ao final
print("Olá mundo!")
#funcao print com varios argumentos
print("A aranha pequenininha" , "subiu" , "a tromba d'água.")
#argumentos com palavras-chaves
#parâmetro end quando colocado na funcao print, NÃO coloca a quebra de linha e o próximo print começa logo depois 
print("Meu nome é", end="*") 
print("Monty Python")
#parâmetro sep controla o que vai entre múltiplos argumentos dentro do mesmo print
print("Meu nome é", "Python", sep="-") 
print("Monty Python")
#string multiplicada
print("String" * 2)

#Sitacoes com strings usando caracter de escape
print("Eu gosto \"Monty Python\"")
print('Eu gosto "Monty Python"')
print("\"Eu sou\"\n\"\"aprendiz\"\"\n\"\"\"Python\"\"\"")

#uso de apostrofos
print('I\'m Monty Python.')




#Numeros inteiros
#conversao para numero octal
print(0o123)
#gexadeciaml
print(0x123)
print(4)

#numeros decimais float
print(0.4)
print(.4)#pode omitir o 0 nessas situações

#potencia usa-se 10 implicito - BASE, valor na frente do (e) / expoente valor apos o (e) e deve ser numero inteiro
print(3e8) #Três vezes dez à potência de oito.

#comportamento de floats pequenos/ ou grandes
print(0.0000000000000000000001)

#valores booleanos true 1 - 0 false
print(True > False)
print(True < False)

