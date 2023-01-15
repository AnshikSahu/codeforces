for t in range(int(input())):
    n,k,r,c=list(map(int,input().split()))
    g=[]
    for i in range(n):
        g.append(["."]*n)
    for i in range(n):
        for j in range(n):
            if(i%k==j%k):
                g[i][j]="X"
    x=(r-1)%k
    y=(c-1)%k
    for i in range(n//k):
        a=x+k*i
        b=y+k*i
        g[a],g[b]=g[b],g[a]
    for e in g:
        print("".join(e))