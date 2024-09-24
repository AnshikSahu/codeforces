# def available(x,y,centres,xs,ys,rad):
#     for i in range(len(centres)):
#         if (x-centres[i][0])**2+(y-centres[i][1])**2<=rad:
#             if x==9 and y==7:
#                 print("centre",centres[i])
#                 print("rad",rad)
#                 print((x-centres[i][0])**2+(y-centres[i][1])**2)
#             return False
#     return True

# for _ in range(int(input())):
#     n = int(input())
#     centres=[]
#     for i in range(n):
#         x,y=map(int,input().split())
#         centres.append((x,y))
    
#     xs,ys,xt,yt=map(int,input().split())
    
#     #dfs
#     stack=[(xs,ys)]
#     visited=set()
#     visited.add((xs,ys))
    
#     delta=[]
#     if xt-xs>0:
#         dx=1
#     elif xt-xs<0:
#         dx=-1
#     else:
#         dx=0
    
#     if yt-ys>0:
#         dy=1
#     elif yt-ys<0:
#         dy=-1
#     else:
#         dy=0
     
#     if dx!=0 and dy!=0:
#         delta.append((dx,dy))   
#     delta.append((dx,0))
#     delta.append((0,dy))
    
#     rad_stack=[0]
    
#     flag=0
#     while stack:
#         x,y=stack.pop()
#         rad=rad_stack.pop()
#         if x==xt and y==yt:
#             print("YES")
#             flag=1
#             break
        
#         for dx,dy in delta:
#             if (xt-x-dx)*dx>=0 and (yt-y-dy)*dy>=0 and  available(x+dx,y+dy,centres,xs,ys,rad+1) and (x+dx,y+dy) not in visited:
#                 visited.add((x+dx,y+dy))
#                 stack.append((x+dx,y+dy))
#                 rad_stack.append(rad+1)
#     if flag==0:
#         print("NO")


for _ in range(int(input())):
    n = int(input())
    centres=[]
    for i in range(n):
        x,y=map(int,input().split())
        centres.append((x,y))
    
    xs,ys,xt,yt=map(int,input().split())
    if xs!=xt:
        line=((yt-ys)/(xt-xs),-1,(xs*yt-ys*xt)/(xs-xt))
        foot=[]
        for i in centres:
            x,y=i
            xf=x-(line[0]*(x*line[0]-y+line[2]))/(line[0]**2+1)
            yf=y+((x*line[0]-y+line[2])/(line[0]**2+1))
            if (xf-xs)*(xf-xt)<=0 and (yf-ys)*(yf-yt)<=0:
                foot.append((xf,yf)) 
    else:
        foot=[(xs,y) for x,y in centres if (y-ys)*(y-yt)<=0]

    flag=0  
    for i in range(len(foot)):
        x,y=centres[i]
        xf,yf=foot[i]
        if (x-xf)**2+(y-yf)**2<=(xf-xs)**2+(y-ys)**2:
            print("NO")
            flag=1
            break
    
    if flag==0:
        print("YES")
    
    