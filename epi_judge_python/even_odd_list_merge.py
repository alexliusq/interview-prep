from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    dummy_head = iter = ListNode(0, L)
    number = -1
    even_head = even_tail = ListNode()
    odd_head = odd_tail =  ListNode()
    while iter.next:
        number += 1
        iter = iter.next
        if number % 2 == 0:
            even_tail.next = iter
            even_tail = even_tail.next
        else:
            odd_tail.next = iter
            odd_tail = odd_tail.next
    # either odd or even tail will point to next node. erase
    odd_tail.next = even_tail.next = None
    dummy_head.next = even_head.next
    even_tail.next = odd_head.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
