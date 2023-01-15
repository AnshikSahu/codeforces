t=int(input())
while(t>0):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    m=int(input())
    c=0
    s=0
    for e in a:
        s+=e*6
        if(s>m):
            break
        c+=1
    print(c)