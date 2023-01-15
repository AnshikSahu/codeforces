def generate_combinations(n, r, index=0):
    global keeper
    if r == 0:
        return []
    else:
        C = []
        for i in range(index, n - r + 1):
            if keeper[i].get(r - 1) == None:
                keeper[i][r - 1] = generate_combinations(n, r - 1, i + 1)
            C1 = keeper[i][r - 1]
            if C1 == []:
                C.append([i])
            for c in C1:
                C.append([i] + c)
        return(C)


N = int(input('N: '))
keeper = {i: {} for i in range(N)}
L = [[]]
for i in range(1, N + 1):
    for element in generate_combinations(N, i):
        L.append(element)
print(L)
