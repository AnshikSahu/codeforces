def BS(arr,val,high,low):
    mid=(high+low)//2
    if(arr[mid]==val):
        return(mid,True)
    if(high==low):
        if(arr[mid]>val):
            return(mid,False)
        else:
            return(mid+1,False)
    if(arr[mid]>val):
        return BS(arr,val,mid,low)
    if(arr[mid]<val):
        return BS(arr,val,high,mid+1)
t=int(input())
ans=[]
while(t>0):
    t-=1
    n=int(input())
    l= list(map(int,input().strip().split()))[:n]
    l.sort()
    c=0
    for i in range(0,n-2):
        x=0
        z=BS(l,2*l[i],len(l)-1,i)[0]
        for j in range(z,len(l)-1):
            r=BS(l,2*l[j],len(l)-1,j)[0]
            if(r<len(l)):
                x=1
                del l[j]
                del l[r-1]
                break
        if(x==0):
            break
        c+=1
    ans.append(c)
for y in ans:
    print(y)
            