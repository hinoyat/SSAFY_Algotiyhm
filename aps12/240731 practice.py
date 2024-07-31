# # 2차원 배열의 행의 합  열의 합은 반대로
# arr = [[i+(s*5) for i in range(1, 6)] for s in range(5)]
# print(arr)
# max = -21e8
# for d in range(5):
#     val = 0
#     for j in range(5):
#         val += arr[d][j]
#     if val >= max:
#         max = val
# print(max)


# # 2차원 배열의 지그재그 순회
# # 원리를 모르겠네요
# arr = [[i+(s*5) for i in range(1, 6)] for s in range(5)]
# print(arr)
#
# for d in range(5):
#     for j in range(5):
#         print(arr[d][j + (5-1-2*j)*(d % 2)],end=' ')


# # 델타를 이용한 2차 배열 탐색
# # 내가 해보는 것
# arr = [[ar+(ar2*5) for ar in range(1, 6)] for ar2 in range(5)]
# print(arr)
# for i in range(5):
#     for j in range(5):
#         val = 0
#         val += arr[i][j]
#         if j - 1 < 0 :
#             val += 0
#         else:
#             val += arr[i][j - 1]
#         if j + 1 >= 5:
#             val += 0
#         else:
#             val += arr[i][j + 1]
#
#         if i - 1 < 0:
#             val += 0
#         else:
#             val += arr[i - 1][j]
#         if i + 1 >= 5:
#             val += 0
#         else:
#             val += arr[i + 1][j]
#         print(f'#{i} {j} {val}')
#
# # 강의


# # 전치 행렬 대각선을 기준으로 대칭이 되는 위치를 바꿈
#
# arr = [[ar+(ar2*5) for ar in range(1, 6)] for ar2 in range(5)]
# print(arr)
#
# for i in range(5):
#     for j in range(5):
#         # 이 대각선을 기준으로
#         if i < j:
#             arr[i][j], arr[j][i] =  arr[j][i], arr[i][j]
# print(arr)

# # 강사님이 보여주는 것
#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# total = 0
# for i in range(N):
#     for j in range(N): # N X N 배열의 모든 원소에 대해
#         # i, j 원소의 4방향 원소에 대해
#         s = 0   # 문제에서 원소와 인접 원소의 차의 절대값의 합 저장  # 합계 중에 최댓값을 구하는 문제면 s 필요
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 s += abs(arr[i][j] - arr[ni][nj]) # 실존하는 인접 원소 ni, nj, 차의 절대값
#     total +=s
#
# print(total)




# # #부분집합
# # 원소의 개수가 달라졌을 때 쓸 수 있어요
# arr = [3, 6, 7, 1, 5, 4]
#
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=',')
#     print()
# print()


# 강사닙

# row = 1
# col = 3
# command = [ 0, 1, 1, 2, 1]
# # 규칙이 있어야 할 떄
# # dr = [-1, 0, 1, 0]
# # dc = [0, 1, 0, -1]
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
from pprint import pprint

# # 연습문제 1 - 2
# arr = [[i + 1 + (5*s) for i in range(5)]for s in range(5)]
# # pprint(arr)
# # 인텍스가 필요한 경우는 124번 for문처럼 쓰지 말고
# # # 상 우 하 좌
# # dr = [-1, 0, 1, 0]
# # dc = [0, 1, 0, -1]
# # for k in range(5)
# # newR = row - dr[k]
# # newC = col + dc[k]
# N = len(arr)
# total_sum = 0
# for row in range(N):
#     for col in range(N):
#         sumV = 0
#         for (dr, dc) in [(0, 1), (0,-1), (1,0), ((-1,0))]:
#             # row, col 주변의 네개의 방향의 값과 차이를 구한다
#             newR = row + dr
#             newC = col + dc
#
#             if 0 <= newR < N and 0 <= newC < N:
#                 sumV = abs(arr[newR][newC] - arr[row][col])
#         print(row, col, sumV)
#         total_sum += sumV
# print(total_sum)


# # 비트 연산
# # X 값을 알고 싶을 때
# # & 연산자 사용해서 1인지 0인지
# arr = [3, 6, 7, 1, 5, 4]
# N = len(arr)
#
# i = 43
# print(f'{i:06b}, {i}')
# # # i = i & 1
# # # print(f'{i:06b}, {i}')
# # i = i << 1
# # print(f'{i:06b}, {i}')
# # i = i << 1
# # print(f'{i:06b}, {i}')
# for j in range(N):
#     if i & (1 << j) != 0:
#         print(arr[j])
#


# # 4837 부분집합의 합
# lst_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# n = len(lst_A)
# sum_lst = []
# test_case = int(input())
# for tc in range(test_case):
#     for i in range(n << 1 ):
#         sum_N = 0
#         for j in range(n):
#             if i & (1 << j):
#                 print(lst_A[j], end=' ')
#                 sum_N += lst_A[j]
#         print()
#     print()
#     print(sum_N)