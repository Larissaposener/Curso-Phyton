print("**************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto = 42

chute = input("\ndigite um numero: ")

print("você digitou ", chute)
numero = int(chute)

acertou = numero == numero_secreto
maior   = numero > numero_secreto
menor   = numero < numero_secreto
if (acertou):
    print("parabéns")
else:
    if(maior):
       print("o número não é o mesmo!! É maior")
    elif(menor):
        print("o número não é o mesmo!! É menor")

print("fim do jogo")
