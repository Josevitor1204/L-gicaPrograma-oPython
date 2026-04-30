programa {
  funcao inicio() {
    escreva("----- Descubra o seu IMC -----")
    cadeia nome 
    inteiro idade
    real peso, altura

    escreva("\n Digite seu nome: ")
    leia(nome)

    escreva("Digite sua idade: ")
    leia(idade)

    escreva("Digite seu peso: ")
    leia(peso)

    escreva("Digite sua altura (em metros): ")
    leia(altura)

real imc
imc= peso/altura*altura
    
    escreva("\nOlá ", nome, ", seja bem vindo!")
    escreva("\nDescobri que você tem ", idade, " anos.")
    escreva("\nSeu peso é: ", peso, " quilos.")
    escreva("\nSua altura é: ", altura, " metros.")
    escreva("\nSeu IMC é: ", imc)
  }
}
