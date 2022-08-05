中序 默认栈中为空，先找到最左的节点，之后每处理一个栈顶元素，访问它的右节点，可以保证左中右的出栈顺序
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #中序遍历
    
    res = []
    #刚开始stack里面什么都没有，因为后面要append root
    stack = []
    if not root:
        return None
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        #可以root是null,这样的话没有root,直接跳到pop那一步
        root = root.right
    return res