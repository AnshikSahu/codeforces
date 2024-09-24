# for t in range(int(input())):
#     n=int(input())
#     l=list(map(int,input().split()))
n=9
l=[14,19,37,59,1,4,4,98,73]
l.sort()
if(n>3):
    m=int((l[(2*n)//3]-l[n//3]+1)/2)
    i=0
    j=n-1
    for k in range(0,(m+1)):
        while(l[i]<=l[0]+2*k):
            i+=1
        while(l[j]>=l[n-1]-2*k):
            j-=1
        i-=1
        j+=1
        if(l[j-1]-l[i+1]<=2*k):
            print(k)
            break
        # for i in range(0,n-2):
        #     for j in range(n-1,i+1,-1):
        #         a=int((l[i]-l[0]+1)/2)
        #         b=int((l[j-1]-l[i+1]+1)/2)
        #         c=int((l[n-1]-l[j]+1)/2)
        #         m=min(max(a,b,c),m)
        # print(m)
    else:
        print(0)
#     i=0
#     j=n-1
#     l.sort()
#     if(n>3):
#         m=int((l[j-1]-l[i+1]+1)/2)
#         while(i<j-1):
#             k=i+1
#             a=m
#             while(k<j-1):
#                 a1=int((l[k]-l[0]+1)/2)
#                 a2=int((l[j-1]-l[k+1]+1)/2)
#                 a3=int((l[n-1]-l[j]+1)/2)
#                 a=min(max(a1,a2,a3),a)
#                 k+=1
#             k=j-1
#             b=m
#             while(k>i+1):
#                 b1=int((l[i]-l[0]+1)/2)
#                 b2=int((l[k-1]-l[i+1]+1)/2)
#                 b3=int((l[n-1]-l[k]+1)/2)
#                 b=min(max(b1,b2,b3),b)
#                 k-=1
#             mi=min(a,b)
#             if(mi<=m):
#                 m=mi
#                 if(mi==a):
#                     i+=1
#                 else:
#                     j-=1
#             else:
#                 break
#         print(m)
#     else:
#         print(0)
