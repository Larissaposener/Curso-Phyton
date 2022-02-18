print("**************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto = 42

chute = input("digite um numero: ")

print("você digitou ", chute)
numero = int(chute)

if (numero == numero_secreto):
    print("parabéns")
else:
    print("o número não é o mesmo")
