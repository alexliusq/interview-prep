
from __future__ import annotations
from typing import Any, Iterable, Iterator, List, Optional, Generator

import random

class ListNode:
    def __init__(
        self,
        data: Any = None,
        prev: Optional[ListNode] = None, 
        next: Optional[ListNode] = None
    ) -> None:
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return f"{self.data}"
    
    def __lt__(self, other: ListNode):
        return self.data < other.data
    
class LinkedList(Iterable):

    def __init__(self, values: List[Any] = []):
        self.dummy_head = self.tail = ListNode()
        for value in values:
            self.add_node(value)

    def add_node(self, val) -> None:
        node = ListNode(data = val, prev = self.tail)
        self.tail.next = node
        self.tail = self.tail.next

    def __repr__(self) -> str:
        result = []
        node = self.dummy_head.next
        while node:
            result.append(node.data)
            node = node.next
        # print(result)
        return ' -> '.join(str(i) for i in result)

    def __iter__(self) -> Generator[ListNode, None, None]:
        # self.curr = self.dummy_head.next
        # return self
        curr = self.dummy_head.next
        while curr:
            yield curr
            curr = curr.next
    
    # def __next__(self):
    #     if self.curr:
    #         temp = self.curr
    #         self.curr = self.curr.next
    #         return temp
    #     else:
    #         raise StopIteration
    
    def delete_node(self, val) -> None:
        """
        Deletes first instance of node val
        """
        prev = self.dummy_head
        curr = self.dummy_head.next
        while curr and curr.data != val:
            prev = curr
            curr = curr.next
        
        if curr:
            prev.next = curr.next
            if curr.next:
                curr.next.prev = prev

    def __eq__(self, o: LinkedList) -> bool:
        # print(self)
        # print(o)
        for l1, l2 in zip(self, o):
            # print(l1, l2, sep = '\n')
            if l1.data != l2.data:
                return False
        
        return True
    
    @classmethod
    def generate_random_list(cls, size: int) -> LinkedList:
        values = [random.randint(0, size) for _ in range(size)]
        return cls(values)

    @classmethod
    def test_delete(cls):
        l = cls([1,2,3,4])

        l.delete_node(1)
        assert l == cls([2,3,4]), 'failed delete 1'

        l.delete_node(4)
        assert l == cls([2,3]), 'failed delete 4'

        l.delete_node(3)
        assert l== cls([2]), 'failed delete 3'

        l.delete_node(2)
        assert l == cls([]), 'failed delete 2'



linked_list = LinkedList.generate_random_list(10)
LinkedList.test_delete()