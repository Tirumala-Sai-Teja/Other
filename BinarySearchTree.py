class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right= insert(root.right,key)
        else:
            root.left=insert(root.left,key)
        return root
def getht(root):
    if root.right and root.left:
        return 1+max(getht(root.right),getht(root.left))
    elif root.right:
        return 1+getht(root.right)
    elif root.left:
        return 1+getht(root.left)
    else:
        return 1
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
insert(r,30)
insert(r,20)
inorder(r)
h=getht(r)
print('height is ',str(h))
'''''Output:
  20
  30
  50
  height is 3''''''
