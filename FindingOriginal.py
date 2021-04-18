a=[1,2,3,4,1]#product id
b=[3,4,1,4,3]#product weight
c=[6,2,3,2,6]#product price
l=[[a[i],b[i],c[i]]for i in range(5)]#pairing product details
s=set(l)
print(len(l)-set(l))#deleting duplicate and printing the unique product
'''''output:
4''''''
