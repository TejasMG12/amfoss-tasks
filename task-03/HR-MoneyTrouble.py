a= list(map(int,input().strip().split()))[:2]
x=a[0]
y=a[1]
if x==y:
    print(x)
if y>x :
    print("-1")
if y<x and x%y==0 :
    g=x/y
    h=g//2
    i=g%2
    print(int((h+i)*y))
if y<x and x%y!=0:
    g=x//2
    h=g%2
    while (g+h)%y!=0 and g!=0 :
        g=g-2
        h=h+2
    if (g+h)%y==0:
        print(int(g+h))
    else:
        print("-1")
