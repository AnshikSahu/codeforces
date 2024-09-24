for t in range(int(input())):
    q=int(input())
    l=list(map(int,input().split()))
    a=l[0]
    c=False
    print("1",end="")
    p=l[0]
    for i in range(1,q,1):
        if(l[i]>=p and c==False):
            print("1",end="")
            p=l[i]
        elif(l[i]>=p and c==True and l[i]<=a):
            print("1",end="")
            p=l[i]
        elif(l[i]<=p and c==False and l[i]<=a):
            print("1",end="")
            p=l[i]
            c=True
        else:
            print("0",end="")
    print()