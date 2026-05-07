"""

Desenvolver um sistema de gerenciamento de Carros com realização do CRUD

"""

import os
import time

carros = []
proximo_id = 1

os.system('cls')
while True:
    print("\n===== Sistema de Carros 🚗 =====")
    print('1 - Cadastrar carro')
    print('2 - Listar carro')
    print('3 - Atualizarar carro')
    print('4 - Deletar carro')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    os.system('cls')

    #Criar
    if opcao == '1':
        modelo = input("Digite o modelo do carro: ").title()
        preco = float(input("Digite o preço: ").replace(',','.'))
        marca = input("Digite a marca do carro: ").title()

        carro = {
            "id"         : proximo_id,
            "modelo"    : modelo,
            "preco"      : preco,
            "marca"      : marca
        }

        carros.append(carros)
        proximo_id += 1

        print('✅ Carro cadastrado com sucesso!')

        time.sleep(3)
        os.system('cls')

    # read
    elif opcao == '2':
        if not carros:
            print ("❌Nenhum carro encontrado")
        else:
            print ("\n 📋Lista de carros")
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')

    #Uptade
    elif opcao == '3':
        os.system('cls')
        for carro in carros:
            print('\n 📋Lista de carros')
            for carro in carros: 
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
        id_busca = int(input('Digite o id do carro para atualizar: '))

        encontrado = False
        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo = input('Digite o novo modelo: ').title()
                novo_preco = float(input('Digite o novo preço: ').replace(',','.'))
                nova_marca = input('Digite a nova marca: ').title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = nova_marca

                print('✅ Carro atualizado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print('❌ Carro não encontrado!')

    #delete
    elif opcao == '4':
        os.system('cls')
        print('\n 📋Lista de carros')
        for carro in carros :
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
        id_busca = int(input('Digite o id do carro para atualizar: '))

        

    # sair
    elif opcao == '0':
        total = 20
        barra = ""
        print('Saindo do sistema...')
        for i in range(1,total +1) :
            barra += "🟩"
            porcentagem = int((i / total) *100)
            vazio ="-" * (total -1)
            print(f'\r[{barra}] {porcentagem}%', end="")
            time.sleep(0.2)
        break
    
    # uptade
    else:
        print('❌ Opção inválida')