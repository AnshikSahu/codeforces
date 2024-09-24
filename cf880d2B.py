for t in range(int(input())):
    n,k,g=map(int,input().split())
    a=g//2 if g%2!=0 else g//2-1
    if(k*g<=a*n):
        print(k*g)
    else:
        r=(k*g-a*(n-1))%g
        if(r<=a):
            print(a*(n-1)+r)
        else:
            print(a*(n-1)+r-g)
        