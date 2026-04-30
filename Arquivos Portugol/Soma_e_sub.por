programa {
  funcao inicio() {
    inteiro num1, num2

    escreva("Digite o primeiro número: ")
    leia(num1)
    escreva("Digite o segundo número: ")
    leia(num2)

    real soma, sub
    soma = num1 + num2
    sub = num1 - num2

    escreva("Os números digitados foram: ", num1, ", ", num2, "\n")
    escreva("A soma desses números é: ", soma, "\n")
    escreva("A subtração desses números é: ", sub)
  }
}
