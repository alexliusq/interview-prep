def bracket_match(bracket_string):
    stack = []
    error_count = 0
    for bracket in bracket_string:
        if bracket == '(':
            stack.append(bracket)
        else: # right bracket
            if stack:
                stack.pop()
            else:
                error_count += 1
    return error_count + len(stack)
        


print(bracket_match('(()())'))
print(bracket_match('((())'))
print(bracket_match('())'))