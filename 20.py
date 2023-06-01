# def isValid(s):
#     list = []
#     check_list = []
#     start_parens = ['{', '(', '[']
#     for char in s:
#         list.append(char)
#     for i in range(len(list)):
#         if list[i] in start_parens:
#             check_list.append(list[i])
#         elif check_list[len(check_list)-1] == '(' and list[i] == ')':
#             check_list.pop()
#         elif check_list[len(check_list)-1] == '[' and list[i] == ']':
#             check_list.pop()
#         elif check_list[len(check_list)-1] == '{' and list[i] == '}':
#             check_list.pop()
#     print(check_list)
#     return True if not check_list else False

def isValid(s):
    check_str = ''
    for i in range(len(s)):
        if check_str == '' and (s[i] == '}' or s[i] == ')' or s[i] == ']'):
            return False
        elif s[i] == '{' or s[i] == '(' or s[i] == '[':
            check_str += s[i]
        elif check_str[len(check_str)-1] == '(' and s[i] == ')':
            check_str = check_str[:-1]
        elif check_str[len(check_str)-1] == '[' and s[i] == ']':
            check_str = check_str[:-1]
        elif check_str[len(check_str)-1] == '{' and s[i] == '}':
            check_str = check_str[:-1]
        else: 
            return False
    return True if not check_str else False

print(1, isValid("({({[[[()]]]})})"))
print(2, isValid(")"))
print(3, isValid("("))
print(4, isValid("()"))
print(5, isValid("()[]{}"))
print(6, isValid("(]"))
print(7, isValid("({(})"))
print(8, isValid("[]{}(({}))"))