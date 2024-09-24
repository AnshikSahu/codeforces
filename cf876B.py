from heapq import heappop, heappush, heapify
for t in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[0])

    a = l[0][0]
    p = []
    heapify(p)
    sum = 0

    for i in range(n):
        if l[i][0] == a:
            heappush(p, -l[i][1])
        else:
            print(p)
            for i in range(len(p)):
                if(i<a):
                    sum -= heappop(p)
                else:
                    _=heappop(p)
            heappush(p, -l[i][1])
            a = l[i][0]
    for j in range(min(a, len(p))):
        sum -= heappop(p)
    print(sum)
