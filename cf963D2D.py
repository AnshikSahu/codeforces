for _ in range (int (input ())):
    n, k = list (map (int, input().split()))
    nums = list (map (int, input ().split()))
    end_len = (n-1)%k + 1
    l = min (nums)
    r = max (nums)
    ans = -1
    while l <= r:
        m = (l + r) //2
        dp = [float("-inf")] * end_len + [0]
        for i in range(n):
            if i% k < end_len:
                dp[i%k] = max(dp[i % k], dp[i%k-1] + (1 if nums[i] >= m else -1))
        print (dp)
        if dp[end_len - 1] > 0:
            ans=m
            l=m+ 1
        else:
            r=m - 1
        print (l, r, m, ans)
    print (ans)