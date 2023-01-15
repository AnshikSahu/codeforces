t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    avg=sum(l)/n
    c="No"
    for e in l:
        if(e==avg):
             c="Yes"
    print(c)