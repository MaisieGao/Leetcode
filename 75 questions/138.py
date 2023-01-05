class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #duplicate the nodes first
        #use a hashmap to make duplicate copies
        #make none connect to none
        oldToCopy = {None : None}
        cur = head
        while cur:
            #create the node of copy
            copy = Node(cur.val)
            #assign the value copy node to key cur node
            oldToCopy[cur] = copy
            cur = cur.next

        #make the connection
        cur = head
        while cur:
            #node correspond
            copy = oldToCopy[cur]
            #next node correspond
            copy.next = oldToCopy[cur.next]
            #random correspond
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        #return the duplicated node
        return oldToCopy[head]

