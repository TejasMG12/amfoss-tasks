t = int(input())
c=0
ans=[]
if t>=1 and t<=10:
    
    for a0 in range(t):
        a=int(input())
        if a>=10 and a<=(10**12):
            ans.append(a)
        else:
            continue
    for k in ans:
        c=k
        ls=[]
        for i in range(2,int(k//2)+1):
                
            if k%i==0:
                ls.append(i)
                    
                for j in ls:
                    for z in range(2,int(j**(1/2))+1):
                        if j%z==0:
                            
                            ls.remove(j)    
                            break           
        ls.reverse()             
        if len(ls)==0:
            print(c)
        else :
            print(ls[0])
