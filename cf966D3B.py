for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dp=[0]*n
    flag=1
    for i in range(n):
        if i>0:
            if l[i]==1 and dp[1]==0:
                print("NO")
                flag=0
                break
            elif l[i]==n and dp[n-2]==0:
                print("NO")
                flag=0
                break
            elif dp[l[i]-2]==0 and dp[l[i]]==0:
                print("NO")
                flag=0
                break
        dp[l[i]-1]=1
    if flag:
        print("YES")