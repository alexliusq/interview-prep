
from __future__ import annotations
from typing import Any, List, Optional

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
    
class LinkedList:

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
        print(result)
        return ' -> '.join(str(i) for i in result)
    
    @classmethod
    def generate_random_list(cls, size: int) -> LinkedList:
        values = [random.randint(0, size) for _ in range(size)]
        return cls(values)

linked_list = LinkedList.generate_random_list(10)
print(linked_list)