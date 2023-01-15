def search(a,s):
    try:
        x=s.index(a)
    except:
        x=-1
    return x

def check(s,c):
    n=len(s)
    ans=""
    for i in range (n):
        if s[i]==c[i]:
            x="2"
        elif search(s[i],c)>=0 :
            x = "1"
        else :
            x = "0"
        ans=ans+x
    return ans 

        
        
        