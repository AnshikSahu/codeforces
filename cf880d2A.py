for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=[0]*101
    for i in range(n):
        l[a[i]]+=1
    c=True
    for i in range(1,101):
        if(l[i]>l[i-1]):
            print("NO")
            c=False
            break
    if(c):
        print("YES")