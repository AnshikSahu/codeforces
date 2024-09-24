def seive(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime
def check(a):
    prv=0
    m=max(a)
    s=seive(m)
    for i in range(0,len(a)):
        c=False
        for j in range(a[i]-prv,1,-1):
            if(s[j]):
                a[i]=a[i]-j
                prv=a[i]
                c=True
                break
        if(not(c)):
            if(a[i]>prv):
                prv=a[i]
                c=True
            else:
                break
    if(c):
        print("YES")
    else:
        print("NO")
        