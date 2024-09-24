for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if l[i] in d:
            d[l[i]].append(i)
        else:
            d[l[i]] = [i]

    def remv(f,b,k):
        # f = [-1] * n
        # b = [-1] * n
        # for i in range(k,n):
        #     if lis[i] != 1:
        #         a = d[l[i]]
        #         lis[i] = 1
        #         for j in a:
        #             if lis[j] != 1 :
        #                 lis[i] = 0
        #                 if(j>i):
        #                     f[i] = i
        #                     b[i] = j
        #                     break
        ans=0
        for i in range(k,n):
            if f[i] != -1:
                # x=lis[:f[i]]+[1]*(b[i]-f[i]+1)+lis[b[i]+1:]
                # both=b[i]-f[i]+1 + remv(x,b[i]+1)
                # first=remv(lis[:f[i]]+[1]+lis[f[i]+1:],i+1)
                # second=remv(lis[:b[i]]+[1]+lis[b[i]+1:],f[i])
                ans=max(ans,both,first,second)
        return ans
    print(f,b,0))
