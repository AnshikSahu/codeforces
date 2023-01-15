t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    c=0
    while(i<n):
        for j in range(i+1,n):
            if(l[j]<l[i]):
                c+=1
                i=j
                break
        i+=1
    print(c)