from funcoes import *

order = ['porta-aviões', 'navio-tanque', 'navio-tanque',
         'contratorpedeiro', 'contratorpedeiro', 'contratorpedeiro',
         'submarino', 'submarino', 'submarino', 'submarino']

nametosize = {'porta-aviões': 4, 'navio-tanque': 3, 'contratorpedeiro': 2, 'submarino': 1}

playing = True

while playing == True:
    frota = {
        "porta-aviões":[],
        "navio-tanque":[],
        "contratorpedeiro":[],
        "submarino": [],
    }
    i = 0
    while i < len(order):
        name = order[i]
        size = nametosize[name]
        print(f'Insira as informações referentes ao navio {name} que possui tamanho {size}')
        x = int(input('Linha: '))
        y = int(input('Coluna: '))
        orientacao = 1
        if name != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'
        
        if posicao_valida(frota, x, y, orientacao, size):
            preenche_frota(frota, name, x, y, orientacao, size)
            i += 1
        else:
            print('Esta posição não está válida!')
    
    frota_oponente = {
        'porta-aviões': [
            [[9, 1], [9, 2], [9, 3], [9, 4]]
        ],
        'navio-tanque': [
            [[6, 0], [6, 1], [6, 2]],
            [[4, 3], [5, 3], [6, 3]]
        ],
        'contratorpedeiro': [
            [[1, 6], [1, 7]],
            [[0, 5], [1, 5]],
            [[3, 6], [3, 7]]
        ],
        'submarino': [
            [[2, 7]],
            [[0, 6]],
            [[9, 7]],
            [[7, 6]]
        ]
    }
    tab = posiciona_frota(frota)
    enemy_tab = posiciona_frota(frota_oponente)
    xylist = []
    coords = [-1, -1]

    while afundados(frota_oponente, enemy_tab) < 10:
        alltab = monta_tabuleiros(tab, enemy_tab)
        print(alltab)
        again = True

        while again == True:
            again = False
            coods = [-1, -1]
            xattack = int(input('Jogador, qual linha deseja atacar? '))
            if xattack > 9 or xattack < 0:
                while xattack > 9 or xattack < 0:
                    print('Linha inválida!')
                    xattack = int(input('Jogador, qual linha deseja atacar? '))
            coords[0] = xattack
                            
            yattack = int(input('Jogador, qual coluna deseja atacar? '))
            if yattack > 9 or yattack < 0:
                while yattack > 9 or yattack < 0:
                    print('Coluna inválida')
                    yattack = int(input('Jogador, qual coluna deseja atacar? '))
            coords[1] = yattack

            if coords in xylist:
                print(f'A posição linha {xattack} e coluna {yattack} já foi informada anteriormente!')
                again = True
            else:
                x = coords[0]
                y = coords[1]
                xylist.append([x, y])
        

        enemy_tab = faz_jogada(enemy_tab, x, y)
   
    if afundados(frota_oponente, enemy_tab) >= 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        playing = False