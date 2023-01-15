s=input()
c=0
for e in s:
    if(e=="1"):
        c+=1
s=1
y=10**9+7
def power(a,n):
    if(n==0):
        return 1
    x=power(a,n//2)%y
    z=(x*x)%y
    if(n%2!=0):
        z=(z*a)%y
    return z
print(power(2,c))