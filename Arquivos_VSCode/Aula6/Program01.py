'''
1. Crie um programa que o usuário possa digitar quantos numeros quiser e ao terminar imprimir a lista em ordem crescente.

2. Crie um programa que o usuário possa digitar a quantidade desejada de notas de um determinado aluno (nota mínima 0 e máxima 10) 
e o programa calcula a media desse aluno, e ao final imprima se o aluno esta (aprovado >= 7, recuperação >= 5 e reprovado) '''

# lista_numero = []

# while True:
#     numero = float(input("Digite um número: "))
#     lista_numero.append(numero)
#     opcao = input("Deseja adicionar mais? (s - Sim) ou enter para não").lower()
#     if opcao != "s":
#         break

# lista_numero.sort()
# print(lista_numero)

import os

print("Boletim escolar 2.0")

lista_notas = []
nome = input("Digite o nome do aluno: ").title()
curso = input("Digite o curso: ").upper()

while True: 
 nota= input("Digite uma nota: ")
 nota = float(nota)
 lista_notas.append(nota)
 print(lista_notas)
 
 opcao = input("Deseja adicionar mais notas? (Enter - continue | n- Não)").lower()
 if opcao == "n": 
   break

media = sum(lista_notas) / len(lista_notas)
print(media)

if media >= 7: 

    resultado = "Aprovado" 

elif media >= 5: 

    resultado = "Recuperação" 

else:
   resultado = "Reprovado"

print(resultado)