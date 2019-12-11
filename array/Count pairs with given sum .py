t=int(input())
for _ in range(t):
    counter=0
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=[0]*1000
    for i in a:
        m[i]+=1
    for j in range(n):
        counter+=m[k-a[j]]
        if (k-a[j]==a[j]):
            counter-=1
            
    print(counter//2)