def calc(matrix,m):
    n=len(matrix)
    suc=[[0]*n for i in range(n)]
    for i in range(n):
        suc[i][0]=matrix[0][i]
        for j in range(1,n):
            suc[i][j]=suc[i][j-1]+matrix[j][i]
    sur=[[0]*n for i in range(n)]
    for i in range(n):
        sur[i][0]=matrix[i][0]
        for j in range(1,n):
            sur[i][j]=sur[i][j-1]+matrix[i][j]
    k=0
    i=0
    while(i<n-k+1):
        s=0
        p=0
        j=0
        while(j<n-k and p<n):
            if(s<=m):
                k_new=j-p+1
                if(i==0):
                    s+=suc[j][i+k_new-1]
                else:
                    s+=suc[j][i+k_new-1]-suc[j][i-1]
                if(p==0):
                    s+=sur[i+k_new-1][j]
                else:
                    s+=sur[i+k_new-1][j]-sur[i][p]
                s-=matrix[i+k_new-1][j]
                k=k_new
                j+=1
            else:
                if(p==0):
                    s-=sur[i+k_new-1][j]
                else:
                    s-=sur[i+k_new-1][j]-sur[i][p]
                if(i==0):
                    s+=suc[p][i+k_new-1]
                else:
                    s+=suc[p][i+k_new-1]-suc[p][i-1]
                s+=matrix[i+k_new-1][p]
                p+=1
                k-=1
        i+=1
    return k
matrix=[[10,20],[5,2]]
m=30
print(calc(matrix,m))
                
            