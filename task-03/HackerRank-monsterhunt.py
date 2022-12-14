#g= no of groups
g=int(input())
x=int(1)
ans=[]
for x in range (0,g):
    x=x+1
    n=int(input())
    ai= list(map(int,input().strip().split()))[:n]
    while ai[len(ai)-1]==0 and len(ai)>1:
        ai.pop(len(ai)-1)
    while ai[0]==0 and len(ai)>1:
        ai.pop(0)
    la=len(ai)
    ele1=ai[0]
    w=int(0)
    for ele in range (0,la):
        Ele=ai[ele]
        if Ele%ele1!=0:
            ans.append("NO")
            w=1
            break
    if la>=3 :
        for ele in range (1,la-1):
            if ai[ele]==0 :
                ans.append("NO")
                w=1
                break   
    if w!=1:
        ans.append("YES")


for q in ans:
    print(q)
