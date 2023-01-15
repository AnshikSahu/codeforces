for t in range(int(input())):
    n,m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    s=-1*m
    for e in l:
        s+=e
    if(s>0):
        print(s)
    else:
        print(0)