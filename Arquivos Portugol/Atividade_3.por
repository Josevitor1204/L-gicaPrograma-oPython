programa {
  funcao inicio() {
    inteiro prova1, prova2, prova3

    escreva("Digite sua nota da prova 1: ")
    leia(prova1)

    escreva("Digite sua nota da prova 2: ")
    leia(prova2)

    escreva("Digite sua nota da prova 3: ")
    leia(prova3)

    real soma
    soma = prova1 + prova2 + prova3

    real div
    div = soma / 3

    escreva("Sua média é: ", div, "\n")

    se(div >= 7) {
      escreva("Parabéns! Você passou!!!", "\n")
    }

    senao{
      escreva("Infelizmente, você não passou!")
    }

  }
}
