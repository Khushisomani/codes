def maxsubarray(arr,size):
    max1=0
    max2=-100000000000
    for i in range(len(arr)):
        if max1+arr[i]>0:
            max1=max1+arr[i]
            if max2<max1:
                max2=max1
        else:
            max1=0
    print(max2)
maxsubarray(a,len(a))