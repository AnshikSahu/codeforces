from math import ceil


def do(n,m,shapes,k):
    maximum=0
    for i in range(n):
        for j in range(i+1,n):
            costs=[]
            max_val=0
            for item in range(m):
                costs.append(max(shapes[i][item],shapes[j][item]))
                max_val+=1/costs[-1]
            max_val=int(k/max_val)
            max_size=0
            for size in range(max_val,0,-1):
                if sum([ceil(size/cost) for cost in costs])<=k:
                    max_size=size
                    break
            maximum=max(maximum,max_size)
    return maximum

n = 4
m = 3
shops = [[3, 2, 5], [1, 3, 2], [2, 2, 2], [1, 1, 1]]
k = 11

print(do(n,m,shops,k))
        
arr=[1,2,3,4,5]

arr.reverse()