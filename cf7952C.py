for t in range(int(input())):
    n,k=list(map(int,input().split()))
    s=input()
    c=0
    l=[]
    for i in range(n):
        if(s[i]=="1"):
            c+=1
            l.append(i)
    sum=c*11
    if(c>1):
        s1=l[0]
        s2=n-1-l[-1]
        if(s2<=k):
            sum-=10
            k-=s2
        if(s1<=k):
            sum-=1
    if(c==1):
        s1=l[0]
        s2=n-1-l[-1]
        if(s2<=k):
            sum-=10
        elif(s1<=k):
            sum-=1
    print(sum)