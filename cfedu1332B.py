def change(a):
    a[0],a[-1]=a[-1],a[0]
    return a
for i in range(int(input())):
    n=int(input())
    print(n)
    a=list(range(1,n+1))
    for i in range(n-1):
        print(*a)
        a=a[0:i]+change(a[i:n])
    print(*a)
    