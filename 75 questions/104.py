# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        level = 0
        while stack:
            level += 1
            for i in range(len(stack)):
                root = stack.pop(0)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
        return level
                    
        