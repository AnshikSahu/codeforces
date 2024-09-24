import math
for t in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    m=n
    lis=[True]*n
    for i in range(n-1,-1,-1):
        if(l[i]>m):
            lis[l[i]-1]=False
        else:
            m=l[i]
    c=0
    for i in lis:
        if(not i):
            break
        c+=1
    print(math.ceil((n-c)/k))