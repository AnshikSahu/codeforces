def ancc4():
    n=int(input())
    s=0
    a=[]
    for i in range(0,n):
        l= list(map(int,input().strip().split()))[:2]
        j=0
        while(j<i):
            if(l[0]>a[j][0]):
                break
            j+=1
        a.insert(j,l)
    m=int(input())
    b=[]
    for i in range(0,m):
        l= list(map(int,input().strip().split()))[:2]
        j=0
        while(j<i):
            if(l[0]>b[j][0]):
                break
            j+=1
        b.insert(j,l)
    i=n
    j=m
    while(i>0 and j>0):
        if(a[i-1][0]<b[j-1][0]):
            s+=a[i-1][1]
            i-=1
        elif(a[i-1][0]>b[j-1][0]):
            s+=b[j-1][1]
            j-=1
        else:
            s+=max(a[i-1][1],b[j-1][1])
            i-=1
            j-=1
    while(i>0):
        s+=a[i-1][1]
        i-=1
    while(j>0):
        s+=b[j-1][1]
        j-=1
    print(s)
ancc4()