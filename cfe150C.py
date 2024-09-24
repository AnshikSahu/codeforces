for t in range(int(input())):
    s=input()
    a=0
    at=False
    ad=False
    b=0
    bt=False
    bd=False
    c=0
    ct=False
    cd=False
    d=0
    dt=False
    dd=False
    for i in range(len(s)-1,-1,-1):
        if(s[i]=="A"):
            if(at):
                a+=1
            if(bt):
                b+=1
            if(ct):
                c+=1
            if(dt):
                d+=1
        if(s[i]=="B"):
            if(not at and not ad):
                at=True
                ad=True
                a-=10
            else:
                at=False
            if(bt):
                b+=1
            if(ct):
                c+=10
            if(dt):
                d+=10
        if(s[i]=="C"):
            if(not at and not ad):
                at=True
                ad=True
                a-=100
            else:
                at=False
            if(not bt and not bd):
                bt=True
                bd=True
                b-=100
            else:
                bt=False
            if(ct):
                c+=100
            if(dt):
                d+=100
        if(s[i]=="D"):
            if(not at and not ad):
                at=True
                ad=True
                a-=1000
            else:
                at=False
            if(not bt and not bd):
                bt=True
                bd=True
                b-=1000
            else:
                bt=False
            if(not ct and not cd):
                ct=True
                cd=True
                c-=1000
            else:
                ct=False
            if(dt):
                d+=1000
        if(s[i]=="E"):
            if(not at and not ad):
                at=True
                ad=True
                a-=10000
            else:
                at=False
            if(not bt and not bd):
                bt=True
                bd=True
                b-=10000
            else:
                bt=False
            if(not ct and not cd):
                ct=True
                cd=True
                c-=10000
            else:
                ct=False
            if(not dt and not dd):
                dt=True
                dd=True
                d-=10000
            else:
                dt=False
    a+=1 if ad else 0
    b+=10 if bd else 0
    c+=100 if cd else 0
    d+=1000 if dd else 0
    l=[0]*(len(s)-1)+[1 if s[-1]=="A" else 2 if s[-1]=="B" else 3 if s[-1]=="C" else 4 if s[-1]=="D" else 5]
    val=1 if s[-1]=="A" else 10 if s[-1]=="B" else 100 if s[-1]=="C" else 1000 if s[-1]=="D" else 10000
    for i in range(len(s)-2,-1,-1):
        if(s[i]=="A"):
            l[i]= 1 if l[i+1]<1 else l[i+1]
            val+=1 if l[i+1]<=1 else -1
        elif(s[i]=="B"):
            l[i]= 2 if l[i+1]<2 else l[i+1]
            val+=10 if l[i+1]<=2 else -10
        elif(s[i]=="C"):
            l[i]= 3 if l[i+1]<3 else l[i+1]
            val+=100 if l[i+1]<=3 else -100
        elif(s[i]=="D"):
            l[i]= 4 if l[i+1]<4 else l[i+1]
            val+=1000 if l[i+1]<=4 else -1000
        elif(s[i]=="E"):
            l[i]= 5
            val+=10000
    e=10000
    for i in range(len(s)):
        if(s[i]=='A'):
            if(not bd):
                b+=10-1
                bd=True
            if(not cd):
                c+=100-1
                cd=True
            if(not dd):
                d+=1000-1
                dd=True
            if(l[i]<=1):
                e=min(e,1)
                break
            else:
                e=min(e,-1)
        elif(s[i]=='B'):
            if(not cd):
                c+=100-10
                cd=True
            if(not dd):
                d+=1000-10
                dd=True
            if(l[i]<=2):
                e=min(e,10)
                break
            else:
                e=min(e,-10)
        elif(s[i]=='C'):
            if(not dd):
                d+=1000-100
                dd=True
            if(l[i]<=3):
                e=min(e,100)
                break
            else:
                e=min(e,-100)
        elif(s[i]=='D'):
            if(l[i]<=4):
                e=min(e,1000)
                break
            else:
                e=min(e,-1000)
    e= e*-1+10000
    x=max(a,b,c,d,e)
    print(val+x)