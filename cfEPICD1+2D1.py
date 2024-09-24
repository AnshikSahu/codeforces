for _ in range(int(input())):
    n,q=map(int,input().split())
    og_tree=[0]+list(map(int,input().split()))
    dfs=list(map(int,input().split()))
    
    new_tree=[-1]*n
    
    def find_tree(dfs,parent,i,j):
        global new_tree
        if i>=j:
            return
        root=dfs[i]
        new_tree[root-1]=parent
        if i+1==j:
            return
        find_tree(dfs,root,i+1,(i+j+1)//2)
        find_tree(dfs,root,(i+j+1)//2,j)
    
    find_tree(dfs,0,0,len(dfs))
    print("og_tree",og_tree)
    print ("new_tree",new_tree)
    for i in range(q):
        x,y=map(int,input().split())
        px=dfs[x-1]
        py=dfs[y-1]
        new_tree[px-1],new_tree[py-1]=new_tree[py-1],new_tree[px-1]
        print("new_tree",new_tree)
        if new_tree==og_tree:
            print("YES")
        else:
            print("NO")
        
    