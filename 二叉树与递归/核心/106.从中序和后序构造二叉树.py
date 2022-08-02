https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/liang-chong-shi-xian-dong-hua-yan-shi-106-cong-zho/
def buildTree(self, inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    #inorder(左中右)
    #postorder(左右中)
    def dfs(inorder,postorder):
        if not inorder:
            return None
        target = postorder[-1]
        root = TreeNode(target)
        index = inorder.index(target)
        root.left = dfs(inorder[0:index],postorder[0:index])
        root.right = dfs(inorder[index+1:],postorder[index:-1])
        return root
    return dfs(inorder,postorder)