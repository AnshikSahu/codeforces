t=int(input())
while(t>0):
    t-=1
    l= list(map(int,input().split()))
    x=l[0]+l[1]+l[2]
    y=l[1]+l[2]
    z=l[2]
    print(str(x)+" "+str(y)+" "+str(z))