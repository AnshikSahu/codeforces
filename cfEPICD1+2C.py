def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)

for _ in range(int(input())):
    n = int(input())
    centres=[]
    for i in range(n):
        x,y=map(int,input().split())
        centres.append((x,y))
    
    xs,ys,xt,yt=map(int,input().split())
    
    m=1e20
    for i in range(n):
        x,y=centres[i]
        distance=dist(x,y,xt,yt)
        m=min(m,distance)
        
    if m>dist(xs,ys,xt,yt):
        print("YES")
    else:
        print("NO")