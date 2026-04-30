programa {
  funcao inicio() {
    
    inteiro num1, num2, num3

    escreva("Digite o número você quer: ")
    leia(num1)

    escreva("Digite outro número: ")
    leia(num2)

     escreva("Digite outro número: ")
    leia(num3)

    se(num1 >= num2){
      escreva(num1, " é maior que ", num2, "\n")
    }
senao{
escreva(num1, " não é maior que ", num2, "\n")
}
    se(num1 >= num3){
      escreva(num1, " é maior que ", num3, "\n")
    }
senao{
escreva(num1, " não é maior que ", num3, "\n")
}
    
 se(num2 >= num3){
      escreva(num2, " é maior que ", num3, "\n")
    }
senao{
escreva(num2, " não é maior que ", num3, "\n")
}
  }
}
