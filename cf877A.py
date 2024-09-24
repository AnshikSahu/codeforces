for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=l[0]
    n=0
    for i in l:
        if i>m:
            m=i
        if i<0:
            n=i
            break
    if n<0:
        print(n)
    else:
        print(m)