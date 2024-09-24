for t in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n//2):
        l.append(n//2+i)
        l.append(i)
    if n%2==1:
        l.append(n-1)
    for i in range(n):
        s=""
        for j in range(m):
            s+=str(l[i]*m+j+1)+" "
        print(s)
