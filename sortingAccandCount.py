ls=list(map(int,input().split()))
ls.sort()
p=sorted(ls,key=lambda x:ls.count(x))
print(p)
'''
sample input:
1 2 2 3 4 4 4 5 
sample output:
1 3 5 2 2 4 4 4
