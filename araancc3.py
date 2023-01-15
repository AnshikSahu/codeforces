t=int(input())
while(t>0):
    t=t-1
    n,k= list(map(int,input().split()))
    if(n%4==0):
        a=int(n/4)
        b=a
        c=2*a
    elif(n%2==0):
        a=2
        b=int((n/2-1)/2)*2
        c=b
    else:
        a=1
        b=int((n-1)/2)
        c=b
    print(a," ",b," ",c)
        