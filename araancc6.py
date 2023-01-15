n=int(input())
aa=[]
ab=[]
ba=[]
bb=[]
for i in range(0,n):
    l= input().split()
    if(l[0]=="11"):
        aa.append(int(l[1]))
    elif(l[0]=="10"):
        ab.append(int(l[1]))
    elif(l[0]=="01"):
        ba.append(int(l[1]))
    elif(l[0]=="00"):
        bb.append(int(l[1]))
ab.sort(reverse=True)
ba.sort(reverse=True)
x=min(len(ab),len(ba))
n=len(aa)
aa=aa+ab[:x]+ba[:x]
bb=bb+ab[x:]+ba[x:]
bb.sort(reverse=True)
aa=aa+bb[:n]
s=0
for e in aa:
    s=s+e
print(s)

