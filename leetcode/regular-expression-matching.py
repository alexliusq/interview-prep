from functools import cache
# import re

# def isMatch(s: str, p: str) -> bool:

#     def checkMatch(s_index, p_index) -> bool:
#         # print(s_index, p_index)
#         while p_index < len(p_list):
#             if '*' in p_list[p_index]:
#                 character = p_list[p_index][0]
#                 has_match = checkMatch(s_index, p_index + 1)
#                 if has_match:
#                     return True
#                 while s_index < len(s) and re.match(character, s[s_index]):
#                     s_index += 1
#                     has_match = checkMatch(s_index, p_index + 1)
#                     if has_match:
#                         return True
#                 return False
#             else:
#                 if s_index >= len(s):
#                     return False
#                 if not re.match(p_list[p_index], s[s_index]):
#                     return False
#                 s_index += 1
#                 p_index += 1
        
#         if s_index == len(s) and p_index == len(p_list):
#             # print('end')
#             return True
#         return False
    
#     p_list = []
#     i = 0
#     while i < len(p):
#         if i + 1 < len(p) and p[i+1] == '*':
#             p_list.append((p[i] + '*'))
#             i += 2
#         else:
#             p_list.append(p[i])
#             i += 1
    
#     # print(p_list)
#     return checkMatch(0,0)

# def isMatch(s: str, p: str) -> bool:
#     if not p:
#         return not s
    
#     first_match = bool(s) and p[0] in (s[0], '.')
#     # print(first_match, s, p)
#     if len(p) >= 2 and p[1] == '*':
#         # print('yolo')
#         return (isMatch(s, p[2:]) or
#             (first_match and isMatch(s[1:], p)))
#     elif first_match:
#         return isMatch(s[1:], p[1:])
#     else:
#         return False
        

def isMatch(s: str, p: str) -> bool:
    @cache
    def indexMatch(s_index, p_index):
        # print(s,p)
        if p_index == len(p):
            return s_index == len(s)

        first_match = s_index < len(s) and p[p_index] in (s[s_index], '.')
        if p_index + 1 < len(p) and p[p_index + 1] == '*':
            return (indexMatch(s_index, p_index + 2) or 
            (first_match and indexMatch(s_index + 1, p_index)))
        elif first_match:
            return indexMatch(s_index + 1, p_index + 1)
        else:
            return False

    return indexMatch(0, 0)

        
if __name__ == "__main__":
    print(isMatch('aa', 'a'))
    print(isMatch('abcd', 'ab*cd*'))
    print(isMatch('a', 'a*'))
    print(isMatch('aaaaaaa', 'a*'))
    print(isMatch('a', 'ab*'))
    print(isMatch('a', 'ab*c*'))
    print(isMatch('asdf', 'as'))