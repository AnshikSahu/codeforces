def search(d,m,l):
    f=m-d[0]
    g=d[1]-f
    if(g<0):
        g=0
    for i in range(g,d[1]+1):
        if(max(l[i:i+m])==m):
            return [m,i]
    return d
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l= list(map(int,input().split()))
    c=1
    x=l.index(1)
    d=[1,x]
    for m in range(2,n):
        k=0
        y=search(d,m,l)
        if(y[0]>d[0]):
            k=1
        c=c*10+k
        d=y
    c=c*10+1
    print(c)
