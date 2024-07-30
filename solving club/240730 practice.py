# # Flatten
# test_case = 10
#
# for i in range(test_case):
#     n = int(input())
#     box_lst = list(map(int, input().split()))
#     # n 번동안 반복 작업
#     for _ in range(n):
#         # max = 0
#         # min = 1e9
#         # for j in box_lst:
#         #     if j >= max:
#         #         max = j
#         #     if j < min:
#         #         min = j
#         max_val = max(box_lst)
#         min_val = min(box_lst)
#         for d in range(len(box_lst)):
#             if box_lst[d] == min_val:
#                 box_lst[d] += 1
#                 break
#         for s in range(len(box_lst)):
#             if box_lst[s] == max_val:
#                 box_lst[s] -= 1
#                 break
#
#     # print(min_val,max_val)'
#     # print(f'#{i+1} {max_val-min_val}')
#     real_max = max(box_lst)
#     real_min = min(box_lst)
#     print(f'#{i + 1} {real_max - real_min}')


# Flatten 2
# test_case = 10
#
# for i in range(test_case):
#     n = int(input())
#     box_lst = list(map(int, input().split()))
#     # n 번동안 반복 작업
#     for _ in range(n):
#         max_value = 0
#         min_value = 1e9
#         for j in box_lst:
#             if j >= max_value:
#                 max_value = j
#             if j < min_value:
#                 min_value = j
#
#         for d in range(len(box_lst)):
#             if box_lst[d] == min_value:
#                 box_lst[d] += 1
#                 break
#         for s in range(len(box_lst)):
#             if box_lst[s] == max_value:
#                 box_lst[s] -= 1
#                 break
#
#     # print(min_val,max_val)'
#     # print(f'#{i+1} {max_val-min_val}')
#     real_max = max(box_lst)
#     real_min = min(box_lst)
#     print(f'#{i + 1} {real_max - real_min}')


# # 4834 숫자카드
# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input()))
#     counts = [0] * 10
#     # print(a, n)
#     for x in a:
#         counts[x] += 1
#
#     max_num = 0
#     for s in counts:
#         if s >= max_num:
#             max_num = s
#     # print(counts)
#
#     many_num = []
#
#     for num in range(len(counts)):
#         if counts[num] == max_num:
#             many_num.append(num)
#
#     # print(many_num)
#     real_num = many_num[len(many_num)-1]
#     # print(real_num)
#
#     print(f'#{i+1} {real_num} {counts[real_num]}')

