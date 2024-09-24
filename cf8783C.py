for t in range(int(input())):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    l=[]
    s=0
    for i in a:
        if(i<=q):
            s+=1
        else:
            l.append(s)
            s=0
    l.append(s)
    ans=0
    for i in l:
        if(i>=k):
            ans+=(i+1)*(i-k+1)+k*(k-1)//2-i*(i+1)//2
    print(ans)

