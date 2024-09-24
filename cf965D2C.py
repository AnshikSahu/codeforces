for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    pairs=sorted([[a[i],b[i]] for i in range(n)])
    l=-1
    for i in range(n-1,-1,-1):
        if pairs[i][1]:
            l=i
            break
    if l==-1:
        print(pairs[-1][0]+pairs[(n)//2-1][0])
        continue
    if l==n-1:
        print(pairs[-1][0]+k+pairs[(n)//2-1][0])
        continue
    if l<=(n)//2-1:
        extra=pairs[(n)//2-1][0]-pairs[l][0]+1
        if extra>k:
            print(pairs[-1][0]+pairs[(n)//2-1][0])
            continue
        k=k-extra
        pairs[l][0]+=extra
        while l<n-1 and pairs[l][0]>=pairs[l+1][0]:
            pairs[l],pairs[l+1]=pairs[l+1],pairs[l]
            l+=1
    ans=pairs[-1][0]+pairs[(n)//2-1][0]
    last=(n)//2-1
    while k>0:
        ans=max(ans,pairs[l][0]+k+pairs[(n)//2-1][0])
        if pairs[n//2-1][1]:
            last=n//2-1
        else:
            while last>=0 and pairs[last][1]==0:
                last-=1
        if last==-1:
            break
        extra=pairs[(n)//2-1][0]-pairs[last][0]+1
        if extra==0:
            extra=1
        if extra>k:
            pairs[last][0]+=k
            break
        k=k-extra
        pairs[last][0]+=extra
        last_copy=last
        while last_copy<n-1 and pairs[last_copy][0]>pairs[last_copy+1][0]:
            pairs[last_copy],pairs[last_copy+1]=pairs[last_copy+1],pairs[last_copy]
            last_copy+=1
    ans=max(ans,pairs[-1][0]+pairs[(n)//2-1][0])
    print(ans)
        
        
            
            
            
            
    
    