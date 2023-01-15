def ancc1():
    t=int(input())
    ans=[]
    while(t>0):
        t-=1
        c= list(map(int,input().strip().split()))[:2]
        n=c[0]
        H=c[1]
        l= list(map(int,input().strip().split()))[:n]
        if(n<2 and H>l[0]):
            i=-1
        else:
            if(n==1):
                mx=l[0]
                smx=l[0]
            elif(l[0]>l[1]):
                mx=l[0]
                smx=l[1]
            else:
                mx=l[1]
                smx=l[0]
            if(mx>0):
                for i in range(2,n):
                    if l[i]>mx:
                        smx=mx
                        mx=l[i]
                    elif l[i]>smx:
                           smx=l[i]
                i=0
                while(H>0):
                    if(i%2==0):
                        H-=mx
                    else:
                        H-=smx
                    i+=1
                ans.append(i)
            else:
                i=-1
    for i in ans:
            print(i)
ancc1()