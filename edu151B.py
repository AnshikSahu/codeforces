for t in range(int(input())):
    xa,ya=map(int,input().split())
    xb,yb=map(int,input().split())
    xc,yc=map(int,input().split())
    dxb=xb-xa
    dyb=yb-ya
    dxc=xc-xa
    dyc=yc-ya
    print(1+(dxb*dxc>0)*min(abs(dxb),abs(dxc))+(dyb*dyc>0)*min(abs(dyb),abs(dyc)))