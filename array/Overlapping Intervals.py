cases=int(input())
for case in range(cases):
    intervals=int(input())
    
    l=input().strip().split()
    intervals=[]
    for num in range(0,len(l)):
        if num%2==0:
            intervals.append([int(l[num])])  
        else:
            intervals[-1]+=[int(l[num])]
    intervals.sort()
    #print(intervals)
    merged=[intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0]<=merged[-1][1]:
            merged[-1][1]=max(merged[-1][1],intervals[i][1])
        else:
            merged.append(intervals[i])
    
    for i in merged:
        print(str(i[0])+' '+str(i[1])+' ', end='')
    print()