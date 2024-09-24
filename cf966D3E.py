def value(i,j,n,m,k):
    return min(min(i+1,k),min(n-i,k))*min(min(m-j,k),min(j+1,k))

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    w=int(input())
    a=list(map(int,input().split()))
    a.sort()
    arr=[ value(i,j,n,m,k) for i in range(n) for j in range(m)]
    arr.sort(reverse=True)
    print(arr)
    ans=0
    for i in range(w):
        ans+=(arr[i]*a[i])
    print(ans)
        
        
    