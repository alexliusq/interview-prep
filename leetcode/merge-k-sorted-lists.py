
import heapq
from collections import namedtuple
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    ValueAndNodeIndex = namedtuple('ValueAndNodeIndex', ('value', 'index'))
    
    min_heap = []
    for index, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, ValueAndNodeIndex(node.val, index))

    dummy_head = tail = ListNode()
    while min_heap:
        _, index = heapq.heappop(min_heap)
        node = lists[index]
        tail.next = node
        tail = tail.next
        if tail.next:
            heapq.heappush(min_heap, ValueAndNodeIndex(tail.next.val, index))
            lists[index] = tail.next

    return dummy_head.next

