for i in range(int(input())):
    n=int(input())
    s=input()
    c=False
    ans=s[0]
    for i in range(1,n):
        if c:
            ans+=s[i]
            c=False
            continue
        if s[i]==ans[-1]:
            c=True
    print(ans)