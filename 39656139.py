from bisect import bisect_right
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    arr=[0]
    arr[0]=a[0]
    for i in range(1,n):
        index=bisect_right(arr,a[i])
        if index==len(arr):
            arr.append(a[i])
        else:
            arr[index]=a[i]
    print(len(arr),*arr)
