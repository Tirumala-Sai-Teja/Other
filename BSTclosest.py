class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def insert(root,val):
    if root is None:
        return node(val)
    else:
        #if val==root.value:
            #return root '''to restrict duplicates in the tree'''
        if val<root.value:
            root.left=insert(root.left,val)
        else:
            root.right=insert(root.right,val)
        return root
def findClosestValueInBst(root,target):
    return fclosestHelper(root,target,float('inf'))

def fclosestHelper(root,target,closest):
    while root is not None:
        new=root.value
        if abs(target-closest)>abs(target-new):
            closest=new
        if target<new:
            root=root.left
        elif target>new:
            root=root.right
        else:
            break
    return closest
r=node(10)
insert(r,5)
insert(r,2)
insert(r,1)
insert(r,5)
insert(r,10)
insert(r,15)
insert(r,13)
insert(r,14)
insert(r,22)
print(findClosestValueInBst(r,11))

