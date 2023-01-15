def ancc3():
    t=int(input())
    ans=[]
    while(t>0):
        t-=1
        n=int(input())
        m=(n*(n-1)/2)
        arr= list(map(int,input().strip().split()))[:n]
        c=0
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    c+=1
        if(c<m):
            ans.append("Yes")
        else:
            ans.append("No")
    for a in ans:
        print(a)
ancc3()