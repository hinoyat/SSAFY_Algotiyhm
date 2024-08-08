from pprint import pprint
# 파스칼의 삼각형
# test_case = int(input())
# for tc in range(1, test_case+1):
#     N = int(input())
#     arr_len = (N*2)-1
#     arr = [[0 for _ in range(arr_len)]for _ in range(N)]
#     arr[0][(arr_len//2)] = 1
#
#     for i in range(1, N):
#         for j in range(arr_len):
#             if j <= (arr_len//2)+1:
#                 if (j - 2) >= 0 and (j+1) < arr_len:
#                     arr[i][j] = arr[i][j-2] + arr[i-1][j+1]
#                 elif (j-2) < 0:
#                     arr[i][j] = arr[i-1][j+1]
#
#     for i in range(1, N):
#         for j in range(arr_len-1, (arr_len//2), -1):
#             if (j+2) < arr_len:
#                 arr[i][j] = arr[i-1][j-1] + arr[i][j+2]
#             else:
#                 arr[i][j] = arr[i-1][j-1]
#
#
#     print(f'#{tc}')
#     for a in arr:
#         for b in a:
#             if b != 0:
#                 print(b, end=' ')
#         print()

# # 4866 괄호검사
# lst = ['(', ')', '{', '}']
# test_case = int(input())
# for tc in range(1, test_case+1):
#     no_word = []
#     f_word = input()
#     for w in f_word:
#         if w in lst:
#             no_word.append(w)
#     r_word = ''.join(no_word)
#     # print(r_word)
#     check_lst = []
#     possible = 1
#     for w in r_word:
#         if w == '(' or w == '{':
#             check_lst.append(w)
#         elif w == ')':
#             if check_lst and check_lst[-1] == '(':
#                 check_lst.pop()
#             else:
#                 possible = 0
#                 break
#         elif w == '}':
#             if check_lst and check_lst[-1] == '{':
#                 check_lst.pop()
#             else:
#                 possible = 0
#                 break
#
#     if len(check_lst) > 0:
#         possible = 0
#     print(f'#{tc} {possible}')


# # 4873 반복문자 지우기
# test_case = int(input())
# for tc in range(1, test_case+1):
#     word = list(input())
#     check = []
#
#     for i in word:
#         if check:
#             if i == check[-1]:
#                 check.pop()
#             else:
#                 check.append(i)
#         else:
#             check.append(i)
#
#     N = len(check)
#     print(f'#{tc} {N}')


# # 파스칼의 삼각형
# test_case = int(input())
# for tc in range(1, test_case+1):
#     N = int(input())
#     arr_len = (N*2)-1
#     arr = [[0 for _ in range(arr_len)]for _ in range(N)]
#     arr[0][(arr_len//2)] = 1
#
#     for i in range(1, N):
#         for j in range(arr_len):
#             if j-1 >= 0 and j+1 < arr_len:
#                 arr[i][j] += arr[i-1][j-1] + arr[i-1][j+1]
#             if j-1 < 0:
#                 arr[i][j] = arr[i-1][j+1]
#             if j+1 >=arr_len:
#                 arr[i][j] = arr[i-1][j-1]
#
#     print(f'#{tc}')
#     for a in arr:
#         for b in a:
#             if b != 0:
#                 print(b, end=' ')
#         print()


# 로봇
T = int(input())
for tc in range(T):
    input_lst = input().split()


    pos_o = 1
    pos_b = 1

    pre_robot = input_lst[i]

    oposite_time = 0
    total = 0

    for i in range(1, len(input_lst), 2):
        robot = input_lst[i]
        no = input_lst[i+1]

        if robot == 'B':
            pass
        else:
            pass
        if pre_robot == robot:
            pass
        else:
            pass
        pre_robot = robot
