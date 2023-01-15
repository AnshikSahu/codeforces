for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=[]
    for e in l:
        k=0
        while(e%2==0):
            e/=2
            k+=1
        if(k!=0):
            c.append(k)
    if(len(c)==n):
        x=min(c)
        print(int(x+len(c)-1))
    elif(len(c)<n and len(c)>0):
        print(len(c))
    else:
        print(0)