from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: Optional[ListNode]) -> Optional[ListNode]:
    if not L:
        return None
    pivot_head = pivot = L
    smaller_head = smaller =  ListNode()
    larger_head = larger = ListNode()

    next = pivot.next
    while next:
        if next.data < pivot.data:
            smaller.next = next
            smaller = smaller.next
        elif next.data > pivot.data:
            larger.next = next
            larger = larger.next
        else:
            pivot.next = next
            pivot = pivot.next
        next = next.next
    smaller.next = None
    larger.next = None
    pivot.next = None
    smaller_sorted = stable_sort_list(smaller_head.next)
    larger_sorted = stable_sort_list(larger_head.next)
    result_head = result = ListNode()
    if smaller_sorted:
        result.next = smaller_sorted
        while result.next:
            result = result.next
    result.next = pivot_head
    result = pivot
    if larger_sorted:
        result.next = larger_sorted

    return result_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
