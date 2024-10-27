def criatab(x, y):
    ash = []
    for ysize in range(y):
        linha = [] 
        for xsize in range(x):
            linha.append(0)
        ash.append(linha)
    return ash

def define_posicoes(x, y, orientacao, size):
    ash = [[x, y]]
    if orientacao == 'horizontal':
        for e in range(y + 1, y + size, 1):
            ash.append([x, e])
    elif orientacao == 'vertical':
        for e in range(x + 1, x + size, 1):
            ash.append([e, y])
    return ash

def preenche_frota(frota, nome, x, y, orientacao, size):
    if nome not in frota:
        frota[nome] = [define_posicoes(x, y, orientacao, size)]
    else:
        frota[nome].append(define_posicoes(x, y, orientacao, size))
    return frota

def faz_jogada(tab, x, y):
    if tab[x][y] == 1:
        tab[x][y] = 'X'
    elif tab[x][y] == 0:
        tab[x][y] = '-'
    return tab

def posiciona_frota(frota):
    tab = criatab(10, 10)
    for nome in frota:
        for pos in frota[nome]:
            for xy in pos:
                x = xy[1]
                y = xy[0]
                tab[y][x] = 1

    return tab

def afundados(frota, tabuleiro):
    ash = 0
    for nome in frota:
        for pos in frota[nome]:
            afundado = True
            for xy in pos:
                x = xy[1]
                y = xy[0]
                if tabuleiro[y][x] == 1:
                    afundado = False

            if afundado == True:
                ash += 1

    return ash

def posicao_valida(frota, x, y, orientacao, size):
    pos = define_posicoes(x, y, orientacao, size)
    for xy in pos:
        if xy[0] >= 10 or xy[1] >= 10:
            return False
        
    for xy in pos:
        x = xy[1]
        y = xy[0]
        for nome in frota:
            for frotpos in frota[nome]:
                for frotxy in frotpos:
                    if x == frotxy[1] and y == frotxy[0]:
                        return False
                    

    return True


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto