def longest_flat(array):
    if not array:
        return 0
    max_flat = current_flat = 1
    prev = array[0]
    for idx in range(1, len(array)):
        if array[idx] == prev:
            current_flat += 1
            if current_flat > max_flat:
                max_flat = current_flat
        else:
            prev = array[idx]
            current_flat = 1
    return max_flat

print(longest_flat([1,1,1]))
print(longest_flat([1,1,2,2,2]))
print(longest_flat([1,1,2,2,2,2]))