def moves(l):
    n=len(l)
    c=0
    for i in range(n-2,-1,-1):
        if(l[i+1]==0):
            return -1
        while(l[i+1]<=l[i]):
            l[i]=l[i]//2
            c+=1
    return c
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    print(moves(l))