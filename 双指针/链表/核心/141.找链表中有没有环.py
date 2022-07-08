def hasCycle(self, head: Optional[ListNode]) -> bool:
    #确认head是否为空，每次都要确认这个
    #有没有环要用快慢指针
    if not head:
        return head
    fast = head
    slow = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        #不是slow.val == fast.val [1,1,1,1]没有环
        #而是slow == fast(这时候说明两个指针指向的是同一个Node)
        if slow == fast:
            return True
    return False
    #如果要确认环开始的位置，是两个相遇的点，让fast停下，
    # slow回到head,然后两个再相遇的点就是环起点
