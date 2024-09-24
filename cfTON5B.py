for t in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    s=0
    A=True
    B=True
    C=True
    for i in range(n):
        if a[i]|x==x and A:
            s=s|a[i]
        else:
            A=False
        if b[i]|x==x and B:
            s=s|b[i]
        else:
            B=False
        if c[i]|x==x and C:
            s=s|c[i]
        else:
            C=False
    if s==x:
        print("YES")
    else:
        print("NO")