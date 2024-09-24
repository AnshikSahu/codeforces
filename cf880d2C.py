for t in range(int(input())):
    A,B,C,k=map(int,input().split())
    if(A>C or B>C or max(A,B)<C-1):
        print(-1)
        continue
    c=10**C
    a=10**A
    b=10**B
    done=0
    d1=0
    for i in range(a//10,a):
        r1l=c//10-i if c//10>i else 1
        r1h=c-i-1 if c>i-1 else 1
        r2l=b//10 
        r2h=b-1 if b>1 else 1
        if(r1h>=r2l and r2h>=r1l and r1l<=r1h and r2l<=r2h):
            a=min(r1h,r2h)-max(r1l,r2l)+1
            if(done+a>=k):
                d1=i
                break
            done+=a
    if(d1==0):
        print(-1)
        continue
    d2=max(r1l,r2l)+k-done-1
    print(str(d1)+" + "+str(d2)+" = "+str(d1+d2))