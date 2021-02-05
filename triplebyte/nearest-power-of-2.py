def nearest_power_of_two(n):
    num_bits = 0
    while n > 0:
        n >>= 1
        num_bits += 1
    return 2 ** (num_bits - 1)

print(nearest_power_of_two(10))
print(nearest_power_of_two(2))
print(nearest_power_of_two(64))