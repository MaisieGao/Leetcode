https://leetcode.cn/problems/binary-tree-preorder-traversal/solution/er-by-mavis233-r82p/
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return None
    res = []
    stack = [root]
    #前序，先pop,然后res.append,然后右边入栈，左边入栈
    #中，然后左，然后右
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        #中左右
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)