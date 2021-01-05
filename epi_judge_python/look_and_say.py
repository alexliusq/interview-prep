from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n <= 1:
        return '1'
    previous = look_and_say(n-1)
    result = []
    count = 0
    digit = previous[0]
    for i in range(len(previous)):
        if digit == previous[i]:
            count += 1
        else:
            result.append(f'{count}{digit}')
            count = 1
            digit = previous[i]
    ## append last pair
    result.append(f'{count}{digit}')
    return ''.join(result)
    
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
