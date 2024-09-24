for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    p=[]
    k=False
    for i in range(n-1,-1,-1):
        if(l[i]==1):
            c+=1
            if(i==0 or l[i-1]==0):
                if(c>len(p)):
                    k=True
                    break
                p.append(c)
                c=0
            else:
                p.append(0)
        else:
            p.append(0)
    if(k):
        print("NO")
    else:
        print("YES")
        print(*p)
                