import collections
def ascii_deletion_distance(str1, str2):
    chars1 = collections.Counter(str1)
    chars2 = collections.Counter(str2)
    intersection = chars1 & chars2
    union = chars1 | chars2

    return sum(ord(char) * abs(count) for char, count in (union - intersection).items())

    print(chars1 - chars2)
    # return sum([ord(x) for x in deleted_chars])



print(ascii_deletion_distance('at', 'cat'))
print(ascii_deletion_distance('boat', 'got'))
