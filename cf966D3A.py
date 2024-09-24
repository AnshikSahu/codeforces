for _ in range(int(input())):
    s=input()
    try:
        n=int(s)
        if len(s)>=3 and s[0]=='1' and s[1]=='0' and s[2]!='0' and s[2:]!='1' :
            print("YES")
        else:
            print("NO")
    except:
        print("NO")