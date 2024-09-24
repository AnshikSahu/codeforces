import math
for t in range(int(input())):
    n,k=map(int,input().split())
    a=int(math.log2(n+1))
    if(k<=a):
        print(2**k)
    else:
        print(n+1)
