import random

def jogar():
        print("**************************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("**************************************")

        numero_secreto = random.randrange(0,101)
        total_tentativas = 0
        pontos = 1000

        print("qual o nível de dificuldade?")
        print("1 - facil    2 - medio   3 - dificil")
        nivel = int(input("defina o nivel: "))

        if(nivel == 1):
            total_tentativas = 20
        elif(nivel == 2):
            total_tentativas = 10
        else:
            total_tentativas = 5

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
                    print("parabéns você acertou e fez {} pontos".format(pontos))
                    break
                else:
                    if(maior):
                       print("o número não é o mesmo!! É maior")
                    elif(menor):
                        print("o número não é o mesmo!! É menor")
                    pontos_perdidos = abs(numero_secreto - numero)
                    pontos = pontos - pontos_perdidos



        print("fim do jogo")
if(__name__=="__main__"):
    jogar()