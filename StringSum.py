s=input()
n=int(input())
length=len(s)
f=0
if int(s)==n:
    print(0)
elif int(s)<n:
    print('not possible')
else:
    for i in range(length):
        c=0
        for j in range(i+1,length):
            s2=s[:j]
            s3=s[j:]
            s1=s2+'+'+s3
            c=1
            #print(s1)
            if eval(s1)==n:
                #print(eval(s1))
                print(c)
                f=1
                break
            elif eval(s1)<n:
                break
            
            else:
                c+=1
                for k in range(len(s[j:])-1):
                    
                    s1=s2+'+'+s3[:k+1]+'+'+s3[k+1:]
                    #print(s1)
                    if eval(s1)==n:
                        print(c)
                        f=1
                        break
                    elif eval(s1)<n:
                        break
               
            if f==1:
                break
            
        if f==1:
            break
                    
                    
            
