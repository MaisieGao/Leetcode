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
            if not min < root.val < max:
                return False
            return valid(root.left, min, root.val) and valid(root.right, root.val, max)
        return valid(root,float('-inf'),float('inf'))
                 
            
                
            
        