# can add any char to string
# can copy all string to buffer
# can add buffer to string

def text_editor(S):
    n=len(S)
    for i in range(n//2,1,-1):
        p=S[:i]
        if p==S[i:2*i]:
            for j in range(2,n//i):
                if p==S[j*i:(j+1)*i]:
                    return p,j+1
            return p,2
    return S,1

def num(S):
    x=text_editor(S)
    if(x[1]==1):
        return len(S)
    else:
        return num(x[0])+len(S)-len(x[0])*x[1]+x[1]
    
def num2(S):
    buffer=ord(S[0])-ord('a')
    n=len(S)
    dp=[n]*n
    dp[0]=1
    hash=[0]*n
    hash[0]=ord(S[0])-ord('a')
    for i in range(1,n):
        hash[i]=hash[i-1]*26+ord(S[i])-ord('a')
    for i in range(1,n):
        if(2*i-1<n):
            if(hash[2*i-1]-hash[i-1]==buffer):
                dp[2*i-1]=dp[i-1]+2
                j=2*i
                while(hash[j+i-1]-hash[j-1]==buffer and j+i<=len(S)):
                        dp[j+i-1]=dp[j-1]+1
                        j+=i
            buffer=buffer*26+ord(S[i])-ord('a')
        dp[i]=min(dp[i],dp[i-1]+1)
    return dp[-1]


print(num("abaaabaaabaaab"))
print(num2("abaaabaaabaaab"))