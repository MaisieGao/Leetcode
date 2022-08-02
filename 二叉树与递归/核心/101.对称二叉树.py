def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    #要看是否对称，要有两个node，两个node怎么来呢，用root.left and root.right
    def dfs(n1, n2):
        if not n1 and n2:
            return False
        elif not n2 and n1:
            return False
        elif not n2 and not n1:
            return True
        elif n1.val != n2.val:
            return False
        else:
            return dfs(n1.left, n2.right) and dfs(n1.right, n2.left)
    return dfs(root.left, root.right) 