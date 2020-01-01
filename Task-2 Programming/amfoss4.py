s=input("please enter the time: ")
if s[-2:]=='AM' and s[:2]=='12':
    s='00'+s[2:-2]
    print(s)
elif s[-2:]=='AM':
    s=s[:-2]
    print(s)
elif s[-2:]=='PM' and s[:2]=='12':
    s=s[:-2]
    print(s)
else:
    s=str(int(s[:2])+12)+s[2:8]
    print(s)

