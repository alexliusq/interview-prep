import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# O(l0) space solution
#
# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
#     l0_nodes = set()
#     head0 = ListNode(0, l0)
#     head1 = ListNode(0, l1)
#     while head0.next:
#         head0 = head0.next
#         l0_nodes.add(id(head0))
#     while head1.next:
#         if id(head1) in l0_nodes:
#             return head1
#         head1 = head1.next
#     return None

## O(c * n), where c is the length of common nodes, n is longest list
## worse case O(n^2)
##
# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
#     head0 = ListNode(0, l0)
#     head1 = ListNode(0, l1)
#     prev0 = next0 = head0
#     prev1 = next1 = head1

#     while next0.next:
#         prev0 = next0
#         next0 = next0.next
    
#     while next1.next:
#         prev1 = next1
#         next1 = next1.next
#     # print('next0', next0)
#     # print('next1', next1)
#     if next0 is not next1:
#         return None
#     # print('searching for common')
#     # print(head0)
#     # print(head1)
#     # print(next0)
#     start_intersection = next0
#     while prev0 is prev1:
#         start_intersection = prev0
#         prev0, prev1 = head0, head1
#         while prev0.next is not start_intersection:
#             prev0 = prev0.next
#         while prev1.next is not start_intersection:
#             prev1 = prev1.next
#     # print(start_intersection)
#     return start_intersection

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    head0 = iter0 = ListNode(0, l0)
    head1 = iter1 = ListNode(0, l1)
    count0 = count1  = 0

    while iter0.next:
        count0 +=1
        iter0 = iter0.next
    
    while iter1.next:
        count1 += 1
        iter1 = iter1.next

    if iter0 is not iter1:
        return None
    # print('searching for common')
    # print(head0)
    # print(head1)
    # print(iter0)
    longer = head0 if count0 >= count1 else head1
    shorter = head0 if count0 < count1 else head1
    for _ in range(abs(count0 - count1)):
        longer = longer.next
    
    while shorter is not longer:
        shorter = shorter.next
        longer = longer.next
    
    return shorter

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))
    # print(common)
    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
