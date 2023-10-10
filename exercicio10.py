N = int(input("Qual será o tamanho do vetor? "))
A = []
for x in range(N):
    num_A = int(input("digite os valores do vetor A: "))
    A.append(num_A)

B = []
for z in range(N):
    num_B = int(input("digite os valores do vetor B: "))
    B.append(num_B)
print(A)
print(B)

SOMA = [0] * N
for y in range(N):
    SOMA[y] = A[y] + B[y]
print(SOMA)