def forwardtime(a):
    s=0
    for e in a:
        if(e>s):
            s+=e-s
        s+=1
    return s
def move(c,p,a,n,m):
    u=a[p[0]-1][p[1]]
    d=a[p[0]+1][p[1]]
    r=a[p[0]][p[1]+1]
    l=a[p[0]][p[1]-1]
    if(u!=-1 and (u-c)<=0):
        if(a[p[0]-1][p[1]-1]==-1 or p[1]==n):
            f1=forwardtime(a[1][p[1]:n+2])
            f2=forwardtime(a[2][p[1]+1:n+2])
            if(f1<=f2 or p[1]==n):
                a[p[0]][p[1]]=-1
                return [p[0]-1,p[1]],m+1
    if(d!=-1 and (d-c)<=0):
        if(a[p[0]+1][p[1]-1]==-1 or p[1]==n):
            f1=forwardtime(a[1][p[1]+1:n+2])
            f2=forwardtime(a[2][p[1]:n+2])
            if(f2<=f1 or p[1]==n):
                a[p[0]][p[1]]=-1
                return [p[0]+1,p[1]],m+1
    if(r!=-1 and (r-c)<=0):
        if(a[p[0]+1][p[1]]==-1 and a[p[0]-1][p[1]]==-1):
            a[p[0]][p[1]]=-1
            return [p[0],p[1]+1],m+1
        else:
            f1=forwardtime(a[1][p[1]+1-p[0]==2:n+2])
            f2=forwardtime(a[2][p[1]+1-p[0]==1:n+2])
            if((f1<=f2 and p[0]==1) or (f2<=f1 and p[0]==2)):
                a[p[0]][p[1]]=-1
                return [p[0],p[1]+1],m+1
    if(l!=-1 and (l-c)<=0):
        a[p[0]][p[1]]=-1
        return [p[0],p[1]-1],m+1
    return p,m
for i in range(int(input())):
    m=int(input())
    l0=[-1]*(m+2)
    l1=[-1]+list(map(int,input().split()))+[-1]
    l2=[-1]+list(map(int,input().split()))+[-1]
    l3=[-1]*(m+2)
    a=[l0,l1,l2,l3]
    c=0
    n=1
    p=[1,1]
    while(n<2*m):
        p,n=move(c,p,a,m,n)
        c+=1
    print(c)