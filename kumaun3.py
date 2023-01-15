def check(s):
    s="="+s
    n=len(s)
    i=1
    c=0
    while(i<(n-1)):
        if(s[i]==s[i+1]):
            c+=1
            s=s[0:i]+s[i+2:]
            n=len(s)
            i=i-1
        else:
            i=i+1
    return c
if(check(input())%2!=0):
    print("YES")
else:
    print("NO")