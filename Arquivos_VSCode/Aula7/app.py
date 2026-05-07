'''
    Manipulação de arquivos: percorrer meus diretótios, encontrar o arquivo
    passar o comando de abertura de arquivo, passar comando de ação.

    arquivo = open('arquivo.txt', "modo")

    modos de ação:
        - "r" : leitura do arquivo
        - "w" : escrita(sobrecreve o conteúdo antigo)
        - "a" : adiciona conteúdo
        - "x" : criar um arquivo
        - "b" : arquivos binários
        - "t" : texto

'''
# Criando e escrevendo arquivo
arquivo = open('primeiro_arquivo.txt', 'w')
arquivo.write('Olá mundo! Meu primeiro arquivo')
arquivo.close()

#lendo arquivo
arquivo = open('primeiro_arquivo.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Aplicando boa prática
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# arquivo com multiplas escritas
with open('alunos.txt', 'w') as arquivo:
    arquivo.write('Davi\n')
    arquivo.write('Davi R.\n')
    arquivo.write('Malu\n')
    arquivo.write('Madu\n')
    arquivo.write('Elisie\n')
    arquivo.write('Ana\n')
    arquivo.write('Gigi\n')
    arquivo.write('Let\n')
    arquivo.write('Nalu\n')
    arquivo.write('Lina\n')
    arquivo.write('Tenshi\n')

#lendo linha a linha
with open("alunos.txt", 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever no arquivo
frutas = ["pera", "abacaxi", 'melancia', 'manga', 'caju']

with open('frutas.txt', "w") as arquivo:
    for f in frutas:
        arquivo.write(f + '\n ')

# converter o arquivo em uma lista
with open('frutas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas)

# Saida ['pera\n', 'abacaxi\n', 'melancia\n', 'manga\n', 'caju\n']

# limpar a quebra de linhas

with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# exemplo para cadastro

while True:
    nome = input("Digite seu nome:").title()

    with open("cadastro.txt", 'a') as arquivo:
        arquivo.write(nome + "\n")

    sair = input("Deseja sair do sistema? s/n").lower()

    if sair == 's':
        break
