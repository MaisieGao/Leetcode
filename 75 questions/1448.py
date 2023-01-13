    def goodNodes(self, root: TreeNode) -> int:
        def count(node, maxV):
            if not node:
                return 0
            res = 1 if node.val >= maxV else 0
            maxV = max(maxV, node.val)
            res += count(node.left, maxV)
            res += count(node.right, maxV)
            return res

        return count(root,root.val)