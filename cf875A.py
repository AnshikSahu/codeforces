for t in range(int(input())):
    l=list(map(int,input().split()))
    if(l[0]%l[1]==0):
        print("2")
        print(l[0]-l[1]//2,l[1]//2)
    else:
        print("1")
        print(l[0])