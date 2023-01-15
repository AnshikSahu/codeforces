n=int(input())-2000
l= list(map(int,input().strip().split()))[:2]
z=(10**9 + 7)
for i in range(2,n+1):
    a=l[1]%z
    l[1]+=l[0]%z
    l[0]=a%z
print(l[1]%z)