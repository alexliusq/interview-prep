from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.storage = [0] * capacity
        self.capacity = capacity
        self.start = 0
        self.end = 0
        self.size_count = 0

    def enqueue(self, x: int) -> None:
        if self.size_count == self.capacity:
            # old_capacity = self.capacity
            # self.capacity = self.capacity * 2
            # new_storage = [0] * self.capacity
            # for i in range(old_capacity):
            #     new_storage[i] = self.storage[(self.start + i) % old_capacity]
            # self.storage = new_storage
            # self.start = 0
            # self.end = old_capacity
            
            ## cleaner approach
            self.storage = [*self.storage[self.start:], *self.storage[:self.start]]
            self.storage = self.storage + ([0] * self.capacity)
            self.start = 0
            self.end = self.capacity
            self.capacity *= 2
        # print(self.storage)
        self.storage[self.end] = x
        self.end = (self.end + 1) % self.capacity
        self.size_count += 1
        return

    def dequeue(self) -> int:
        if not self.size_count:
            raise IndexError('empty queue')
        result = self.storage[self.start]
        self.size_count -= 1
        self.start = (self.start + 1) % self.capacity
        return result

    def size(self) -> int:

        return self.size_count


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
