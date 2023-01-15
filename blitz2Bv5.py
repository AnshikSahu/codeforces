for t in range(int(input())):
    n,q=list(map(int,input().split()))
    l=[""]
    for i in range(n):
        s=input()
        l.append(l[i]+s)
    for i in range(q):
        s=input().split()
        p=int(s[0])
        c=l[p].count(s[1])
        if(c%2==0):
            print("YES")
        else:
            print("NO")