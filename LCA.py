#
# Traverse the tree starting from root.
# If any of the given keys (n1 and n2) matches with root,
# then root is LCA (assuming that both keys are present).
# If root doesn’t match with any of the keys, we recur for left and right subtree.
# The node which has one key present in its left subtree and the other key present
# in right subtree is the LCA. If both keys lie in left subtree, then left subtree
# has LCA also, otherwise LCA lies in right subtree.



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        lcaleft=self.lowestCommonAncestor(root.left,p,q)
        lcaright=self.lowestCommonAncestor(root.right,p,q)
        if lcaright or lcaleft:
            return root
        if lcaleft != None:
             return lcaleft
        else: 
            return lcaright