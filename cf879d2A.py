for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    neg=0
    for i in l:
        if i<0:
            neg+=1
    n=n//2
    if n%2!=0:
        n-=1
    if neg<=n:
        print(neg%2)
    else:
        print(neg-n)
