import copy
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
        change(input())
        l.append(copy.deepcopy(d))
    for i in range(q):
        s=input().split()
        p=l[int(s[0])-1]
        if(s[1] in p.keys()):
            if(p[s[1]]==1):
                print("YES")
            else:
                print("NO")
        else:
            p[s[1]]=1
            print("YES")