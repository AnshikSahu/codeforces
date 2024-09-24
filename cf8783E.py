for y in range(int(input())):
    s1=input()
    block=[-1]*len(s1)
    s2=input()
    t,k=map(int,input().split())
    for i in range(k):
        q=list(map(int,input().split()))
        if(q[0]==1):
            block[q[1]-1]=t+i
        elif(q[0]==2):
            if(q[1]==1):
                if(q[3]==2):
                    a=s1[q[2]-1]
                    s1=s1[:q[2]-1]+s2[q[4]-1]+s1[q[2]:]
                    s2=s2[:q[4]-1]+a+s2[q[4]:]
                else:
                    a,b=min(q[2],q[4]),max(q[2],q[4])
                    s1=s1[:a-1]+s1[b-1]+s1[a:b-1]+s1[a-1]+s1[b:]
            else:
                if(q[3]==1):
                    a=s1[q[4]-1]
                    s1=s1[:q[4]-1]+s2[q[2]-1]+s1[q[4]:]
                    s2=s2[:q[2]-1]+a+s2[q[2]:]
                else:
                    a,b=min(q[2],q[4]),max(q[2],q[4])
                    s2=s2[:a-1]+s2[b-1]+s2[a:b-1]+s2[a-1]+s2[b:]
        else:
            c=True
            for j in range(len(s1)):
                if(block[j]<=i):
                    if(s1[j]!=s2[j]):
                        c=False
                        break
            if(c):
                print("YES")
            else:
                print("NO")

