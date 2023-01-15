n,t=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
for i in range(t):
    x,y=list(map(int,input().split()))
    s=0
    for j in range(n-x,n-x+y):
        s+=l[j]
    print(s)