from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n <= 1:
        return '1'
    previous = look_and_say(n-1)
    result = []
    count = 1
    i = 0
    while i  < len(previous):
        while i + 1 < len(previous) and previous[i] == previous[i + 1]:
            i += 1
            count += 1
        result.append(f'{count}{previous[i]}')
        count = 1
        i += 1
    return ''.join(result)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
