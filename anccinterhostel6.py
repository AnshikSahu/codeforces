def stu():    
    t=int(input())
    while(t>0):
        t-=1
        l= list(map(int,input().split()))
        a=[0]*(l[0]+1)
        for i in range(0,l[1]):
            x= list(map(int,input().split()))
            for j in range(x[0],x[1]+1):
                a[j]+=1
        s=""
        c=0
        for i in range(1,l[0]+1):
            if(a[i]!=1):
                c+=1
                s=s+" "+str(i)
        print(c)
        print(s)
stu()