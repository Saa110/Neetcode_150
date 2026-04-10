# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists:[ListpOptional[ListNode]])-> Optional[ListNode]:
        min_heap=[]
        for i,j in enumerate(lists):
            if j:
                heapq.heappush(min_heap,(j.val,i,j))
        dummy=ListNode()
        curr=dummy
        while min_heap:
            val,i,node=heapq.heappop(min_heap)
            curr.next=node
            curr=curr.next
            if node.next:
                node=node.next
                heapq.heappush(min_heap,(node.val,i,node))
        return dummy.next




class Solution_old:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        rtr_node=ListNode()
        head=rtr_node
        while True:
            least=[0,1001]
            flag=1
            for i in range(len(lists)):
                if lists[i] and lists[i].val<least[1]:
                    least=[i,lists[i].val]
                    flag=0
            if flag:
                break
            rtr_node.next=lists[least[0]]
            rtr_node=rtr_node.next
            lists[least[0]]=lists[least[0]].next
        return head.next

                
        
