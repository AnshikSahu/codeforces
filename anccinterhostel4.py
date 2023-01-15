def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
def lcm(a,b):
    return int(a*b/gcd(min(a,b),max(a,b)))
def bus():
    t=int(input())
   # ans=[]
    while(t>0):
        t-=1
        l= list(map(int,input().strip().split()))[:4]
        a=l[0]//l[1] + l[0]//l[2] + l[0]//l[3]
        b=l[0]//lcm(l[1],l[2]) + l[0]//lcm(l[2],l[3]) + l[0]//lcm(l[3],l[1])
        c=l[0]//lcm(l[1],lcm(l[2],l[3]))
        print(a-2*b+3*c)
bus()