
from __future__ import annotations
from typing import List, NamedTuple


class MinWithCount(NamedTuple):
    value: int
    count: int

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack: List[MinWithCount] = []
    
    def push(self, value):
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(MinWithCount(value, 1))
            return
        
        top = self.min_stack[-1]
        print(top)
        if value < top.value:
            self.min_stack.append(MinWithCount(value, 1))
        elif value == top.value:
            _, count = self.min_stack.pop()
            self.min_stack.append(MinWithCount(value, count + 1))
        
        return
    
    def min(self):
        if not self.min_stack:
            return
        return self.min_stack[-1].value
    
    def pop(self):
        if not self.stack:
            return
        
        popped = self.stack.pop()
        if popped == self.min_stack[-1].value:
            value, count = self.min_stack.pop()
            count -= 1
            if count > 0:
                self.min_stack.append(MinWithCount(value, count))
            
        return popped


min_stack = MinStack()
min_stack.push(10)
min_stack.push(11)
min_stack.push(5)
min_stack.push(5)
assert min_stack.min() == 5
print(min_stack.min_stack)
assert min_stack.pop() == 5
assert min_stack.min() == 5
assert min_stack.pop() == 5
assert min_stack.min() == 10
assert min_stack.pop() == 11
assert min_stack.min() == 10
