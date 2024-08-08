
# # 백트래킹 - 미로찾기
# test_case = int(input())
#
# for tc in range(1, test_case + 1):
#     N = int(input())
#     maze = [[list(map(int, input()))]for _ in range(N)]



# 계산기
def step1(s):
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = ''
    # result = []
    for c in s:
        if c.isdigit():
            result += c
        # elif c == '(':
        #     stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            if stack and isp[stack[-1]] >= icp[c]:
                result += stack.pop()
            stack.append(c)

    while stack:
        result += stack.pop()

    return result

s = '(6+5*(2-8)/2)'
post_order = step1(s)
print(post_order)

# def cal(val1, val2, op):
#     if op == '+':
#         return val2 + val1
#     if op == '-':
#         return val2 - val1
#     if op == '*':
#         return val2 * val1
#     if op == '/':
#         return val2 / val1
#
#
#
# def step2(s):
#     stack = []
#     for c in s:
#         if c.isdigit():
#             stack.append(int(c))
#         else:
#         val1 = stack.pop()
#         val2 = stack.pop()
#         temp = cal(val1, val2, c)
#         stack.append(temp)
#     return stack.pop()