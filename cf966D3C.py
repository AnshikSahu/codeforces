for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    for i in range(m):
        s=input()
        if len(s)!=n:
            print("NO")
            continue
        flag=1
        dict1={}
        dict2={}
        for j in range(n):
            if (l[j] not in dict1) and (s[j] not in dict2):
                dict1[l[j]]=s[j]
                dict2[s[j]]=l[j]
            elif (l[j] in dict1) and (s[j] in dict2):
                if dict1[l[j]]!=s[j] or dict2[s[j]]!=l[j]:
                    print("NO")
                    flag=0
                    break
            else:
                print("NO")
                flag=0
                break
        if flag:
            print("YES")
            