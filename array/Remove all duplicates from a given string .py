def remove_duplicate(s):
    l=[]
    ns=''
    for i in range(0,len(s)):
        if(s[i] not in l):
            ns=ns+s[i]
            l.append(s[i])
    return ns
T=int(input())

for i in range(0,T):
    s=input()
    print(remove_duplicate(s))