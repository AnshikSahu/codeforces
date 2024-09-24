for t in range(int(input())):
    n=int(input())
    s=input()
    l=[0]*n
    c=0
    check=0
    check2=False
    check3=False
    for i in range(n-1,-1,-1):
        if(s[i]=='('):
            c+=1
        else:
            c-=1
        if(c<0):
            break
    if(c==0):
        print("1")
        print(" ".join(map(str,[1]*n)))
        continue
    c=0
    for i in range(n):
        if(s[i]=='('):
            check+=1
            c=c+1
            l[i]=1
        if(s[i]==')'):
            check-=1
            if(c>0):
                check3=True
                c=c-1
                l[i]=1
            else:
                check2=True
                l[i]=2
    for i in range(n):
        if(s[n-i-1]=='(' and c>0):
            c=c-1
            l[n-i-1]=2
    if(check!=0):
        print("-1")
    else:
        if(check2 and check3):
            print("2")
        else:
            print("1")
        if(not check3):
            print(" ".join(map(str,[1]*n)))
        else:
            print(" ".join(map(str,l)))
# for t in range(int(input())):
#     n=int(input())
#     s=input()
#     l=[0]*n
#     c=0
#     c2=0
#     for i in range(n):
#         if(s[i]=='('):
#             l[i]=1
#             c+=1
#         else:
#             if(c>0):
#                 l[i]=1
#                 c-=1
#             else:
#                 l[i]=2
#                 c2+=1
#     for i in range(n-1,-1,-1):
#         if(s[i]=='(' and c2>0):
#             l[i]=2
#             c-=1
#             c2-=1
#     if(c!=0 or c2!=0):
#         print("-1")
#     else:
#         if()      