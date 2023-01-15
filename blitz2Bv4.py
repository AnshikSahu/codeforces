for t in range(int(input())):
    n,q=list(map(int,input().split()))
    l=[""]
    for i in range(n):
        s=input()
        c=""
        r=s+l[i]
        for e in r:
            if(not(e in l[i] and e in s)):
                c=c+e
        l.append(c)
    for i in range(q):
        s=input().split()
        p=int(s[0])
        if(s[1] in l[p]):
            print("NO")
        else:
            print("YES")