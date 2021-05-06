s=[1,1,2,3,4,4,4,5,2,1]
s.sort()
l=sorted(s,key=lambda x:s.count(x),reverse=True)
print(l)
s='helloitssai'
a='abcdefghijklmnopqrstuvwxyz'
l=sorted(s,key=lambda x:a.index(x))
print(l)
