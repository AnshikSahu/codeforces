for t in range(int(input())):
    n=int(input())
    l=[0]+list(map(int,input().split()))
    s=0
    k=0
    m=0
    ma=0
    for i in range(n):
        s+=l[i]
        if(l[i+1]<0):
            temp=0 
            for j in range(0,n+1):
                if(temp>=s):
                    temp=max(temp+l[j],s)
                else:
                    temp+=l[j]
            if(temp>m):
                m=temp
                k=s
    print(k)