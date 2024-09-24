for t in range(int(input())):
    n,m=map(int,input().split())
    a=sum(list(map(int,input().split())))
    b=sum(list(map(int,input().split())))
    if a>b:
        print("Tsondu")
    elif a<b:
        print("Tenzing")
    else:
        print("Draw")