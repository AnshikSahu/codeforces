t=int(input())
while(t>0):
    t-=1
    X=[]
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(0,n):
        x=min(l[i:])
        k=l.index(x)
        if(k!=i):
            X.append(l[i]&l[k])
            l[i],l[k]=l[k],l[i]
    print(max(X))