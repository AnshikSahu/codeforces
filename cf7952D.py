for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    c="YES"
    for e in l:
        if e<0:
            s=0
        else:
            if(s>0):
                c="NO"
                break
            s+=e
    print(c)