#recurrence
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case当链表为空或只有head的时候，反转结果就是自己
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        # 经过递归调用之后，可以认为self.reverseList()返回了head节点后面【节点】反转的结果
        # 即1-> 【2 <-3 <-4 <-5】
        # 注意，这里2还指向Null
        # 因此下一步需要让2指向1，即head.next（表示2）.next = head
        # 让head.next的节点指向head
        head.next.next = head
        # 让head节点指向None
        head.next = None
        return last

#iteration
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #刚开始指好了
        dummy = None
        pre = dummy
        cur = head
        #进入循环
        while cur:
            #先标记temp,省的cur变位找不到temp
            temp = cur.next
            #从cur指向pre
            cur.next = pre
            #移动两个点，cur和pre
            #先移动pre不然后面cur移动之后pre就不是移一个了，移动pre到cur的位置
            pre = cur
            #移动cur到temp的位置
            cur = temp
        #cur是Null的时候，pre是末尾的Node
        return pre