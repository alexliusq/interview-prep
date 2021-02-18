from typing import Iterable


class CounterWithGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        curr = self.start
        while curr <= self.end:
            yield curr
            curr += 1
            # print(self.count)

    # def __next__(self):
        

class CounterIterable(Iterable):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    class CounterIterator:
        def __init__(self, source) -> None:
            self.source = source
            self.count = source.start
        
        def __next__(self):
            val = self.count
            self.count += 1
            if val <= self.source.end:
                return val
            else:
                raise StopIteration
    

    def __iter__(self):
        return self.CounterIterator(self)


count10 = CounterIterable(0, 10)
for i in count10:
    print(i)
print('try1: ', list(count10))
print('try2: ', list(count10))