def minDepth(self, root: Optional[TreeNode]) -> int:
    #dfs的loop,用stack.pop(0)相当于queue
    #一层while loop, while 里面是depth
    #一层for loop, 里面是pop这一层所有的node
    #下面如果是bfs,就是stack.append(两边的node)。如果是children,就是for loop
    if not root:
        return 0
    stack = [root]
    depth = 0
    while stack:
        #for loop pop完一层,depth加一层
        depth += 1
        for i in range(len(stack)):
            cur = stack.pop(0)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            #到达left node（离root最近的）就return depth
            if not cur.left and not cur.right:
                return depth