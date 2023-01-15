for i in range(int(input())):
    n=int(input())
    c=0
    if(n==1):
        c=1
    c+=n//3+(n%3>0)
    print(c)