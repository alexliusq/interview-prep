from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start == finish:
        return L
    if L is None:
        return L
    head = current = ListNode(0, L)
    count = 0
    insert_reverse = ListNode()
    reverse_head = ListNode()
    while count < finish and current.next:
        if count == start - 1:
            insert_reverse = current
            # print('insert reverse start', insert_reverse)
            # print('insert reverse start id', id(insert_reverse))
        current = current.next
        count += 1
    if count != finish:
        return L
    remainder = current.next
    current.next = None
    reverse_head.next = reverse_tail = current
    # print('reverse head', reverse_head)
    # print('reverse head id', id(reverse_head))
    # print('yolo')
    last_reverse = insert_reverse.next
    # print('insert reverse ', insert_reverse)
    # print('insert reverse id', id(insert_reverse))
    # print('reverse_tail ', reverse_tail)
    while last_reverse != reverse_tail:
        # print('reverse_head', reverse_head)
        next_reverse = last_reverse
        while next_reverse.next != reverse_tail:
            # print('inner next reverse', next_reverse)
            # print('inner reverse_tail', reverse_tail)
            next_reverse = next_reverse.next
            # print('inner next reverse 2: ', next_reverse)
        # print('exited')
        reverse_tail.next = next_reverse
        reverse_tail = reverse_tail.next
        reverse_tail.next = None
        # print('hello?')
        # print('end last_reverse', last_reverse)
        # print('end reverse_tail', reverse_tail)
    insert_reverse.next = reverse_head.next
    reverse_tail.next = remainder
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
