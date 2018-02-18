# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)!=-1
        
    def check(self,root):
        if root is None:
            return 0
        l=self.check(root.left)
        r=self.check(root.right)
        if l==-1 or r==-1 or abs(l-r)>1:
            return -1
        return 1+max(l,r)      