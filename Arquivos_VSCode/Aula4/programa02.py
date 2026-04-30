import random
import os
import time

lista_nomes = []
lista_sorteados=[]

print(30*"-", "Bem Vindo ao sistema de sorteio", 30*"-")
while True:
    nome = input("Digite um nome para ser sorteado: ").title()
    lista_nomes.append(nome)
    opcao = input("Deseja adicionar mais? (s - Sim) ou enter para não").lower()
    if opcao != "s":
        break

while True:
    if not lista_nomes:
        print("A lista de nomes está vazia!")
        break
    else:
        nome_sorteado = random.choice(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        lista_sorteados.append(nome_sorteado)
        os.system("cls")

    for i in range(5,0,-1):
        time.sleep(1)
        os.system("cls")
        print(f'Contagem regressiva...{i}')

    print(f"O sorteado foi: {nome_sorteado}")
    sortear_novamente = input("Deseja sortear outro nome? (s - Sim | n - Não)")

    if sortear_novamente == 'n':
        break

print(lista_sorteados)
print("Fim do programa")