for t in range(int(input())):
    n,q=list(map(int,input().split()))
    l=[]
    for i in range(n):
        l.append(input())
    for i in range(q):
        s=input().split()
        p=int(s[0])
        c=0
        for j in range(p):
            if(s[1] in l[j]):
                c+=1
        if(c%2==0):
            print("YES")
        else:
            print("NO")