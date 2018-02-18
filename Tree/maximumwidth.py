# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minimum=[0]
        maximum=[0]
        self.findMinMax(root,minimum,maximum,0)
        a=maximum[0]-minimum[0]
        return a
    def findMinMax(self,node, minimum, maximum, hd):
    
    # Base Case
        if node is None:
            return 
    
    # Update min and max
        if hd < minimum[0] :
            minimum[0] = hd
        elif hd > maximum[0]:
            maximum[0] = hd

    # Recur for left and right subtrees
        self.findMinMax(node.left, minimum, maximum, hd-1)
        self.findMinMax(node.right, minimum, maximum, hd+1)

            