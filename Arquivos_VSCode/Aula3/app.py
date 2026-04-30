# Estrutura de Dados em Pyton
# Lista | Dicionário |Tupla 
#   []        

#NOTE: Boletim Escolar 2.5 (2.0 só que melhor)

import os

os.system("cls")

print("Boletim Escolar")
lista_notas = []
nome = input("Digite o nome do aluno: ").title()
curso = input("Digite o curso: ").upper()


while True:
    nota = input("Digite sua nota: ")
    nota = float(nota)
    lista_notas.append(nota) #adiciona um elemento a lista, sempre em última posição
    print(lista_notas)

    opcao = input("Deseja adicioar mais notas? (Enter - continua | n - não)").lower()
  
    if opcao == "n":
        break
   
media = sum(lista_notas) / len(lista_notas)
print(media)