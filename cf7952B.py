for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))+[-1]
    d=[0]*n
    c=0
    x=l[0]
    f=True
    s=[]
    for i in range(0,n+1):
        if(l[i]!=x):
            if(c==1):
                f=False
                break
            else:
                s.append(c)
                x=l[i]
                c=1
        else:
            c+=1
    k=0
    if(f):
        for e in s:
            d[k]=str(e+k)
            for i in range(k+1,k+e):
                d[i]=str(i)
            k+=e
        print(" ".join(d))
    else:
        print(-1)