class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return 
        
        # 1. Count Length
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
            
        # 2. Move to the node BEFORE the split point
        temp = head
        # We want the first half to have floor(length/2) nodes (or +1 for odd)
        # Moving 'steps' times lands us on the last node of the first half
        steps = (length // 2) + (length % 2) - 1 
        
        for _ in range(steps):
            temp = temp.next
            
        # 3. Explicit Cut
        second = temp.next  # Save start of second half
        temp.next = None    # Sever the first half
        
        # 4. Reverse 'second'
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 5. Merge
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
