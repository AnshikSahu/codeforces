for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=input()
    l=0
    while l<n and s[l]=="R":
        l+=1
    r=n-1
    while r>=0 and s[r]=="L":
        r-=1
    ans=0
    height=0
    while l<r:
        while l<=r and s[l]=="R":
            ans+=(a[l]*height)
            l+=1
        while l<=r and s[r]=="L":
            ans+=(a[r]*height)
            r-=1
        if l>=r:
            break
        height+=1
        ans+=((a[l]+a[r])*height)
        l+=1
        r-=1
        if l==r:
            ans+=(a[l]*height)
    print(ans)