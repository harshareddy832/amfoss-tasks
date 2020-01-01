n=int(input("please input the n value of n*n: "))
matrix = []
for i in range(n):
    a=[]
    for j in range(n):
        k=int(input("please enter your each element: "))
        a.append(k)
    matrix.append(a)
print(matrix)
diagonal1sum=0
diagonal2sum=0
for l in range(n):
    for k in range(n):
        if l==k:
            diagonal1sum += matrix[l][k]
        if (l+k)==(n-1):
            diagonal2sum += matrix[l][k]
print(abs(diagonal1sum-diagonal2sum))