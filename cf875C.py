for t in range(int(input())):
    s=input()
    c=['0']*len(s)
    for i in range(len(s)):
        if(s[i]=='?'):
            if(i==0):
                c[i]='0'
            else:
                if(c[i-1]=='1'):
                    c[i]="1"
        else:
            c[i]=s[i]
    print("".join(c))