t=int(input())
while(t>0):
    t-=1
    n=int(input())    
    s=input()
    c=0
    x=s[n//2]
    for i in range(n//2,n):
        if(s[i]==x):
            c+=1
        else:
            break
    c=2*c-1+(n%2==0)
    print(c)