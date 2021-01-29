
import threading
from typing import OrderedDict

class RW:

    data = 0
    read_count = 0
    read_lock = threading.Condition()
    write_lock = threading.Condition()
    


class Writer(threading.Thread):

    def run(self):
        while True:
            with RW.read_lock


from collections import OrderedDict
a = OrderedDict()
a.

class Reader(threading.Thread):

    def __init__(self):
        super().__init__()
        self.read_count = 0
        self.read_lock = threading.Condition()
        # self.monitor = monitor

    def run(self):
        # with self.monitor:
        #     if self.monitor.status != ReadWriteMonitor.READ_TURN:
        #         self.monitor.wait()
        with self.cv:
            self.read_count += 1

        print('reading')
        
        with self.cv:
            self.read_count -= 1


if __name__ == '__main__':
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = OrderedDict()
        max_length = 0
        for char in s:
            if char in substring:
                popped = ''
                while popped != char:
                    popped = substring.popitem(False)
                
            substring[char] = True
            
            substring_length = len(substring)
            if substring_length > max_length:
                max_length = substring_length
        
        return max_length
