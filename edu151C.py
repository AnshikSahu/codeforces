for t in range(int(input())):
    s=input()
    m=int(input())
    l=list(map(int,[*input()]))
    r=list(map(int,[*input()]))
    d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
    occur={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],0:[]}
    for i in range(len(s)):
        occur[int(s[i])].append(i)
    dp=[-1]*(m+1)
    c=False
    for i in range(m):
        for j in range(l[i],r[i]+1):
            if(d[j]==-1 or len(occur[j])-d[j]<=0 or occur[j][-1]<=dp[i]):
                print("YES")
                c=True
                break
            else:
                while(d[j]<len(occur[j]) and occur[j][d[j]]<=dp[i]):
                    d[j]+=1
                dp[i+1]=max(occur[j][d[j]],dp[i+1])
                d[j]+=1
        if(c):
            break
    if(not c):
        print("NO")
