from uteis import cores
from uteis.entradas import verifica_Jogada


def titulo():
    print(f'{cores["negrito"]}={cores["limpa"]}' * 30)
    print(f'{cores["cinza"]}{"  BEM VINDO AO JOGO DA VELHA":^20}{cores["limpa"]}')
    print(f'{cores["negrito"]}={cores["limpa"]}' * 30)


def exibe_Tabuleiro(jogo):
    print(f'{cores["negrito"]}={cores["limpa"]}' * 30)
    print(f'{cores["negrito"]}     {"A":^5}{"B":^5}{"C":^5}{cores["limpa"]}\n')
    for linha in range(0, 3):
        print(f'{cores["negrito"]}{linha + 1:<5}{cores["limpa"]}', end='')
        for coluna in range(0, 3):
            if jogo[linha][coluna] == 'X':
                print(cores['amarelo'], end='')
            elif jogo[linha][coluna] == 'O':
                print(cores['roxo'], end='')
            print(f'{jogo[linha][coluna]:^5}', end='')
            print(cores['limpa'], end='')
        print()


def insere_Jogada(jogo, jogada, jogador):
    linha = coluna = 0
    if 'A' in jogada:
        coluna = 0
    elif 'B' in jogada:
        coluna = 1
    elif 'C' in jogada:
        coluna = 2
    if '1' in jogada:
        linha = 0
    elif '2' in jogada:
        linha = 1
    elif '3' in jogada:
        linha = 2

    if jogo[linha][coluna] != '-':
        print(f'{cores["vermelho"]}Campo ocupado{cores["limpa"]}')
        return False
    else:
        if jogador['atual'] == 'jogador_1':
            jogo[linha][coluna] = 'X'
        else:
            jogo[linha][coluna] = 'O'
        return True


def realiza_Jogada(game, players):
    while True:
        if players['atual'] == 'jogador_1':
            print(cores["amarelo"], end='')
        else:
            print(cores['roxo'], end='')

        escolha = str(
            input(f'{players[players["atual"]]}, onde deseja marcar? [ex:A1]{cores["limpa"]}')).upper().strip()[:2]

        if verifica_Jogada(escolha):
            if insere_Jogada(game, escolha, players):
                if players['atual'] == 'jogador_1':
                    players['atual'] = 'jogador_2'
                else:
                    players['atual'] = 'jogador_1'
                break


def confereVitoria(game, players):
    xganha = ['X', 'X', 'X']
    oganha = ['O', 'O', 'O']
    diagonal1 = [game[0][0], game[1][1], game[2][2]]
    diagonal2 = [game[0][2], game[1][1], game[2][0]]
    coluna1 = [game[0][0], game[1][0], game[2][0]]
    coluna2 = [game[0][1], game[1][1], game[2][1]]
    coluna3 = [game[0][2], game[1][2], game[2][2]]
    empatou = 1
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if game[linha][coluna] == '-':
                empatou = 0

    if game[0] == xganha or game[1] == xganha or game[
        2] == xganha or diagonal1 == xganha or diagonal2 == xganha or coluna1 == xganha or coluna2 == xganha or coluna3 == xganha:
        exibe_Tabuleiro(game)
        print(f'{cores["amarelo"]}Parabéns {players["jogador_1"]}! Você ganhou o jogo!!!!!{cores["limpa"]}')
    elif game[0] == oganha or game[1] == oganha or game[
        2] == oganha or diagonal1 == oganha or diagonal2 == oganha or coluna1 == oganha or coluna2 == oganha or coluna3 == oganha:
        exibe_Tabuleiro(game)
        print(f'{cores["roxo"]}Parabéns {players["jogador_2"]}! Você ganhou o jogo!!!!!{cores["limpa"]}')
    elif empatou == 1:
        exibe_Tabuleiro(game)
        print(f'{cores["ciano"]}O jogo empatou!{cores["limpa"]}')
    else:
        return False
    return True
