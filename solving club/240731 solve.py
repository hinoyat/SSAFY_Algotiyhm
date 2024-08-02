from pprint import pprint

# # 1209 sum [2일차]
# # print(len(arr))
#
# # 테스트 케이스
# test_case = 10
#
# for tc in range(test_case):
#     case_num = int(input())
#     arr = [[0 for _ in range(100)] for _ in range(100)]
#     max_val = -21e8
#     arr_range = len(arr)
#
#     for hang in range(arr_range):
#         in_arr = list(map(int,input().split()))
#         for yeol in range(len(in_arr)):
#             arr[hang][yeol] = in_arr[yeol]
#
# # 행 합의 최댓값
#     for i in range(arr_range):
#         val = 0
#         for j in range(arr_range):
#             val += arr[i][j]
#         if val >= max_val:
#             max_val = val
#
#
# # 열 합의 최댓값
#     for i in range(arr_range):
#         val = 0
#         for j in range(arr_range):
#             val += arr[j][i]
#         if val >= max_val:
#             max_val = val
# # \ 대각선
#     val = 0
#     for s in range(arr_range):
#         # 원래 val = 0이 여기 있어서 이 for 문은 s가 들어와야 정상 작동이 되는데 왜냐?
#         # 킹각선이기 때문이다 그래서 이 for 문 안에서 초기화 하는 것이 아닌 for 문을 들어오기 전에 초기화를 시켜줘야 정상작동
#         for d in range(arr_range):
#             if s == d:
#                 val += arr[s][d]
#     if val >= max_val:
#         max_val = val
#     val = 0
# # / 대각선
#     for s in range(arr_range):
#         for d in range(arr_range):
#             if (arr_range -1- s) == d:
#                 val += arr[s][d]
#     if val >= max_val:
#         max_val = val
#
#     print(f'#{case_num} {max_val}')
# # 코드 리뷰 일단 하나 하나 나눠서 킹모리 소모가 많다 그리고 for문 과 초기화 시킬 변수에 대한
# # 기본기가 부족해서 항상 뇌로 시뮬레이션 하면서 생각해보자


# # 4836 색칠하기
# # color = [2, 2, 4, 4, color(1) = red (2) = blue]
# #         [0, 1, 2, 3, 4]
# test_case = int(input())
# for tc in range(1,test_case+1):
#     arr = [[[] for _ in range(10)]for _ in range(10)]
#     # print(len(arr))
#     painting = int(input())
#     for _ in range(painting):
#         color = list(map(int , input().split()))
#         # print(color)
#         for i in range(color[0],color[2]+1):
#             for j in range(color[1], color[3]+1):
#                 arr[i][j].append(color[4])
#     # print(arr)
#     result = 0
#     for s in range(len(arr)):
#         for d in range(len(arr)):
#             if 1 in arr[s][d] and 2 in arr[s][d] :
#                 result += 1
#     print(f'#{tc} {result}')


# # 수미님
# for _ in range(10):
#     test_case = int(input())
#     lst = [list(map(int, input().split())) for _ in range(100)]
#     max_sum = 0
#
#     for x in range(100):
#         num = sum(lst[x])
#         if num >= max_sum:
#             max_sum = num
#     for x in range(100):
#         num = 0
#         for y in range(100):
#             num += lst[y][x]
#
#         if num >= max_sum:
#             max_sum = num
#
#     num = 0
#     for i in range(100):
#         num += lst[i][i]
#     if num >= max_sum:
#         max_sum = num
#
#     num = 0
#     for i in range(100):
#         num += lst[i][len(lst)-1-i]
#
#     if num >= max_sum:
#         max_sum = num
#
#     print(f'#{test_case}', max_sum)


# # 4837 부분집합의 합
# test_case = int(input())
#
# lst_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# N = len(lst_A)
#
# sum_lst = []
#
#
# for tc in range(1,test_case+1):
#     n, k = map(int, input().split())
#     cnt = 0
#
#     for i in range(2**N):
#
#         sum_V = 0
#         lst = []
#         for j in range(N):
#
#             if i & (1 << j):
#
#                 sum_V += lst_A[j]
#                 lst.append(lst_A[j])
#
#         if len(lst) == n:
#             if sum(lst) == k:
#                 cnt += 1
#         # 이 라인에서 숫자 세주자
#         # cnt += 1
#     #     print()
#     # print()
#
#     print(f'#{tc} {cnt}')




# # 2001 파리 퇴치

# test_case = int(input())
# for tc in range(1, test_case +1):
#     n, m = map(int, input().split())
#     lst = [[0 for _ in range(n)]for _ in range(n)]


#     for ar1 in range(n):
#         arr = list(map(int,input().split()))
#         for ar2 in range(n):
#             lst[ar1][ar2] = arr[ar2]

#     kill_max = -21e8
#     for i in range(0, n-m+1):
#         for j in range(0, n-m+1):
#             sum_kill = 0

#             for s in range(m):
#                 for d in range(m):
#                     sum_kill += lst[s+i][d+j]

