def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    res = []
    stack = [root]
    count = 0
    while stack:
        level = []
        count += 1
        for i in range(len(stack)):
            cur = stack.pop(0)
            level.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        if level:
            res.append(level)
    return res[::-1]