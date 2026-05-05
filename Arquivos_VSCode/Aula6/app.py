'''
[] --> Lista
{} --> Dicionário
() --> Tupla
'''

lista = ['gomes', 10, True, 10.5]

print(lista)

# imprimindo valor específico da lista
print(lista[0])

# imprimindo último índice
print(lista[-1])

# imprimir intervalo
print(lista[2:4])

#ordenar essa lista
#lista.sort()

#adicionando valor na lista
lista.append("karython")

#inserindo em posição específica
lista.insert(2, 'joao')

# inerindo varios valores
lista.extend(['ana', 'beatriz', 'david', 'roberto'])

numeros = []

for i in range(10):
    numeros.append(i * 2)
print(numeros)

#removendo item da lista 
print(f'Lista antes de remover {lista}')

# pop - remove pelo índice
lista.pop(0)

# pop - removendo o último indice
lista.pop()

#removendo pelo valor, (remove a primeira ocorrencia)
lista.remove('beatriz')

lista_numeros = [ n for n in range(1,11)]

#removendo intervalo de valores
del lista [2:4]

print(f'lista depois de remover {lista_numeros}')

listanomes = ['gomes', 'fulano', 'joao', 'cicrano', 'beltrano', 'maria', 'pedro']
#alteração de valores da lista
listanomes[1] = 'lucas'

print (listanomes)
# for i in range(len(lista)):
#     print(f'{i+1}º valor da lista: {lista[i]}')

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[i] * 2
print (numeros)

numeros2 = [10,20,30,40,50]

# list compreheision
numeros = [n * 2 if n > 20 else n for n in numeros]
print (numeros)