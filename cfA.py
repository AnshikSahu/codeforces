t=int(input())
while(t>0):
    t-=1
    n=int(input())
    if(n<100):
        print(n%10)
    else:
        m=n%10
        while(n>0):
            a=n%10
            if(a<m):
                m=a
            n=n//10
        print(m)