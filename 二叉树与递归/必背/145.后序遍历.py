def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
    if not root:
        return None
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        #左边入栈，右边先出，变成中，右，左
        #然后res[::-1]翻转成左，右，中
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        
    return res[::-1]