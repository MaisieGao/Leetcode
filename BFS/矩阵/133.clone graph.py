def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    #hashmap里面有old node: new node
    oldToNew = {}
    def dfs(node):
        #如果node在，说明clone了新的node,直接return new node
        if node in oldToNew:
            return oldToNew[node]
        #没有node,说明没clone,要做一个新的Node = copy
        copy = Node(node.val)
        #放到对应的hashmap的value里
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    #如果没有Node就return none
    if not node:
            return None
    else:
        return dfs(node)