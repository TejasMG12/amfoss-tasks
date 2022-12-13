t=int(input())
for i in range (0,t):
    n=int(input())
    if n>0:
        n=n-1
    y=0
    j=n//3
    k=n//5
    m=n//15
    l=(j*(3+j*3))/2
    
    n=(k*(5+k*5))/2
    o=(m*(15+m*15))/2
    print(l+n-o)
