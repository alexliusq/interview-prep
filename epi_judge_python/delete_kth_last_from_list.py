from typing import List, Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = find_last = prev_k = ListNode(0, L)

    for _ in range(k):
        if find_last.next is None:
            return None
        find_last = find_last.next
    
    while find_last.next:
        find_last = find_last.next
        prev_k = prev_k.next


    if prev_k.next:
        prev_k.next = prev_k.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
