n=int(input("please enter the number of statements: "))
lst=[]
for i in range(n):
    operation=input()
    lst.append(operation)
intial_value=0
for j in range(len(lst)):
    if lst[j]=="++X"or lst[j]== "X++":
        intial_value=intial_value+1
    elif lst[j]=="--X" or lst[j]=="X--":
        intial_value=intial_value-1
print(intial_value)