programa {
  funcao inicio() {
    cadeia nome, nomeinv, let1, let2, let3, let4, let5, let6

    escreva("Digite a primeira letra: ")
    leia(let1)
    escreva("Digite a segunda letra: ")
    leia(let2)
    escreva("Digite a terceira letra: ")
    leia(let3)
    escreva("Digite a quarta letra: ")
    leia(let4)
    escreva("Digite a quinta letra: ")
    leia(let5)
    escreva("Digite a sexta letra: ")
    leia(let6)

    nome = let1 + let2+ let3 + let4 + let5 + let6
    nomeinv = let6 + let5 + let4 + let3 + let2 +let1

    escreva("Nome original: ", nome, "\n")
    escreva("Nome invertido: ", nomeinv, "\n")
  }
}