#             if sum_kill >= kill_max:
#                 kill_max = sum_kill
#     print(f'#{tc} {kill_max}')


# # 1979 어디에 단어가 들어갈 수 있을까  ####################
# # from pprint import pprint
# test_case = int(input())
# for tc in range(1, test_case+1):
#     # n은 배열 크기, k는 단어의 길이
#     n, k = map(int, input().split())

#     lst = [[0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(n):
#         new_lst = list(map(int,input().split()))
#         for j in range(n):
#             lst[i][j] = new_lst[j]
#     # pprint(lst)
#     cnt = 0
#     # 행
#     for s in range(n):
#         val = 0
#         for d in range(n):
#             if lst[s][d] == 1:
#                 val += 1
#                 if d == n-1:
#                     if val == k:
#                         cnt += 1
#                         val = 0
#                     else:
#                         pass
#             else:
#                 if val == k:
#                     cnt +=1
#                     val = 0
#                 else:
#                     val = 0
    
#     # 열
#     for s in range(n):
#         val = 0
#         for d in range(n):
#             if lst[d][s] == 1:
#                 val += 1
#                 if d == n-1:
#                     if val == k:
#                         cnt += 1
#                         val = 0
#                     else:
#                         pass
#             else:
#                 if val == k:
#                     cnt +=1
#                     val = 0
#                 else:
#                     val = 0    

#     print(f'#{tc} {cnt}')


# # 스도쿠 검증

# test_case = int(input())
# for tc in range(1, test_case+1):
#     sudoku = [[0 for _ in range(9)] for _ in range(9)]
#     N = len(sudoku)
#     for i in range(N):
#         sudoku_num = list(map(int,input().split()))
#         for j in range(N):
#             sudoku[i][j] = sudoku_num[j]
#     # 행 검증 행의 합이 45면 정상
#     check_lst = []
#     hang_val = 0
#     for hang in sudoku:
#         for s in hang:
#             hang_val += s
#         check_lst.append(hang_val)    
#         hang_val = 0
#     #  합 45 정상
#     # print(f'# {check_lst}')

#     yeol_val = 0
#     for i in range(N):
#         for j in range(N):
#             yeol_val += sudoku[j][i]
#         check_lst.append(yeol_val)    
#         yeol_val = 0
#     # print(f'# {check_lst}')
    
#     # 3X3 합이 45여야 정상
#     for i in range(0,N,3):
#         box_val = 0
#         for s in range(0,N,3):
#             box_val += sudoku[i][s]
#             box_val += sudoku[i][s+1]
#             box_val += sudoku[i][s+2]
#             box_val += sudoku[i+1][s]
#             box_val += sudoku[i+1][s+1]
#             box_val += sudoku[i+1][s+2]
#             box_val += sudoku[i+2][s]
#             box_val += sudoku[i+2][s+1]
#             box_val += sudoku[i+2][s+2]
#             check_lst.append(box_val)
#             box_val = 0

#     sudoku_pos = True

#     for val in check_lst:
#         if val != 45:
#             sudoku_pos = False
#             print(f'#{tc} 0')
#             break
#     if sudoku_pos == True:
#         print(f'#{tc} 1')

# # 스도쿠 검증 이거 전체가 5인 경우도 맞았다고 할 수 있어

# test_case = int(input())
# for tc in range(1, test_case+1):
#     sudoku = [[0 for _ in range(9)] for _ in range(9)]
#     N = len(sudoku)
#     for i in range(N):
#         sudoku_num = list(map(int,input().split()))
#         for j in range(N):
#             sudoku[i][j] = sudoku_num[j]
#     # 행 검증 행의 합이 45면 정상
#     check_lst = []
#     hang_val = 0
#     for hang in sudoku:
#         for s in hang:
#             hang_val += s
#         check_lst.append(hang_val)
#         hang_val = 0
#     #  합 45 정상
#     # print(f'# {check_lst}')

#     yeol_val = 0
#     for i in range(N):
#         for j in range(N):
#             yeol_val += sudoku[j][i]
#         check_lst.append(yeol_val)
#         yeol_val = 0
    
#     # 3X3 합이 45여야 정상
#     for i in range(0,N,3):
#         box_val = 0
#         for s in range(0,N,3):
#             box_val += sum(sudoku[i][s:s+3])
#             box_val += sum(sudoku[i+1][s:s+3])
#             box_val += sum(sudoku[i+2][s:s+3])

#             check_lst.append(box_val)
#             box_val = 0
#     # print(f'# {check_lst}')

#     sudoku_pos = True

#     for val in check_lst:
#         if val != 45:
#             sudoku_pos = False
#             print(f'#{tc} 0')
#             break
#     if sudoku_pos == True:
#         print(f'#{tc} 1')


# 스도쿠 강사님

test_case = int(input())
for tc in range(1, test_case+1):
    arr = [list(map(int,input().split()))for _ in range(9)]

for col in range(9):
    counts = [0]* 10
    for row in range(9):
        idx = arr[row][col]
        if counts[idx]:
            return 0
        counts[idx] = 1