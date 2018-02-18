# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L,R):
            if L and R and L.val==R.val:
                return isSym(L.right,R.left) and isSym(L.left,R.right)
            return L is R
        return isSym(root,root)
        