# def is_balanced(ip_str):
#     opening_brackets = ['(', '{', '[']
#     closing_brackets = [')', '}', ']']
#     brackets_stack = list()
#     #print(brackets_stack)
#
#     for char in ip_str:
#         if char in opening_brackets:
#             brackets_stack.append(char)
#             #print(brackets_stack)
#         else:
#             #stack_len = len(brackets_stack)
#             if not brackets_stack:
#                 print('Stack is empty and found a closing brakcet')
#                 break
#             curr_bracket = brackets_stack.pop()
#             print(curr_bracket)
#             if curr_bracket == '(':
#                 if char != ')':
#                     print('Unbalanced')
#                     break
#             elif curr_bracket == '{':
#                 if char != '}':
#                     print('Unbalanced')
#                     break
#             elif curr_bracket == '[':
#                 if char != ']':
#                     print('Unbalanced')
#                     break
#
#     if brackets_stack:
#         print('Unbalanced')
#     else:
#         print('Balanced')
#    # print(brackets_stack)
#
# brac_list = "{()}}"
#
# is_balanced(brac_list)