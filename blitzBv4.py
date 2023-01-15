for t in range(int(input())):
    n,q=list(map(int,input().split()))
    l=[""]
    for i in range(n):
        s=input()
        c=""
        for e in s:
            if(not(e in l[i])):
                c=c+e
        for e in l[i]:
            if(not(e in s)):
                c+=e
        l.append(c)
    for i in range(q):
        s=input().split()
        p=int(s[0])
        if(s[1] in l[p]):
            print("NO")
        else:
            print("YES")