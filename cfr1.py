for i in range(0,int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l[0]=l[0]-1
    c=True
    for i in range(1,n):
        if(l[i]<=l[0]):
            c=False
            break
    if(c):
        print("Bob")
    else:
        print("Alice")