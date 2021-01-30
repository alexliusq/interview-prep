

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    result = []
    for row in range(numRows):
        if row == 0 or row == numRows - 1:
            i = row
            while i < len(s):
                result.append(s[i])
                i += (numRows - 1) * 2
        else:
            i = row
            down = True
            while i < len(s):
                result.append(s[i])
                if down:
                    i += (numRows - 1 - row) * 2
                    down = False
                else:
                    i += row * 2
                    down = True

    return ''.join(result)


if __name__ == '__main__':
    test3 = convert('PAYPALISHIRING', 3)
    print(test3, test3 == 'PAHNAPLSIIGYIR' )
    print(convert('a', 1))