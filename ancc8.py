def ancc8():
    t=int(input())
    ans=[]
    while(t>0):
        t=t-1
        c= list(map(int,input().strip().split()))[:2]
        n=c[0]
        H=c[1]
        l= list(map(int,input().strip().split()))[:n]
        k=H//n
        c=[]
        total=0
        for i in range(0,n-1):
            d=l[i+1]-l[i]
            c.append(d)
            total+=d
        f=False
        while(n>0):
            s=0
            for x in c:
                if(x<=k):
                    s=s+x
                else:
                    s=s+k
            if(f):
                k=H-total
            if(s==total):
                f=True
            s=s+k
            if(s>=H):
                break
            k=k+1
        ans.append(k)
    for x in ans:
        print(x)
ancc8()