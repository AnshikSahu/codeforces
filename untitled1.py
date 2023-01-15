n,m=list(map(int,input().split()))
a=[True]*n
b=[True]*n
s=""
def count():
    c=0
    for i in range(n):
        if(a[i]):
            for j in range(n):
                if(b[j]):
                    c+=1
for i in range(m):
    x,y=list(map(int,input().split()))
    a[x-1]=False
    b[y-1]=False
    s=s+str(count())
print(s)       