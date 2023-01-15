def ancc5():
    l= list(map(int,input().strip().split()))[:2]
    D=8*(l[0]+l[1])+9
    d=D**0.5
    ans=2*l[0]+3-d
    ans=ans/2
    print(int(ans))
ancc5()