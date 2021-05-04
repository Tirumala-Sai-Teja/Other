def car(c1,c2,sp1=20,sp2=20,cr=3):
    speed1=(18/sp1)*60+c1*cr
    speed2=(20/sp2)*60+c2*cr
    if speed1<speed2:
        return [speed1,1]
    else:
        return [speed2,2]
def tuktuk(c1,c2,sp1=12,sp2=12,cr=1):
    speed1=(18/sp1)*60+c1*cr
    speed2=(20/sp2)*60+c2*cr
    if speed1<speed2:
        return [speed1,1]
    else:
        return [speed2,2]
def bike(c1,c2,sp1=10,sp2=10,cr=2):
    speed1=(18/sp1)*60+c1*cr
    speed2=(20/sp2)*60+c2*cr
    if speed1<speed2:
        return [speed1,1]
    else:
        return [speed2,2]
def minspeed(s1,s2,s3):
    if s1==s2 and s2==s3:
        return 'BIKE'
    elif s1<=s2:
        if s1<s3:
            return 'CAR'
        else:
            return 'BIKE'
    elif s2<=s3:
        if s2==s3:
            return 'BIKE'
        if s2<s3:
            return 'TUKTUK'
    else:
        return 'BIKE'
        
s=input()
l=s.split()

if l[0]=='SUNNY':
    c1=22
    c2=11
    s1=car(c1,c2,min(20,int(l[1])),min(20,int(l[2])))
    s2=tuktuk(c1,c2,min(12,int(l[1])),min(12,int(l[2])))
    s3=bike(c1,c2,min(10,int(l[1])),min(10,int(l[2])))
    r=minspeed(s1[0],s2[0],s3[0])
    if r=='BIKE':
        print(r+' ORBIT'+str(s3[1]))
    if r=='CAR':
        print(r+' ORBIT'+str(s1[1]))
    if r=='TUKTUK':
         print(r+' ORBIT'+str(s2[1]))
elif l[0]=='RAINY':
    c1,c2=24,12
    s1=car(c1,c2,min(20,int(l[1])),min(20,int(l[2])))
    s2=tuktuk(c1,c2,min(12,int(l[1])),min(12,int(l[2])))
    if s1[0]<s2[0]:
        print('CAR ORBIT'+str(s1[1]))
    else:
        print('TUKTUK ORBIT'+str(s1[1]))
else:
    c1,c2=20,10
    s1=car(c1,c2,min(20,int(l[1])),min(20,int(l[2])))
    s2=bike(c1,c2,min(10,int(l[1])),min(10,int(l[2])))
    if s1[0]<s2[0]:
        print('CAR ORBIT'+str(s1[1]))
    else:
        print('BIKE ORBIT'+str(s1[1]))
'''''
sample input and output:
RAINY 40 25
o/p:
CAR ORBIT2
iput2:SUNNY 12 10
O/P:TUKY=TUK ORBIT1
INPUT:WINDY 14 20
O/P:CAR ORBIT2''''
