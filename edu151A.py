for t in range(int(input())):
    n,k,x=map(int,input().split())
    if(x!=1):
        print("YES")
        print(n)
        print(*([1]*n))
    else:
        if(k>=3):
            if(n>1):
                print("YES")
                if(n%2==0):
                    print(n//2)
                    print(*([2]*(n//2)))
                else:
                    print(n//2)
                    print(*([2]*(n//2-1)+[3]))
            else:
                print("NO")
        elif(k==2 and n%2==0):
            print("YES")
            print(n//2)
            print(*([2]*(n//2)))
        else:
            print("NO")