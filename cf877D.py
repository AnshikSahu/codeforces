def walkable(s):
    n=len(s)
    minR=0
    maxL=False
    maxR=0
    r=False
    for i in range(n):
        if s[i]=='(':
            minR+=1
            if i!=0:
                if(s[i-1]=='('):
                    maxL=True
        else:
            minR-=1
            if i!=0:
                if(s[i-1]==')'):
                    minR=min(minR%2,minR)
                    if(i>1):
                        if(s[i-2]==')'):
                            minR=min(0,minR)
                    maxR=max(minR,maxR)
        if minR+maxR<0:
            if(not maxL):
                return False
                                    
    if(minR>0):
        return False
    else:
        if((-1*(minR+maxR))%2==1):
            return False
    return True
# n,k=map(int,input().split())
# s=input()
# for i in range(k):
#     index=int(input())
#     if s[index-1]=='(':
#         s=s[:index-1]+')'+s[index:]
#     else:
#         s=s[:index-1]+'('+s[index:]
#     if walkable(s):
#         print("YES")
#     else:
#         print("NO")
# while True:
#     print(walkable(input()))
print(walkable("((())"))