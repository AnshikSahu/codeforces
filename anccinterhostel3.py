n,k= list(map(int,input().split()))
s=input()
l=[]
st=[]
for i in range(0,n):
    if(s[i]=='W'):
        st.append(1)
    else:
        st.append(0)
        l.append(i)
ln=len(l)
def case(k,l):
    r=[]
    for i in range(0,2**(l)):
        x=[]
        j=i
        c=0
        for m in range(0,l):
            x.append(j%2)
            if(j%2==1):
                c+=1
            j=j//2
        if(c==k):
            r.append(x)
    return(r)
def maxst(ind):
    m = 0
    c1 =0
    l = len(ind)
    for j in range(l):
        if ind[j]==0:
            if c1>m:
                m = c1
            c1 = 0
        else :
            c1+=1     
    return max(m,c1)
if(k==0):
    print(maxst(st))
elif(k<ln):
    r=case(k,ln)
    m=0
    for e in r:
        s2=st.copy()
        for y in range(0,ln):
            s2[l[y]]=e[y]
        x=maxst(m)
        if(x>m):
            m=x
    print(m)
else:
    print(n)
        