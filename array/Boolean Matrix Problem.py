def boolarr(arr,rows,cols):
    finalarr=[[0]*cols]*rows
    for i in range(rows):
        if 1 in arr[i]:
            finalarr[i]=[1]*cols
    for j in range(cols):
        if 1 in [element[j] for element in arr]:
            for element in finalarr:
                element[j] = 1
    return finalarr
    
t= int(input())
for i in range(t):
    string = input().split()
    rows,cols = int(string[0]),int(string[1])
    arr=[]
    for i in range(rows):
        arr.append(list(map(int,input().split())))
    arr=boolarr(arr,rows,cols)
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j],end=" ")
        print()
        