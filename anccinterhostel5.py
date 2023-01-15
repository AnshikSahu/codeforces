def prime(H):
    x=True
    for i in range(2,int(H**0.5)+1):
        if(H%i==0):
            x=False
            break
    return x
def cat():
    l= list(map(int,input().split()))
    n=l[0]
    H=l[1]
    c=True
    while(H>n):
        x=True
        if( prime(H)):
            c=False
            break
        for i in range(2,n+1):
            if(H%i==0):
                x=False
                break
        if(x):
            c=False
            break
        H-=1
    if(c):
        print(-1)
    else:
        print(H)
cat()
            