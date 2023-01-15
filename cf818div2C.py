for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=True
    d=True
    for i in range(n):
        if((a[i]>b[i] or b[i]>b[(i+1)%n]+1)and(a[i]!=b[i])):
            c=False
            break
    if(c):
        print("YES")
    else:
        print("NO")