def minTime(n,solve,search,k):
    dp=[-1]*n
    k=max(1,k)
    def helper(i):
        if(i>=n):
            return 0
        elif(dp[i]>=0):
            return dp[i]
        else:
            next=helper(i+1)
            sol=solve[i]+next
            for j in range(i+2,i+k+1):
                next=min(next,helper(j))
            srch=search[i]+next
            dp[i]= min(sol,srch)
            return dp[i]
    return helper(0)
        
n=7
solve=[2,1,9,7,8,4,3]
search=[5,1,6,1,6,1,5]
k=3

print(minTime(n,solve,search,k))