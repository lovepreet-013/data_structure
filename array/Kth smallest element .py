n=int(input())
for _ in range(n):
    i = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    arr.sort()
    print(arr[k-1])