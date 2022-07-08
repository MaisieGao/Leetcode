def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #像merge 里的temp
    #不能在同一个链表上更改（array的时候要求在同一array上，所以最后还得还给nums）
    p = dummy = ListNode(0)
    #像mergesort 里的merge part
    #有两个pointer: list1 and list2(array中是i = left, j = mid+1)
    #两个都有值的时候
    while list1 and list2:
        if list1.val < list2.val:
            p.next = list1
            #挪到下一位（array里i+=1）
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        p = p.next
    #list2没有时
    if list1:
        p.next = list1
    #list1没有时
    if list2:
        p.next = list2
    return dummy.next