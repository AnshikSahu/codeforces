def ancc6():
    n=int(input())
    l= list(map(int,input().strip().split()))[:n]
    l.sort()
    m=int(input())
    d=[]
    for i in range(0,m):
        x=(int(input()))
        c=0
        while(c<n):
            if(l[c]>x):
                break
            c=c+1
        d.append(c)
    for s in d:
        print(s)
ancc6()
    