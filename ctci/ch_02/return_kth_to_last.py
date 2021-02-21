

from linked_list import LinkedList, LinkedListNode

def kth_to_last(l, k):
    
    fast = slow = l.head
    while fast:
        fast = fast.next
        k -= 1
        if k == 0:
            break

    if k > 0:
        return None

    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow.value




def test_return_kth():
    cases = [
        (([1,2,3,4,5], 2), 4),
        (([1,2,3,4,5], 3), 3),
        (([1], 1), 1)
    ]
    for args, expected in cases:
        l, k = LinkedList(args[0]), args[1]
        assert kth_to_last(l, k) == expected

test_return_kth()