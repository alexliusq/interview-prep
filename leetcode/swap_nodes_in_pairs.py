
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    dummy_head = tail = ListNode()
    while head and head.next:
        temp = head.next.next
        tail.next = head.next
        tail = tail.next
        tail.next = head
        tail = tail.next
        head = temp
    if head:
        tail.next = head
        tail = tail.next
    tail.next = None
    return dummy_head.next