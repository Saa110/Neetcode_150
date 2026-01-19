# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        if c==n:
            if head.next:
                head=head.next
                return head
            else:
                return None
        c=c-n
        temp=head
        for _ in range(c-1):
            temp=temp.next
        temp.next=temp.next.next
        return head


        
