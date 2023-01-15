d=dict()
def change(s):
    for e in s:
        if(not(e in d.keys())):
            d[e]=-1
        else:
            d[e]*=-1
for t in range(int(input())):
    n,q=list(map(int,input().split()))
    l=[]
    d=dict()
    for i in range(n):
        l.append(input())
    i=0
    while(i<=n and q>0):
        s=input().split()
        q-=1
        j=int(s[0])
        while(i<j):
            change(l[i])
            i+=1
        while(j<i):
            i-=1
            change(l[i])
        if(s[1] in d.keys()):
            if(d[s[1]]==1):
                print("YES")
            else:
                print("NO")
        else:
            d[s[1]]=1
            print("YES")