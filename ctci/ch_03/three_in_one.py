
import unittest

class Stack:
    def __init__(self, start_index, max_size, three_stack):
        self.top = start_index
        self.max_size = max_size
        self.size = 0
        self.three_stack = three_stack
    
    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.size == self.max_size:
            raise StackFullError

        if not self.is_empty():
            self.top += 1

        self.three_stack.data[self.top] = value
        self.size += 1
        return
    
    def pop(self):
        if self.is_empty():
            raise StackEmptyError
        
        value = self.three_stack.data[self.top]
        self.top -= 1
        self.size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise StackEmptyError
            
        return self.three_stack.data[self.top]

class MultiStackError(Exception):
    """multistack operation error"""

class StackFullError(MultiStackError):
    """the stack is full"""

class StackEmptyError(MultiStackError):
    """the stack is empty"""


class ThreeStack:

    def __init__(self, stack_size):
        self.data = [0 for _ in range(stack_size * 3)]
        self.stacks = tuple(Stack(i * stack_size, stack_size, self) for i in range(3))

class TestMultiStack(unittest.TestCase):
    def test_multistack(self):
        three_stack = ThreeStack(2)
        s1, s2, s3 = three_stack.stacks

        s1.push(1)
        s1.push(2)
        with self.assertRaises(StackFullError):
            s1.push(3)
        self.assertEqual(s1.peek(), 2)
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.pop(), 1)
        with self.assertRaises(StackEmptyError):
            s1.pop()

        s2.push(1)
        s3.push(1)
        self.assertEqual(s2.pop(), 1)
        self.assertEqual(s3.pop(), 1)

unittest.main()
