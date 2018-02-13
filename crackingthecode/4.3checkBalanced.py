class Node:
    def __init__(self,key):
        self.left=self
        self.right=self
        self.key=key
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
    def preorder(self,node):
        if node is None:
            return None
        print("Node",node.key)
        self.preorder(node.left)
        self.preorder(node.right)

    def minimalBST(self,arr,start,end):
        if start>end:
            return None
        mid=(start+end)/2
        root=Node(arr[mid])
        root.left=self.minimalBST(arr,start,mid-1)
        root.right=self.minimalBST(arr,mid+1,end)
        return root
    def getHeight(self,root):
        if root is None:
            return -1
        return max(self.getHeight(root.left),self.getHeight(root.right))+1
    def checkBalanced(self,root):
        if root is None:  #Base Case
            return True
        diff=self.getHeight(root.left)-self.getHeight(root.right)
        if abs(diff)>1:
            return True
        else:
            return self.checkBalanced(root.left) and self.checkBalanced(root.right)
        

n=Node(1)
arr=[1,2,3,4,5,6,7]
root=n.minimalBST(arr,0,6)
n.preorder(root)