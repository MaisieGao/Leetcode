# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
         def sameTree(node1,node2):
            if node1 and not node2:
                return False
            elif not node1 and node2:
                return False
            elif not node1 and not node2:
                return True
            elif node1.val == node2.val:
                return sameTree(node1.left, node2.left) and sameTree(node1.right,node2.right)
        if not root:
            return False
        elif sameTree(root, subRoot):
            return True
        #从subtree 和sameTree来选择
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)