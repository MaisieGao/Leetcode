# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        if not root:
            return None
        stack = [root]
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res[k-1]

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root,res):
            if not root:
                return None
            traverse(root.left,res)
            res.append(root.val)
            traverse(root.right,res)
            return res
        res = traverse(root,[])
        return res[k-1]