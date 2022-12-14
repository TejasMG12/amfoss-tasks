#n=the number of points
n=int(input())
p=0
q=0
r=0
s=0
X=[]
Y=[]
ans=0
for i in range (0,n):
    A= list(map(int,input().strip().split()))[:2]
    X.append(A[0])
    Y.append(A[1])
for p in range (0,n):
    lown=0
    upn=0
    rtn=0
    ltn=0
    nt=0
    for q in range (0,n):
        
        if X[p]==X[q] and Y[p]<Y[q]:
            lown+=1
        if X[p]==X[q] and Y[p]>Y[q]:
            upn+=1
        if X[p]>X[q] and Y[p]==Y[q]:
            rtn+=1
        if X[p]<X[q] and Y[p]==Y[q] :
            ltn+=1
    if lown>0:
        nt +=1
    if upn>0:
        nt +=1
    if rtn>0:
        nt +=1
    if ltn>0:
        nt +=1
    if nt>3 and n>4:
        ans = ans + 1
        
    if nt==3 and n==4:
        ans = ans + 1
        
    if nt==2 and n==3:
        ans = ans + 1
        
    if nt==1 and n==2:
        ans = ans + 1
        
            

if n==1:
    ans=ans+1


print(ans)
