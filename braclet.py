def cut(arr,k):
    n = len(arr)
    dp=[0]*n
    best=1<<63
    for i in range(k):
        dp[i]=0
        for j in range(1,n+1):
            p=(j+i)%n
            dp[p]=dp[p-1]+arr[p]
            for q in range(p,max(p-k-1,i-1),-1):
                dp[p]=min(dp[p],dp[q]+arr[p])
        best=min(best,dp[i])
    print(best)