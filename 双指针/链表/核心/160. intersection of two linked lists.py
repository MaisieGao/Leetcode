def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        node1 = headA
        node2 = headB
        #他俩相等的时候开始相交
        while node1 != node2:
            #如果里面不用if用while,那么就变成了O(n^2)了
            if node1:
                #node1这时候已经是none了，所以直接等于headB.不是node1.next = headB
                node1 = node1.next
                
            else:
                node1 = headB
            if node2:
                node2 = node2.next
            else:
                node2 = headA
        #他俩相等了就return 其中一个 node1 or node2
        #如果有一个没有了，node1 = None,相当于return None
        return node1
