t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    if(n%2!=0):
        print("No")
    else:
        l.sort()
        c=True
        for i in range(1,n//2):
            if(l[i]==l[i+n//2] or l[i]==l[n//2 + i -1]):
                c=False
                break
        if(c):
            print("Yes")
            s=""
            for i in range(0,n//2):
                s+=str(l[i])+" "+str(l[n//2 + i])+" "
            print(s)
        else:
            print("No")