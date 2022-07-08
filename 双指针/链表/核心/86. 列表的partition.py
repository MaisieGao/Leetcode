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
   def partition(self, head, x):
        #因为这一题不要求区分大于和等于，所以其实是分成了两个区间（小于）（大于或者等于）
        #array 的partition是分成了三个区间[0,zero][i][two,n-1]
        #两个区间在链表看来不能从原链表上换（感觉只有递归可以从原链表上换），所以创建了两个新的链表
        p = dummy1 = ListNode(0)
        q = dummy2 = ListNode(0)
        #相当于array里的 for i in range(n):
        #array中三个指针(zero, i ,two), linked list 三个指针(p, q, head)
        while head:
            if head.val >= x:
                #放到大的区间
                q.next = head
                q = q.next
            else:
                p.next = head
                p = p.next 
            head = head.next
        #把两个新的list连接起来
        q.next = None
        p.next = dummy2.next
        return dummy1.next