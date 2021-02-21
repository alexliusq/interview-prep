
from collections import Counter
from linked_list import LinkedList, LinkedListNode


def remove_dups_buffer(l: LinkedList) -> LinkedList:
    count = Counter()
    curr = l.head
    while curr:
        count[curr.value] += 1
        curr = curr.next

    prev = curr = l.head
    while curr:
        if count[curr.value] > 1:
            prev.next = curr.next
        
        prev = curr
        curr = curr.next
    
    print(l)
    return l

def linked_list_sort(l: LinkedList) -> LinkedList:
    if not l.head:
        return l
    
    pivot_node = l.head
    pivot = pivot_node.value
    less_head = less_tail = LinkedListNode(0)
    greater_head = greater_tail = LinkedListNode(0)
    
    curr = l.head.next
    while curr:
        if curr.value < pivot:
            less_tail.next = curr
            less_tail = less_tail.next
        else:
            greater_tail.next = curr
            greater_tail = greater_tail.next
        
        curr = curr.next

    less_list = LinkedList()
    less_list.head = less_head.next
    less_tail.next = None
    less_list = linked_list_sort(less_list)

    greater_list = LinkedList()
    greater_list.head = greater_head.next
    greater_tail.next = None
    greater_list = linked_list_sort(greater_list)
    
    dummy_head = tail = LinkedListNode(0)
    if less_list:
        tail.next = less_list.head
        tail = less_list.tail
    tail.next =  pivot_node
    tail = tail.next
    if greater_list:
        tail.next = greater_list.head
        tail = greater_list.tail
    

    l.head = dummy_head.next
    l.tail = tail
    tail.next = None
    # print(l)
    return l


def remove_dups_sort(l: LinkedList) -> LinkedList:
    
    return

l2 = LinkedList([1,4,3,1,5])
assert linked_list_sort(l2).values() == [1,1,3,4,5]

l1 = LinkedList([1,2,2,3,3,3,4])
assert remove_dups_buffer(l1).values() == [1, 2, 3, 4]
assert remove_dups_sort(l1).values() == [1,2,3,4]