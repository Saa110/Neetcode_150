class Node:
    def __init__(self,val: int=0,key: int=None,next: 'Node'=None,back: 'Node'=None):
        self.val=int(val)
        self.key=key
        self.next=next
        self.back=back
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.back=self.head

    def _remove(self,node:'Node'):
        node.next.back=node.back
        node.back.next=node.next
    
    def _addtohead(self, node:'Node'):
        node.next=self.head.next
        node.back=self.head
        self.head.next.back=node
        self.head.next=node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._addtohead(node)
            return node.val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._addtohead(node)
            node.val=value
            return
        else:
            node=Node(value,key)
            self.cache[key]=node
            self._addtohead(node)
        if len(self.cache)>self.capacity:
            lru=self.tail.back
            del self.cache[lru.key]
            self._remove(lru)
            








        
