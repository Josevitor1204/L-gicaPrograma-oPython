programa {
  funcao inicio() {
    inteiro x, y

    escreva("Escolha um valor para x: ")
    leia(x)
    escreva("Escolha um valor para y: ")
    leia(y)

    // equação: 8x + 4y / (x + y)2.

    real parte1, parte2, parte3
    parte1 = 8*x + 4*y
    parte2 = x*x + 2*x*y + y*y
    parte3 = parte1/parte2

    escreva("Os valores de x e y são: ", x, ", ", y, "\n")
    escreva("O resultado da equação é: ", parte3)
  }
}
