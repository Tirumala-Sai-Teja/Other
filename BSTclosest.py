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
    if root is None:
        return closest
    if abs(target-closest)>abs(target-root.value):
        closest=root.value
    if target<root.value:
        return fclosestHelper(root.left,target,closest)
    elif target>root.value:
        return fclosestHelper(root.right,target,closest)
    else:
        return closest
        #this function takes O(log(N)) andO(N) time and space in AVG and WORST
def fclosestHelper(root,target,closest):
    new=root
    while new is not None:
        if abs(target-closest)>abs(target-new.value):
            closest=new.value
        if target<new.value:
            new=new.left
        elif target>new.value:
            new=new.right
        else:
            break
    return closest
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))
def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else: break
    return closest

r=node(10)
insert(r,5)
insert(r,2)
insert(r,1)
insert(r,5)
insert(r,15)
insert(r,13)
insert(r,14)
insert(r,22)
print(findClosestValueInBst(r,11))

