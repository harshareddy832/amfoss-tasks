n=int(input("please enter your number of testcases: "))
for i in range(n):
    k=int(input("please enter your N: "))
    sum=0
    for j in range(k):
        if j%3==0 or j%5==0:
            sum += j
    print("your sum is: ",sum)