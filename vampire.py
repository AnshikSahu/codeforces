def vampire(initialPower,welderPowers):
    n=len(welderPowers)
    welderPowers.sort()
    greenSerums=2
    blueSerums=1
    for i in range(n):
        if initialPower> welderPowers[i]:
            initialPower+=(welderPowers[i]//2)
        else:
            if greenSerums>0 and 2*initialPower>welderPowers[i]:
                initialPower*=2
                greenSerums-=1
                initialPower+=(welderPowers[i]//2)
            elif blueSerums>0 and 3*initialPower>welderPowers[i]:
                initialPower*=3
                blueSerums-=1
                initialPower+=(welderPowers[i]//2)
            elif greenSerums>1 and 4*initialPower>welderPowers[i]:
                initialPower*=4
                greenSerums-=2
                initialPower+=(welderPowers[i]//2)
            else:
                return i+1
    return n
print(vampire(1,[2,1,8,9]))
print(vampire(3,[6,2,60]))