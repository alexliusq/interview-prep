from test_framework import generic_test


def power(x: float, y: int) -> float:
    result = 1
    next_power = x
    if (y < 0):
        next_power = 1 / x
        y = -y
    while (y):
        if (y & 1):
            result *= next_power
        next_power *= next_power
        y >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
