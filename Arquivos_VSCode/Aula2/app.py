"""int = inteiro
str --> string = textual
bool --> boolian = lógico(True,False)
float = valor real
Tipagem dinâmica = não precisa declarar o tipo de dado da variável
Para se delcarar um nome é necessário estar entre aspas
Com parenteses vira função"""

str
int
bool
float 

#variavel com valor definido
nome = "José Vitor" 
idade = 16
altura = 1.72
aluno = True

"""print("Nome:",nome)
print("Idade:",idade)
print("Altura:",altura)
print("É aluno?",aluno)"""

# entrada de dados 
novo_nome = input("Digite o seu nome: ")

print("Nome:",nome)
print("Novo nome:",novo_nome)

"""
Desenvolva um sistema que receba do usuário seu nome, data de nascimento, peso e altura.
Formate a saída para aparecer na tela do usuário: Olá {nome_informado}, seja bem-vindo ao sistema Python.
Aqui estão as suas informações:"""

print(type(nome))