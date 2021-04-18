a,n=map(int,input().split())
s=[]
r=[]
for __ in range(a):
    s.append(input())
for i in range(a):
    s1=int(s[i],2)
    for j in range(i,a):
    	s2=int(s[j],2)
    	b=bin(s1|s2)
    	r.append(b)
 
c=0
n=0

for i in r:
    if i.count('1')>c:
    	c=i.count('1')
for i in r:
    if i.count('1')==c:
        n+=1
print(c)
print(n)
'''''
4 5
10101
11100
11010
00101
o/p:
5
2
Calculating topics known for all permutations of 2 attendees we get:
(1,2) -> 4
(1,3) -> 5
(1,4) -> 3
(2,3) -> 4
(2,4) -> 4
(3,4) -> 5
The 2 teams (1, 3) and (3, 4) know all 5 topics which is maximal.''''''

