import modulo as ma


while True:
        print("Calculadora")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Dividir")
        print("5. Limp Terminal")

        opcao = input("Digite a opção desejada: ")
        match opcao:
            case '1':
                print("-"*5, 'SOMA', "-"*5)
                num1 = int(input("Digite um número para somar: "))
                num2 = int(input("Digite outro número para somar: "))
                result = ma.soma(num1, num2)
                print(f'Resultado: {result}')
                break
                      
            case '2':
                print("-"*5, 'SUBTRAÇÃO', "-"*5)
                num1 = int(input("Digite um número para subtrair: "))
                num2 = int(input("Digite outro número para subtrair: "))
                result = ma.sub(num1, num2)
                print(f'Resultado: {result}')
                break

            case '3':
                print("-"*5, 'MULTIPLICAÇÃO', "-"*5)
                num1 = int(input("Digite um número para multiplicar: "))
                num2 = int(input("Digite outro número para multiplicar: "))
                result = ma.multiplicacao(num1, num2)
                print(f'Resultado: {result}')
                break

            case '4':
                print("-"*5, 'DIVISÃO', "-"*5)
                num1 = int(input("Digite um número para dividir: "))
                num2 = int(input("Digite outro número para dividir: "))
                result = ma.divisao(num1, num2)
                print(f'Resultado: {result}')
                break

            case '5':
                ma.limpa_terminal()
                break
            
            case _ :
                print("Opção inválida!")

