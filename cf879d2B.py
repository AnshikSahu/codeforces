def answer(l,r):
    if(len(l)==0):
        return 0
    if(len(l)!=len(r)):
        return int(r[0])+(len(r)-1)*9
    d=len(r)
    ans=0
    for i in range(len(r)):
        d-=1
        if(l[i]!=r[i]):
            ans+=int(r[i])-int(l[i])
            break
    return(ans+9*d)
for t in range(int(input())):
    l,r=input().split()
    ans=answer(l,r)
    print(ans)
#     ans=0
#     if(len(r)>len(l)):
#         c=True
#         for i in range(1,len(r)-len(l)):
#             if(r[i]!='9'):
#                 c=False
#                 break
#         if(c):
#             ans=int(r[0])+(len(r)-1)*9
#             print(ans)
#             continue
#         ans=int(r[0])+(len(r)-1)*9-1
#         print(ans)
#         continue
#     d=len(r)
#     for i in range(len(r)):
#         d-=1
#         if(l[i]!=r[i]):
#             print(l[i],r[i],d)
#             ans+=int(r[i])-int(l[i])
#             break
#     print(ans+9*d)