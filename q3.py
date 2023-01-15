def Highest():
    high = 0
    for i in queue:
        if i[1] >= queue[high][1]:
            high = i
    return queue[high][0]
def Order(orderID: int, BillValue:int):
    queue.append((orderID, BillValue))
def Serve():
    high = Highest()
    for i in queue:
        if high in i:
            queue.pop(i)
            break
n= int(input())
queue= []
for i in range(n):
    c=input()
    if "Order" in c:
        x1 = c.split()
        x2 = []
        for j in x1:
            if j.isdigit():
                x2.append(int(j))
        Order(x2[0], x2[1])
    elif c == "Serve":
        Serve()
    elif c == "Highest":
        print(Highest())
