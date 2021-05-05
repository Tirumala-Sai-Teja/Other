dp={999999999:'not possible'}
def reduction(s,n,r='0',f=0):
    ind=0
    for j in range(1,length+1):        
        s2=s[:j]
        s3=s[j:]
        
        if len(s3)<1 :
            s1=s2[0]
            for i in range(1,len(s2)):
                s1+='+'+s2[i]
        else:
            s1=s2+'+'+s3
        s1=r+'+'+s1
        #print(s1)
        if eval(s1)==n:            
            #print(s1.count('+'))
            f=1
            dp[s1.count('+')]=s1
            break      
        elif eval(s1)>n and len(s3)>1 and f==0:
            reduction(s3,n,r+'+'+s2)
s=input()
n=int(input())
length=len(s)

if int(s)==n:
    print(0)
elif int(s)<n:
    print('not possible')
else:
    reduction(s,n)
    if len(dp)==1:
        print('not possible')
    else:
        print(min(dp.keys())-1)
'''
sample input: '111' and num=3
output=2(no of pluses to be inserted)
1162,19
o/p:2
1+16+2 or 11+6+2'''
        
            
                
                    
                    
            
