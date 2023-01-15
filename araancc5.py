n=int(input())
l1= list(map(int,input().split()))
l2= list(map(int,input().split()))
i=1
a=[0]*n
for e in l1:
    a[e-1]=i
    i+=1
for i in range(0,n):
    l2[i]=a[l2[i]-1]
c=0
for i in range(0,n-1):
    if(min(l2[i:])!=l2[i]):
        c+=1
print(c)
