for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=True
    c=[0]*n
    a1=[True]*n
    a2=[True]*n
    res2=[0]*n
    res1=[0]*n
    for e in l:
        c[e-1]+=1
        if(c[e-1]>2):
            x=False
    for i in range(0,n):
        x=not x
        if(a1[l[i]-1]):
            res1[i]=l[i]
            a1[l[i]-1]=False
            for j in range(l[i]-1,-1,-1):
                if(a2[j]==True and c[j]<2):
                    c[j]+=1
                    a2[j]=False
                    res2[i]=j+1
                    x=not x
                    break
        else:
            res2[i]=l[i]
            a2[l[i]-1]=False
            for j in range(l[i]-1,-1,-1):
                if(a1[j]==True and c[j]<2):
                    c[j]+=1
                    a1[j]=False
                    res1[i]=j+1
                    x=not x
                    break
        if(not x):
            break
    if(x):
        print("YES")
        print(' '.join([str(elem) for elem in res1]))
        print(' '.join([str(elem) for elem in res2]))   
    else:
        print("NO")