n,k=map(int,input().split())
list1=list(map(int,input().split()))
s=0
for i in range(len(list1)):
    if list1[i]>=k+1:
        s=s+1
print(s)

