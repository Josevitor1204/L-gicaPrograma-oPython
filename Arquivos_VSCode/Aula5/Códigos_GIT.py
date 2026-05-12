""" Códigos para subir arquivos no git hub
Para novo repositório:
1. git init
2. git config --local user.name Josevitor1204
3. git config --local user.email jose.v.rodrigues11@aluno.senai.br
4. git add .
5. git commit -m "NOME_PARA_O_COMMIT"
6. git branch -M main
7. git remote add origin LINK_DO_REPOSITÓRIO_NO_GITHUB
8. git remote -v
9. git push origin main

Para repositório já existente:
1. git add .
2. git commit -m "NOME_PARA_O_COMMIT"
3. git remote add origin LINK_DO_REPOSITÓRIO_NO_GITHUB
4. git branch -M main
5. git push origin main

Clonar repositório:
1.Copiar o link do repositório
2. git clone LINK_DO_REPOSITÓRIO_NO_GITHUB
"""

usuarios = []

for i in range(2):
    print(f"Usuário {i+1}")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    
    usuarios.append([nome, sobrenome])

print("\nResultado:")
print(usuarios[0][0], usuarios[1][1])
print(usuarios[1][0], usuarios[0][1])