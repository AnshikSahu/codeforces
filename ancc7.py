def ancc7():
    c= list(map(int,input().strip().split()))[:2]
    n=c[0]
    k=c[1]
    r=[[-1,0,0]]
    c=0
    for i in range(0,n):
        l= list(map(int,input().strip().split()))[:2]
        j=0
        while j<c+1:
            j=j+c+2
            if(r[j-c-2][0]<l[0]):
                j=j-c-1
            elif(r[j-c-2][0]==l[0] and r[j-c-2][1]>l[1]):
                j=j-c-1
            elif(r[j-c-2][0]==l[0] and r[j-c-2][1]==l[1]):
                r[j-c-2][2]+=1
            else:
                r.insert(j-c-2,[l[0],l[1],1])
                c=c+1
        if(j==c+1):
            r.append([l[0],l[1],1])
            c=c+1
    s=0
    while(c>0):
        s=s+r[c][2]
        if(s>=k):
            print(r[c][2])
            break
        c-=1        
ancc7()