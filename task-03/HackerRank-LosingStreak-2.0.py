a=2
A= list(map(int,input().strip().split()))[:a]
n=A[0]
m=A[1]
x=0
y=0
ans1=0
ans2=0
z=m/n
p=m/n
while m%n==0 and z%2==0:
    z=z/2
    ans1 += 1
while m%n==0 and z%3==0:
    z=z/3
    ans2 +=  1

if n > m:
    print("-1")
elif m==n:
    print("0")
elif m>n and z==1 :
    print(int(ans1+ans2))
else:
    print(-1)
