Alice_rating=list(map(int,input("please enter your rating for Alice problem: ").split()))
Bob_rating=list(map(int,input("please enter your rating for Bob problem: ").split()))
alice=0
bob=0
for i in range(0,3):
    if Alice_rating[i]>Bob_rating[i]:
        alice+=1
    elif Bob_rating[i]>Alice_rating[i]:
        bob+=1
print(alice,bob)