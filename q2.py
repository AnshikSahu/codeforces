Line = []
def Issue():
    if len(Line) == 0:
        print("Invalid")
    else:
        Line.pop(0)
def Join(AadharID: int):
    Line.append(AadharID)
def Check():
    if len(Line) == 0:
        print("Invalid")
    else:
        print(Line[0])
def GetLine():
    if len(Line) == 0:
        print("Invalid")
    else:
        s=""
        for i in range(len(Line)):
            s+=str(Line[i])+" "
    print(s)
n = int(input())
for i in range(n):
    c=input()
    if "Join" in c:
        x = int(c[5:])
        Join(x)
    elif c == "Issue":
        Issue()
    elif c == "GetLcne":
        GetLine()
    elif c == "Check":
        Check()
    else:
        print("Invalid")