for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=[[i-1] for i in range(n)]
    for i in range(m):
        u,v=map(int,input().split())
        if u>v:
            u,v=v,u
        graph[v-1].append(u-1)
    