def big(a,b,d):
    r=False
    for i in range(d,0,-1):
        y=10**(i-1)
        ai=a//y
        bi=b//y
        if(ai>bi):
            if(i%2==1):
                r=True
            break
        if(ai<bi):
            if(i%2==0):
                r=True
            break
        a=a%y
        b=b%y
    return r
def merge(arr, l, m, r,d):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if big(L[i], R[j],d) or L[i]==R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r,d):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m,d)
        mergeSort(arr, m+1, r,d)
        merge(arr, l, m, r,d)
l= list(map(int,input().split()))
l2= list(map(int,input().split()))
mergeSort(l2,0,l[0]-1,l[1])
ans=l2
if(l[1]%2==0):
    s=str(ans[0])
    for i in range(1,l[0]):
        s=s+" "+str(ans[i])
else:
    s=str(ans[l[0]-1])
    for i in range(l[0]-2,-1,-1):
        s=s+" "+str(ans[i])
print(s)
    