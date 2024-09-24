n,m=map(int,input().split())
d=[[] for i in range(n)]
for i in range(n):
    u,v,y=map(int,input().split())
    d[u].append((v,y))
    d[v].append((u,y))

def dfs(list1,ele):
    if(len(list1)==0):
        return ([],[],0)
    if(len(d[ele])==0):
        return (list1,[],-1)
    m=d[ele][0][1]
    rem=[]  
    for i in d[ele]:
        list1.remove(i[0])
        m=min(m,i[1])
        rem.append(i[0])
    return (list1,rem,m)

def remov(list,ele):
    rem=[]
    if(len(list)==0):
        return ([],[],0)
    if(len(ele)==0):
        return (list,[],0)
    m=float('inf')
    for i in ele:
        list.remove(i)
        ans=dfs(list,i)
        if(ans[2]==-1):
            return (list,[],-1)
        else:
            list=ans[0]
            rem.append(ans[1])
            m=min(m,ans[2])
    return (list,rem,m)




