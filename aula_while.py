print("**************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
        chute = input("digite um numero: ")
        print("tentativa",rodada,"de",total_tentativas)
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

                rodada = rodada + 1

print("fim do jogo")
