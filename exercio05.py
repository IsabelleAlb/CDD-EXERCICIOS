A = [10, 5, 13, 45, 36, 71, 24, 18, 33, 27]
X = int(input("digite um número: "))

M = [0] * 10
for x in range(10):
    M[x] = A[x] * X
print(M)
