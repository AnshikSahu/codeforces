def f(n,m,flowers):
    dict={}
    for i in range(n):
        if flowers[i] in dict:
            dict[flowers[i]]+=1
        else:
            dict[flowers[i]]=1
    keys=list(dict.keys()).sort()
    for i in range(len(keys)):
        