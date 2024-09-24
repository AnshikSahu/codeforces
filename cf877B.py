for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    one=-1
    two=-1
    last=-1
    for i in range(n):
        if l[i]==1:
            one=i+1
        if l[i]==2:
            two=i+1
        if l[i]==n:
            last=i+1
        if one!=-1 and two!=-1 and last!=-1:
            break
    if (two<last and last<one) or (one<last and last<two):
        print(str(one)+" "+str(one))
    else:
        if (one<two and two<last) or (last<two and two<one):
            print(str(two)+" "+str(last))
        else:
            print(str(last)+" "+str(one))
        