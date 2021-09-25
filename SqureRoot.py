'''we can find square root of a number in two ways one is using general for loop and its time complexity is O(n) and 
we can use two pointers concept here whose time complexity is O(logn base2)'''
from math import floor
n=int(input())
l=0
r=n
while(l<=r):
    s=(l+r)/2
    #print(s)
    if round(s*s)==n:
        print(s)
        break
    elif s*s>n:
        r=s
    elif s*s<n:
        l=s
 '''using this program we will get square root of not perfect square numbers also----------O(logn base2)------------ '''
