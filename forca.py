# forca.py

import random


def jogar():

    mensagem_introducao()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)

    letras_utilizadas = []

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # while (not enforcou and not acertou):
    while True:

        chute = pedir_chute()

        if (chute in letras_utilizadas):
            print("Essa letra ja foi utlizada!!!")
            print(letras_utilizadas)
            continue

        if (chute in palavra_secreta):
            letras_utilizadas.append(chute)
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            letras_utilizadas.append(chute)
            erros += 1
            desenha_forca(erros)

        # enforcou = erros == 6
        # acertou = "_" not in letras_acertadas
        # print(letras_acertadas)

        if (erros == 7):
            break
        if ("_" not in letras_acertadas):
            break

        print(letras_acertadas)

    # if (acertou):
    #     print("Voce ganhou!!")
    # else:
    #     print("Voce perdeu :(")

    if ("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def mensagem_introducao():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pedir_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()  # tratar entrada (tirar espaços da entrada, deixar maiusculo)
    return chute


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra):
    print("A palavra era {}".format(palavra))
    print("Você perdeu!")

if (__name__ == "__main__"):  #sempre colocar no fim do arquivo
    jogar()

