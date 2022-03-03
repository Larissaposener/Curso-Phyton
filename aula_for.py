import random
print("**************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto = random.randrange(0,101)
total_tentativas = 3

print(numero_secreto)

for rodada in range(1, total_tentativas + 1):
        chute = input("\ndigite um numero entre 1 a 100: ")
        print("tentativa {} de {}".format(rodada,total_tentativas))
        print("você digitou ", chute)
        numero = int(chute)

        if(numero < 1 or numero > 100):
            print("chute não pode ser menor que 1 ou maior que 100")
            continue
        acertou = numero == numero_secreto
        maior   = numero > numero_secreto
        menor   = numero < numero_secreto
        if (acertou):
            print("parabéns")
            break
        else:
            if(maior):
               print("o número não é o mesmo!! É maior")
            elif(menor):
                print("o número não é o mesmo!! É menor")



print("fim do jogo")
