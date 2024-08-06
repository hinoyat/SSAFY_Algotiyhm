# 스택의 구현
# # push 알고리즘
# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('탈락')
#     else:
#         stack[top] = item
#
#
#
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
# top += 1
# stack[top] = 20
#
# print(stack)

# # pop 알고리즘
# def my_pop():
#     global top
#     if top == -1:
#         print('undweflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top + 1]
# print(pop())
#
# if top > -1:
#     top -=1
#     print(stack[top+1])


# # 스택을 구현해 봅시다
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
#
# stack_size = 10
# stack = [0]*stack_size
# top = -1
# top +=1
# stack[top] = 1
# top +=2
# stack[top] = 2
# top +=3
# stack[top] = 3
#
# top -=1
# print(stack[top+1])
# print(stack[top])
# top -=1
# print(stack[top])
# top -=1
#
# def f2(c,d):
#     return c-d
#
# def f1(a,b):
#     c = a+b
#     d = 10
#     return f2(c, d)
#
# a = 10
# b = 20
# print(f1(a,b))

# def f(i, N):
#     if i == N:
#         return
#     else:
#         print(arr[i]):
#         f(i+1, N)
#         return

# 이론 적인 설명 시험에 나오면 쓰세여
# def push(item) :
#     global top
# 
#     top +=1
#     stack[top] = item
#
# def my_pop():
#     global top
#     result = stack[top]
#     top-=1
#     return result
#
#
# def peek():
#     return stack[top]





# top = -1
# N = 10
# stack = [0] * N
#
# push(1)
# print(top, stack)
#
# push(2)
# print(top, stack)
#
# push(3)
# print(top, stack)
#
# item = my_pop()
# print(top, stack, item)
#
# item = my_pop()
# print(top, stack, item)
#
# item = my_pop()
# print(top, stack, item)
#
# item = my_pop()
# print(top, stack, item)


# def push(item):
#     stack.append(item)
#
# def mypop():
#     return  stack.pop() #pop(-1)
#


# # s의 짝이 맞으면 T 아니면 F
# def isPair(s):
#     stack = []
#     for c in s:
#         if c=='(':
#             stack.append(c)
#         elif c==')':
#             if len(stack)>0:
#                 stack.pop()
#             else:
#                 return False
#     if stack:
#         return False
#     return True
#
# s = '()()((()))'
# print(isPair(s))
# s2 = '())'
# print(isPair(s2))
# s3 = '((())'
# print(isPair(s2))
# s4 = ''
# print(isPair(s2))