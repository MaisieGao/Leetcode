https://leetcode.cn/problems/validate-binary-search-tree/solution/by-huan-huan-20-zg19/
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #binary search tree最好考虑中序遍历，bst要没有重复的值，左中右依次有小到大
    self.res = []
    def dfs(root):
        if not root:
            return False
        dfs(root.left)
        self.res.append(root.val)
        dfs(root.right)
        return self.res
    tList = dfs(root)
    #newList 是sorted加上去重的，如果newList 和tList 一样，说明tList 代表的tree是bst
    newList = sorted(list(set(tList)))
    if newList == tList:
        return True
    else:
        return False