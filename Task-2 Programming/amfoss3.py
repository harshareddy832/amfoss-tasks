n=int(input("Age is: "))
lst=[]
for i in range(n):
    k=int(input("give the height of each of your candles: "))
    lst.append(k)
s=max(lst)
maxi=0
for j in range(len(lst)):
    if lst[j]==s:
        maxi += 1
print("maximum candles that can be blown: ",maxi)