#1
x = float(input("Digite o valor para x: "))
y = 1 / ( x + 1 / ( x + 1 / (x + 1  / x)))
print("y =", y)

#2 avaliar a hora de término de um período
horas = int(input("Hora de inicio: ")) #so aceita inteiros
minu = int(input("Minutos: "))
duracao = int(input("Duracao do evento em minutos: "))

#encontrar a duracao de total de minutos
minu += duracao
#ver se há horas nos minutos
horas += minu // 60 # //divisao numeros inteiros - teremos o total de hora correto

minu = minu % 60 # resto da divisao por 60 é o restante dos minutos que nao sao horas
horas = horas % 24 # se passar de 24, volta para 0-23

print(horas,":", minu, sep='')

#solicitacao para encerrar o programa 
print("\nPressione Enter para finalizar o programa.")
input()
print("O FIM.")