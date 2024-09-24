def minSwaps(arr):
	n = len(arr)

	# Create two arrays and use
	# as pairs where first array
	# is element and second array
	# is position of first element
	arrpos = [*enumerate(arr)]

	# Sort the array by array element
	# values to get right position of
	# every element as the elements
	# of second array.
	arrpos.sort(key=lambda it: it[1])

	# To keep track of visited elements.
	# Initialize all elements as not
	# visited or false.
	vis = {k: False for k in range(n)}

	# Initialize result
	ans = 0
	for i in range(n):

		# already swapped or
		# already present at
		# correct position
		if vis[i] or arrpos[i][0] == i:
			continue

		# find number of nodes
		# in this cycle and
		# add it to ans
		cycle_size = 0
		j = i

		while not vis[j]:

			# mark node as visited
			vis[j] = True

			# move to next node
			j = arrpos[j][0]
			cycle_size += 1

		# update answer by adding
		# current cycle
		if cycle_size > 0:
			ans += (cycle_size - 1)

	# return answer
	return ans
for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=[False]*n
    x=False
    for i in range(n):
        if(l[i]==i+1):
            c[i]=True
        if(i<n-1):
            if(l[i]==i+2 and l[i+1]==i+1):
                c[i]=True
                c[i+1]=True
                x=True
    a=-1
    an=0
    if(not x):
        for i in range(n-1):
            if((not c[i]) and (not c[i+1])):
                a=i
                break
    if(a>=0):
        for i in range(n):
            if(l[i]==a+2):
                l[i],l[a]=l[a],l[i]
                c[a]=True
            elif(l[i]==a+1):
                l[i],l[a+1]=l[a+1],l[i]
                c[a+1]=True
        an=2
    elif(a<0 and not x):
        an=1
    f=[]
    for i in range(n):
        if(not c[i]):
            f.append(l[i])
    print(an+minSwaps(f))
# Python3 program to find
# minimum number of swaps
# required to sort an array

# Function returns the minimum
# number of swaps required to
# sort the array




