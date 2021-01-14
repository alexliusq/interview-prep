import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


# def find_max_simultaneous_events(A: List[Event]) -> int:
    # events = collections.deque(sorted(A))
    # levels = []
    # while events:
    #     next_level = []
    #     for event in events:
    #         if not next_level:
    #             next_level.append(event)
    #             continue

    #         if event.start > next_level[-1].finish:
    #             next_level.append(event)

    #     levels.append(next_level)
    #     for event in next_level:
    #         events.remove(event)
    #     # print(events)
    #     # print(len(events))
    # # print('levels')
    # # for level in levels:
    #     # print(level)
    # return len(levels)

def find_max_simultaneous_events(A: List[Event]) -> int:
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

    endpoints = [
        endpoint for event in A 
        for endpoint in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]

    endpoints.sort(key = lambda x: (x.time, not x.is_start))

    max_num_events = 0
    num_events = 0
    for endpoint in endpoints:
        if endpoint.is_start:
            num_events += 1
            max_num_events = max(max_num_events, num_events)
        else: ## endpoint is end
            num_events -= 1

    return max_num_events

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
