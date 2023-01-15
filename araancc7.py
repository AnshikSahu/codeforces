t=int(input())
def binary(x):
    a=[]
    while(x>0):
        a.append(x%2)
        x=x//2
    return a
while(t>0):
    t=t-1
    l= list(map(int,input().split()))
    n=l[0]
    m=l[1]
    if(n>m):
        print(0)
    else:
        m_=binary(m)
        p=len(m_)
        n_=binary(n)
        q=len(n_)
        if(m_[q-1]==1):
            print((m+1)^n)
        else:
            x=(m//(2**q))*(2**q)
            print((x+n)^n)