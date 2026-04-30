'''
Programa 01 - Aula04 - 28/04
Professor: Karynthon Gomes
Turma:2º DS

    Sistema de sorteio 1.0
'''

import os
import random

lista_nomes = ['Arthur Cintra', 'Cleber', 'Davi Ales', 'Davi Rodrigues',
'Erick Kallel', 'Elisie', 'Ester','Malu', 'José', 'Rhuan', 'Gabriel', 'Lucas', 
'Lina', 'Gigi', 'Tenshi', 'Lais', 'Letícia', 'Nalu']



'''lista_sorteados = []
sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    print(f'Sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)

    print(f'Lista antes de remover {len(lista_nomes)}')

    lista_nomes.remove(nome_sorteado)

    print(f'Lista atualizada {len(lista_nomes)}')

    sorteados +=1

print('Fim do programa')'''

lista_sorteados = []
sorteados = 1
while sorteados == 1:
    nome_sorteado = random.choice(lista_nomes)
    print(f'Sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)
    lista_nomes.remove(nome_sorteado)
    sorteados +=1

print('Fim do programa')
