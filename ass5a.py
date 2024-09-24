data=[]
used=[]
garbage=[]
def index_of(x):
    for i in range(0,len(data)):
        if(type(data[i])==tuple):
            if(data[i][0]==x):
                return i
        else:
            if(type(data[i])== bool or type(x)== bool):
                if(data[i]==x and type(data[i])==type(x)):
                    return i
            elif(data[i] == x):
                return i
    return -1
def value(x):
    if(x.strip("-").isdigit()):
        r=(int(x),"int")
    elif(x.replace(".","",1).strip("-").isdigit()):
        r=(float(x),"float")
    elif(x=="True"):
        r=(True,"boolean")
    elif(x=="False"):
        r=(False,"boolean")
    else:
        i=index_of(x)
        if(i<0):
            raise Exception("variable "+x+" not initialised")
        return value(str(data[data[i][1]]))
    if(index_of(r[0])==-1):
        data.append(r[0])
    return r
def assign(a,b):
    if(a.replace(".","",1).strip("-").isdigit() or a=="True" or a=="False"):
        raise Exception("Invalid variable name: "+a)
    y=index_of(value(b)[0])
    p=index_of(a)
    if(p==-1):
        data.append((a,y))
    else:
        data[p]=(a,y)
def unary(a,b):
    if(a=="-"):
        return str(-(value(b)[0]))
    elif(a=="not"):
        return str(not(value(b)[0]))
    else:
        raise Exception("Invalid unary operator: "+a)
def member(L,x):
    for i in range(0,len(L)):
        if(L[i]==x):
            return i
    return -1
def binary(L):
    x=value(L[0])[0]
    y=value(L[2])[0]
    if(L[1]=="+"):
        return str(x+y)
    elif(L[1]=="-"):
        return str(x-y)
    elif(L[1]=="*"):
        return str(x*y)
    elif(L[1]=="/"):
        return str(x/y)
    elif(L[1]==">"):
        return str(x>y)
    elif(L[1]=="<"):
        return str(x<y)
    elif(L[1]=="<="):
        return str(x<=y)
    elif(L[1]==">="):
        return str(x>=y)
    elif(L[1]=="=="):
        return str(x==y)
    elif(L[1]=="!="):
        return str(x!=y)
    elif(L[1]=="and"):
        return str(x and y)
    elif(L[1]=="or"):
        return str(x or y)
    else:
        raise Exception("Invalid binary operator: "+L[1])
def evaluate(L):
    if(len(L)==3 and L[1]=="="):
        assign(L[0],L[2])
    elif(len(L)==4 and L[1]=="="):
        assign(L[0],unary(L[2],L[3]))
    elif(len(L)==5 and L[1]=="="):
        assign(L[0],binary(L[2:]))
    else:
        raise Exception("Invalid statement: ",L)
def value_of_variables():
    print("Values of variables are:")
    for i in range(0,len(data)):
        if(type(data[i])==tuple):
            print(data[i][0]+"="+str(data[data[i][1]]))
            used.append(data[i][1])
    if(len(used)==0):
        print("No variables present")
def unused():
    for i in range(0,len(data)):
        if(not(type(data[i])==tuple)):
            if(member(used,i)==-1):
                garbage.append(data[i])
def output():
    value_of_variables()
    unused()
    if(len(garbage)):
        print("Garbage values: ",garbage)
    else:
        print("No garbage")
lines = []
with open('input_file.txt') as f:
    lines = f.readlines()
for statement in lines:
    token_list = statement.split()
    evaluate(token_list)
output()