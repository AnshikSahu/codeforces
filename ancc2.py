def ancc2():
    t=int(input())
    ans=[]
    while(t>0):
        t-=1
        n=int(input())
        l= list(map(int,input().strip().split()))[:n]
        m=l[0]
        for x in l:
            if(x<m):
                m=x
        c=0
        for x in l:
            if(x>m):
                c=c+1
        ans.append(c)
    for i in ans:
        print(i)
ancc2()