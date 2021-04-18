
d1={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
        'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':-12,'p':-11,'q':-10,'r':-9,'s':-8,
        't':-7,'u':-6,'v':-5,'w':-4,'x':-3,'y':-2,'z':-1}
s=input('enter a string  ')   
c=abs(d1['a']-d1[s[0]])
c=min(c,26-c)
for i in range(len(s)-1):
    d=abs(d1[s[i]]-d1[s[i+1]])
    d=min(d,26-d)
    c+=d
print(c)
'''output:
 swag=22
 cko=14
 clp=15
 baz=3'''


