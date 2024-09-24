def solve(l1,l2,r1,r2,a,b,dp,n):
    if l1==r1:
        if a[l1]==b[l2]:
            return True
        else:
            return False
    if dp[l1*n+r1]!=0:
        return True
    if not((a[l1]==b[l2] and a[r1]==b[r2]) or (a[l1]==b[r2] and a[r1]==b[l2])):
        return False
    if a[l1]==b[l2]:
        l=solve(l1+1,l2+1,r1,r2,a,b,dp,n)
        r=solve(l1,l2,r1-1,r2-1,a,b,dp,n)
    else:
        l=solve(l1+1,l2,r1,r2-1,a,b,dp,n)
        r=solve(l1,l2+1,r1-1,r2,a,b,dp,n)
    if l and r:
        dp[l1*n+r1]=1
        return True
    return False
        
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    dp=[0]*(n*n)
    if solve(0,0,n-1,n-1,a,b,dp,n):
        print("Bob")
    else:
        print("Alice")
        