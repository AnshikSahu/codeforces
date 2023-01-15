for t in range(int(input())):
    n=int(input())
    c=0
    while(n%2==0):
        n=n/2
        c+=1
    n=n//2
    if(n>0):
        print(2**c)
    else:
        if(c==0):
            print(3)
        else:
            print(2**c+1)