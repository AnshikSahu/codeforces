import copy
t=int(input())
while(t>0):
    t-=1
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    x=copy.copy(r)
    c=0
    s=0
    for i in range(0,l[0]):
        if(c==l[1]):
            break
        
        e=r.index(m)
        if(l[0]-e-1<m):
            s-=m
            for i in range(e+1,l[0]):
                r[i]+=1
            c+=1
    for e in r:
        s+=e
    print(s)