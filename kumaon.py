a=[]
n=int(input())
c=0
def check(x,y):
    c=0
    for e in a:
        if(e[0]==x or e[1]==y):
            c+=1
    return c
while(n>0):
    n-=1
    x,y=list(map(int,input().split()))
    c+=check(x,y)
    a.append((x,y))
print(c)
    