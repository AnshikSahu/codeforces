def answer(n,a,b):
    f=0
    ba=0
    for i in range(n):
        if(a[i]!=b[i]):
            f+=1
        if(a[i]!=b[n-i-1]):
            ba+=1
    p=0
    q=0
    if(f==0):
        p=0
    elif(f%2==0):
        p=2*f
    else:
        p=2*f-1
    if(ba==0):
        q=2
    elif(ba%2==0):
        q=2*ba-1
    else:
        q=2*ba
    print(min(p,q))
for t in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    answer(n,a,b)
    # reva=a[::-1]
    # s=0
    # r=0
    # for i in range(n):
    #     if(a[i]!=b[i]):
    #         s+=1
    #     if(reva[i]!=b[i]):
    #         r+=1
    # if(s>r):
    #     rev=True
    # elif(r>s):
    #     rev=False
    # else:
    #     if(r%2==0 and r!=0):
    #         rev=True
    #     else:
    #         rev=False
    # m=min(s,r)
    # if(m==0 and rev):
    #     m=2
    # elif(m==0 and not rev):
    #     m=0
    # elif(m==n):
    #     m=2*n-1
    # else:
    #     m=2*m-1+rev
    # print(m)