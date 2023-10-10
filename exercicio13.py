vetor = []
pares = []
maior = 0
menor = 0
soma = 0
cont = 0
for x in range(30):
    numeros = int(input("digite os números do vetor: "))
    vetor.append(numeros)
print(vetor)

#numeros pares
for y in vetor:
    if y%2 == 0:
        pares.append(y)



#menor e maior valor
for c in range(30):
    if c == 0:
        maior = menor = vetor[c]
    else:
        if vetor[c] > maior:
            maior = vetor[c]
        if vetor[c] < menor:
            menor = vetor[c]

#media dos números
media = sum(vetor) / 30
print(media)
for m in range(30):
    if vetor[m] > media:
        cont += 1


print(f"os números pares no vetor são {pares}; o maior número é {maior} e o menor é {menor}"
      f"\n a média do vetor é igual a {media} e há {cont} números acima da média")






