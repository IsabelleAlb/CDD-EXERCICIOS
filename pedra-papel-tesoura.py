opcao = ['pedra', 'papel', 'tesoura']
repeat = "sim"

while repeat in "simSIM":
    ponto_jogador1 = 0
    ponto_jogador2 = 0
    for x in range(3):
        jogador1 = input("\nJogador 1, escolha uma opção entre pedra, papel e tesoura: ")
        jogador2 = input("Jogador 2, escolha uma opção entre pedra, papel e tesoura: ")

        if jogador1 == jogador2:
            print("Empate!!")
            ponto_jogador1 += 1
            ponto_jogador2 += 1
            print(f"o placar está {ponto_jogador1} para o jogador 1\n{ponto_jogador2} para o jogador 2")


        elif jogador1 != jogador2:
            if jogador1 == opcao[0] and jogador2 == opcao[2]:
                print("Ponto para o Jogador 1 \n")
                ponto_jogador1 += 1
                print(f"O placar está:\n{ponto_jogador1} para o jogador 1\n{ponto_jogador2} para o jogador 2")

            elif jogador1 == opcao[2] and jogador2 == opcao[1]:
                print("Ponto para o Jogador 1 \n")
                ponto_jogador1 += 1
                print(f"O placar está:\n{ponto_jogador1} para o jogador 1\n{ponto_jogador2} para o jogador 2")

            elif jogador1 == opcao[1] and jogador2 == opcao[0]:
                print("Ponto para o Jogador 1 \n")
                ponto_jogador1 += 1
                print(f"O placar está:\n{ponto_jogador1} para o jogador 1\n{ponto_jogador2} para o jogador 2")

            else:
                print("Ponto para o Jogador 2 \n")
                ponto_jogador2 += 1
                print(f"O placar está:\n{ponto_jogador1} para o jogador 1\n{ponto_jogador2} para o jogador 2")

    if ponto_jogador1 > ponto_jogador2:
        print("Vitória do Jogador1!!")

    elif ponto_jogador1 < ponto_jogador2:
        print("Vitória do Jogador2!!!!!!")

    else:
        print("empateee!!!!")

    repeat = input("\nDeseja jogar novamente? sim/não: ")
