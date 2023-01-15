def splitstring(s):
    l=[]
    for k in range(len(s)):
        if s[k]=="'":
            t=s[k-1]+s[k]
            l.remove(l[-1])
            l.append(t)
        else:
            l.append(s[k])
    return(l)
def generatelegalregion(funcTrue,funcdc):
    l3=[]
    for w in range(len(funcTrue)):
        l3.append(splitstring(funcTrue[w]))
    for w in range(len(funcdc)):
        l3.append(splitstring(funcdc[w]))
    return l3
def countliterals(l1):
    var=0
    for w in range(len(l1)):
        if l1[w]!=None:
            var+=1
    return(var)
def check(l1,l2):
    var=True
    for w in range(len(l1)):
        if (l1[w]!=None and l1[w]!=l2[w]):
            var=False
            break
    return(var) 
def findmaxregion(funcTrue,funcdc):
    l3=[]
    r=generatelegalregion(funcTrue,funcdc)
    for w in range(len(funcTrue)):
        l=splitstring(funcTrue[w])
        m=0
        while m<(len(l)): 
            checkifallcells=0
            temp=l[m]
            l[m],p=None,0
            while (p<(len(r)) and checkifallcells!=2**(len(l)-countliterals(l))):
                if check(l,r[p])==True:
                    checkifallcells+=1
                p+=1
            if checkifallcells==2**(len(l)-countliterals(l)):
                m+=1
            else:
                l[m]=temp
                m+=1
        s=""
        for w in range(len(l)):
            if l[w]!=None:
                s+=l[w]
        l3.append(s)
    return(l3)

func_TRUE = ["a'b'c'd", "a'bcd'", "abc'd'", "abc'd", "ab'cd"]
func_DC = ["a'bc'd","a'bcd","abcd"]
print(findmaxregion(func_TRUE,func_DC))