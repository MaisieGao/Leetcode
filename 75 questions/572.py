# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIndentical(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            return (
                s.val == t.val
                and isIndentical(s.left, t.left)
                and isIndentical(s.right, t.right)
            )

        if not root:
            return False
        if isIndentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)