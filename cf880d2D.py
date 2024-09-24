n,m,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
p,q=-1,-1
c=0
for i in range(m):
    while(c<n and a[c]<=i):
        c+=1
    if(c<k):
        low=0
    else:
        low=(i+a[c-k+1]+1)//2 if k>1 else i if a[c-1]!=i else i+1
    if(c>n-k):
        high=m
    else:
        high=(i+a[c+k-1]-1)//2 if k>1 else i if a[c-1]!=i else i-1
    num=high-low+1
    if(num>p):
        p=num
        q=i
print(str(p)+" "+str(q))