n,t=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
for i in range(t):
    x,y=list(map(int,input().split()))
    print(sum(l[n-x:n-x+y]))