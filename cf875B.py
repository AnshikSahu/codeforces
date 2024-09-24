for t in range(int(input())):
    n=int(input())
    s=input()
    c=1
    m=0
    char=s[0]
    for i in range(len(s)-1):
        if(s[i+1]==char):
            c+=1
        else:
            m=max(c+1,m)
            char=s[i+1]
            c=1
    m=max(c+1,m)
    print(m)