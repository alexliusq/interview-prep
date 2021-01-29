from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    def find_min(a, b) -> int:
        # print(a,b)
        if a < 0:
            return b + 1
        if b < 0:
            return a + 1
        if result[a][b] != -1:
            return result[a][b]

        if A[a] == B[b]:
            result[a][b] = find_min(a - 1, b - 1)
            return result[a][b]

        substitute_min = find_min(a - 1, b - 1)
        insertion_min = find_min(a, b - 1)
        deletion_min = find_min(a - 1, b)
        new_min = 1 + min(substitute_min, insertion_min, deletion_min)
        result[a][b] = new_min
        return new_min


    result = [[-1] * len(B) for _ in range(len(A))]
    # print(result)
    return find_min(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
