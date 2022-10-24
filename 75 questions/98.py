# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def valid(root, min, max):
            if not root:
                return True
            if min and root.val <= min.val:
                return False
            if max and root.val >= max.val:
                return False
            return valid(root.left, min, root) and valid(root.right, root, max)
        return valid(root,None,None)
                 