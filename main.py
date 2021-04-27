from uteis import tabuleiro, cores


# Programa Principal
jogo = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
tabuleiro.titulo()
jogadores = {'jogador_1': str(input(f"{cores['amarelo']}Nome do jogador X: ")).strip(),
             'jogador_2': str(input(f"{cores['roxo']}Nome do jogador O: {cores['limpa']}")).strip(),
             'atual': 'jogador_1'}
while True:
    if tabuleiro.confereVitoria(jogo, jogadores):
        break
    tabuleiro.exibe_Tabuleiro(jogo)
    tabuleiro.realiza_Jogada(jogo, jogadores)
