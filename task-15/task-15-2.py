t=int(input())
for i in range (0,t):
    n=int(input())
    list=[1,2]
    y=0
    while list[len(list)-1]<n:
        a=list[len(list)-1]
        b=list[len(list)-2]
        if (a+b)<n:
            list.append(a+b)
            if (a+b)%2==0:
                y=y+a+b
    print(y)

