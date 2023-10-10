lista_nomes = []
lista_senhas = []
for x in range(3):
    cadast_nome = input("digite seu nome: ")
    cadast_senha = input("digite sua senha para cadastro ao nosso sistema: ")
    lista_nomes.append(cadast_nome)
    lista_senhas.append(cadast_senha)


"""#imprimir nome, senha e posição dos dados no array:   
print(lista_nomes)
print(lista_senhas)
for x in range(5):
      print(f"O úsuário {lista_nomes[x]} com senha {lista_senhas[x]} está na posição {x}")"""


#acesso à conta
nome_acesso = input("digite seu nome para acesso à conta: ")
senha_acesso = input("digite sua senha de acesso: ")

for z in range(3):
    if nome_acesso == lista_nomes[z] and senha_acesso == lista_senhas[z]:
        print("Login efetuado com sucesso!!")

    else:
        print("Usuário ou senha inválidos")
        break
