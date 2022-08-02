https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/tu-jie-gou-zao-er-cha-shu-jian-dan-yi-do-3kso/
def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    #preorder中左右(先找中的value)
    #inorder左中右(找中的value,然后中-左的size)
    def helper(preorder,inorder):
        if not preorder:
            return None
        target = preorder[0]
        root = TreeNode(target)
        index = inorder.index(target)
        root.left = helper(preorder[1:index+1],inorder[0:index])
        root.right = helper(preorder[index+1:],inorder[index+1:])
        return root
    return helper(preorder,inorder)