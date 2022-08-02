def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    #因为是要得到height,所以return的都是height
    def height(root):
        if not root:
            return True
        left=height(root.left)
        right = height(root.right)
        #如果是平衡二叉树，我们就得到高度
        if left >= 0 and right >= 0 and abs(left-right) <= 1:
            return max(left, right) + 1
        else:
            return -1
    return height(root) >= 0