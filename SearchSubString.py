s='banana'
p='ana'
i=len(p)
j=0
c=0
while i<=len(s):
    s1=s[j:i]
    if s1==p:
        c+=1
    j+=1
    i+=1
print(c)
'''''
output:
2'''''
