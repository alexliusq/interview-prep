
def urlify(s: str) -> str:
    if not s:
        return ''
    result = []
    for char in s.strip():
        if char == ' ':
            if len(result) >= 0 and result[-1] == ' ':
                continue
            else:
                result.append('%20')
        else:
            result.append(char)
    # print(result)
    return ''.join(result)

test_cases = [
    ('a b', 'a%20b'),
    ('   ', ""),
    ('', ''),
    ('hello byee  ', 'hello%20byee')
]

for val, expected in test_cases:
    # print(expected)
    assert urlify(val) == expected, f"FAILED for {val}"