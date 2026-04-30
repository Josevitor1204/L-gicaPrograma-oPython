# for

#laço de for, ele é finito: quando eu sei o número de repetições
lista_frutas = []
fruta = ['melancia', 'abacaxi', 'melão', 'pera']
fruta = 'melancia'

''' for f in frutas:
    print(f) '''

#for range(inicio, fim, salto)

''' for i in range(5)
    print(i) '''

''' for _ in range(1,20,2):
   print("Repeti") '''

#num = int(input('Digite um número para saber a sua tabuada: '))

'''for i in range(1,11):
    print(f"{i} X {num} = {i*num}")
'''

lista_nomes = ['Arthur Cintra', 'Cleber', 'Davi Ales', 'Davi Rodrigues',
'Erick Kallel', 'Elisie', 'Ester','Malu', 'José', 'Rhuan', 'Gavriel', 'Lucas']

for i, nome in enumerate(lista_nomes):
    print(f'{i+1}º {nome}')

nome_buscar = input('Digite um nome para buscar: ').title()

if nome_buscar in lista_nomes:
    print("Usuário encontrado! ")