t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l= list(map(int,input().split()))
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            if(l[i]*l[j]==i+j+2):
                c+=1
    print(c)
