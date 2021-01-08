from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self) -> None:
        self.push_stack = []
        self.pop_stack = []
    ## your method is worst case O(N) because each element gets pushed or popped if
    ## enqueue and dequeue are not sequential
    # def enqueue(self, x: int) -> None:
    #     while self.pop_stack:
    #         self.push_stack.append(self.pop_stack.pop())
    #     self.push_stack.append(x)
    #     return

    # def dequeue(self) -> int:
    #     while self.push_stack:
    #         self.pop_stack.append(self.push_stack.pop())
    #     return self.pop_stack.pop()

    def enqueue(self, x: int) -> None:
        self.push_stack.append(x)
        return

    def dequeue(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
