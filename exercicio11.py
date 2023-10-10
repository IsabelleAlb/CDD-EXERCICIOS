#ler um vetor de 30 números
V = []
for z in range(30):
    numero = int(input("digite um número: "))
    V.append(numero)
print(V)

#pesquisar quantas vezes um número aparece
pesquisa = int(input("qual número você deseja encontrar? "))
print(f"o número {pesquisa} aparece {V.count(pesquisa)} vezes no vetor")
