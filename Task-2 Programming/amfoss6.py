n=int(input("please enter the number of testcases: "))
for i in range(n):
    k=input("please enter you string: ")
    if len(k)>=10:
        abb=k[0]+str(len(k)-2)+k[-1]
        print(abb)
    else:
        print(k)