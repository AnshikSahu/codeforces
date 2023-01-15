"""def BS(arr,val,high,low):
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
def paint():
    t=int(input())
    while(t>0):
        t-=1
        n=int(input())
        l= list(map(int,input().split()))
        a=[-1]
        c=0
        for i in range(0,n):
            x=0
            while(l[i]>0):
                x+=1*(l[i]%2)
                l[i]=l[i]//2
            r=BS(a,x,c,0)
            if(not r[1]):
                c+=1
                a.insert(r[0],x)
            l[i]=x
        s=str(BS(a,l[0],c,0)[0])
        for i in range(1,n):
            s=s+" "+str(BS(a,l[i],c,0)[0])
        print(c)
        print(s)
paint()"""
def paint():
    t=int(input())
    while(t>0):
        t-=1
        n=int(input())
        l= list(map(int,input().split()))
        c=0
        for i in range(0,n):
            x=0
            while(l[i]>0):
                x+=1*(l[i]%2)
                l[i]=l[i]//2
            l[i]=x
        s=""
        for i in range(0,n):
            k=l[i]
            if(k>0):
                c+=1
                for j in range(i,n):
                    if(l[j]==k):
                        l[j]=-1*c
            s=s+" "+str(-1*l[i])
        print(c)
        print(s)
paint()