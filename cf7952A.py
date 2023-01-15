t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    e=0
    o=0
    for i in l:
        if(i%2==0):
            e+=1
        else:
            o+=1
    print(min(e,o))