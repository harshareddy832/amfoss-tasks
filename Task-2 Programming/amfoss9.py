x=int(input())
s=str(x)
team1="0000000"
team2="1111111"
if team1 in s or team2 in s:
    print("YES")
else:
    print("NO")