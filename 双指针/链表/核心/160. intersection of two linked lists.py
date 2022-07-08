def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        node1 = headA
        node2 = headB
        #他俩相等的时候开始相交
        while node1 != node2:
            #如果里面不用if用while,那么就变成了O(n^2)了
            if node1 is None:
                #node1这时候已经是none了，所以直接等于headB.不是node1.next = headB
                node1 = headB
            else:
                node1 = node1.next
            if node2 is None:
                node2 = headA
            else:
                node2 = node2.next
        return node1
