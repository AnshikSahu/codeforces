def codemania1():
    t=int(input())
    while(t>0):
        t-=1
        n=int(input())
        l= list(map(int,input().split()))
        c=0
        m=0
        for i in range(0,n):
            if(l[i]>l[m]):
                m=i
        for i in range(m,n):
            if(l[i]!=l[m]):
                break
            c+=1
        s=str(l[m])+" "+str(c)
        print(s)
codemania1()