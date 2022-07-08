#链表的partition也是3个pointer:p,q和head
#array是i中间是1, linked list 中间是head
#array比中间小要移到zero+1的位置，然后和i swap, linked list是head加到p的后面
#array比中间大要移到two-1的位置，然后和i swap, linked list是head加到q的后面
#array不需要extra space,但是linked list需要两个新的链表，然后将第二个新建的链表移到第一个后面

def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    p = dummy1 = ListNode(0)
    q = dummy2 = ListNode(0)

    while head:
        if head.val < x:
            p.next = head
            p = p.next
        else:
            q.next = head
            q = q.next
        head = head.next
    q.next = None
    p.next = dummy2.next
    return dummy1.next