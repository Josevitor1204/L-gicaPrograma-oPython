programa {
  funcao inicio() {
    cadeia p1, p2, p3, p4

    escreva("Digite a primeira palavra: ")
    leia(p1)
    escreva("Digite a segunda palavra: ")
    leia(p2)
    escreva("Digite a terceira palavra: ")
    leia(p3)
    
    p4 = p1 + p2+ p3
    escreva("As palavras originais são: ", p1, ", ", p2, ", ", p3, "\n")
    escreva("A concatenação das palavras são: ", p4)
  }
}
