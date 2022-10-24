# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            level = []
            for i in range(len(stack)):
                cur = stack.pop(0)
                level.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            res.append(level)
        return res
                