# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret=[]
        level=[root]
        while root and level:
            currentlevel=[]
            nextlevel=[]
            for node in level:
                currentlevel.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            ret.append(currentlevel)
            level=nextlevel
        return ret