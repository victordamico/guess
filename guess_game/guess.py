#o Programa irar gerar um numero Aleatorio de 1 a 10 

from random import randint

def gerador(b):
    return randint(1, b)


#Aparecer Bem-Vindo para os jogadores 

def bemvindo():
    print("-=" *30)
    print(" " *22, "Bem-Vindo", " " * 20)
    print("-=" *30)
    print("\n- Nesse jogo você tera que palpitar qual é o número que foi gerado")

def line():
    print("_" *80)


bemvindo()


#Nivel de Dificuldade Facil, Medio e Dificil

nivel = input("Escolha a Dificuldade \033[32mFacil\033[32m, \033[33mMedio\033[33m, \033[35mDificil\033[35m \033[37m:").title()
if nivel == "Facil\033[37m":
    b = 5
    chances = 3
    print(f" Você escolheu o modo Fácil aqui voce tera que acertar um número de 1 a 5 \n Você tem {chances} Chances\n")
elif nivel == "Medio": 
    b = 10
    chances = 4
    print(f"\n Você escolheu o modo Medio aqui voce tera que acertar um número de 1 a 10 \n Você tem {chances} Chances\n")
else:
    b = 50
    chances = 7
    print(f"\n Você escolheu o modo Dificio aqui voce tera que acertar um número de 1 a 50 \n Você tem {chances} Chances\n")

numero_secreto = gerador(b)



#O jogador podera ter somente 3 tentativa de acertar o numero gerado, Criar um 'Contador'
contador = 0
pontos = 100
while chances != contador or numero_secreto == palpite :
    palpite = int(input("Digite seu Palpite: "))
    if numero_secreto == palpite:
        line()
        print("\n\033[32m Parabéns Você acertou\033[m\n")
        print(f' O número secreto era: {numero_secreto}\n')
        print(f' Sua Pontuação {pontos}p')
        line()
        break
    contador += 1
    pontos -= 10

#mostrar o numero secreo 

#falar que vc perdeu 

if chances == contador and numero_secreto != palpite:
    pontos = 0
    line()
    print("\n\033[35m GAME OVER\033[m\n")
    print(f' O número secreto era: {numero_secreto}\n')
    print(f' Sua Pontuação {pontos}p')
    line() 




