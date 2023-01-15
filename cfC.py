import copy
def check(m):
    for e in m:
        x=e.copy()
        x.sort()
        if(e!=x):
            return False
    return True
def exchange(m,i,j):
    for e in m:
        k=e[i]
        e[i]=e[j]
        e[j]=k
    return m
t=int(input())
while(t>0):
    x=-1
    t-=1
    l= list(map(int,input().split()))
    m=[]
    for i in range(0,l[0]):
        r= list(map(int,input().split()))
        m.append(r)
    for i in range(0,l[1]):
        for j in range(0,l[1]):
            z=copy.deepcopy(m)
            z=exchange(z,i,j)
            if(check(z)):
                x=j
                break
        if(x>-1):
            print(str(i+1)+" "+str(x+1))
            break
    if(x==-1):
        print("-1")