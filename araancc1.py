def string(r):
    s=""
    for e in r:
        s=s+str(e)+" "
    return s
def maximum(l):
    k=0
    for i in range(0,len(l)):
        if(l[i]>l[k]):
            k=i
    return k
def arrange(l,a):
    if(len(l)==1 or len(l)==0):
        return(a+l)
    i=maximum(l)
    return arrange(l[:i],a+l[i:])
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l= list(map(int,input().split()))
    r=arrange(l,[])
    print(string(r))