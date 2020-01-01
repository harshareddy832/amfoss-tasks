lst=list(map(int,input("please enter your input in the format n,m,a: ").split()))
if lst[1]==0:
    k=lst[1]//lst[2]
else:
    k=lst[1]//lst[2]+1
if lst[0]==0:
    c=lst[0]//lst[2]
else:
    c=lst[0]//lst[2]+1
print(k*c)