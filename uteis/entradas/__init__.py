from uteis import cores


def verifica_Jogada(jogada):
    if jogada in '3A1A2A3B1B2B3C1C2C3A':
        return True
    else:
        print(f'{cores["vermelho"]}Opção fora do padrão{cores["limpa"]}')
        return False
