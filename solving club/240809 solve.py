# switch = int(input())  # 스위치의 갯수
# switch_lst = [0] + list(map(int, input().split()))  # 1번 인덱스부터 시작하기 위해 앞에 0 추가
# student_num = int(input())  # 학생수
# for _ in range(student_num):  # 학생 수 만큼 입력 값 받음
#     gender, num = map(int, input().split())  # gender: 성별 num: 스위치 위치
#     if gender == 1:  # gender == 1 남학생
#         for idx in range(num, switch + 1, num):  # idx가 cur_pos의 배수만큼
#             if num <= switch:
#                 if switch_lst[idx] == 0:  # 0 ==> 1
#                     switch_lst[idx] = 1
#                 else:
#                     switch_lst[idx] = 0
#     # out of range 발생
#     else:  # gender == 2 여학생
#         switch_lst[num] = 1 - switch_lst[num]
#         i = 1
#         while 0 < num - i and num + i < len(switch_lst) and switch_lst[num - i] == switch_lst[num + i]:  # switch_list 1~끝 리스트까지
#             switch_lst[num - i] = 1 - switch_lst[num - i]
#             switch_lst[num + i] = 1 - switch_lst[num + i]
#             i += 1
#
# # 20개씩 출력
# for i in range(1, len(switch_lst)):
#     if (i - 1) % 20 == 0 and i != 1:
#         print()
#     print(switch_lst[i], end=' ')


# 배열 최소 합



# # 123의 순열 구한다
# def min_v(arr, result):
#
#     min_a = 21e8
#
#     for i in result:
#         sum_a = 0
#         for j in range(len(i)):
#             sum_a += arr[j][i[j]-1]
#         if sum_a < min_a:
#             min_a = sum_a
#     return min_a
#
#
#
# def permutation(k):
#     if k == n :
#         result.append(save_lst.copy())
#         return
#
#     for i in range(n):
#         if visited[i]:continue
#         visited[i] = 1
#         save_lst[k] = idx[i]
#         permutation(k+1)
#         visited[i] = 0
#     else:
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#
#     n = int(input())
#
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     idx = [i for i in range(1, n+1)]
#
#     result = []
#
#
#
#     # 데이터 사용 여분
#     visited = [0] * n
#     # 순열 정보 저장
#     save_lst = [0] * n
#
#     permutation(0)
#     # print(result)
#
#     min_a = 21e8
#
#
#     print(f'#{tc} {min_v(arr, result)}')



# # 순열
# def dfs(T, sumv):
#     global minv
#     if T == n:
#         if sumv < minv:
#             minv = sumv
#
#         # print(result)
#     if sumv >= minv:
#         return
#     else:
#         for i in range(len(idx)):
#             if check_lst[i] == 0:
#                 result[T] = idx[i]
#                 check_lst[i] = 1
#                 sumv += arr[T][idx[T]-1]
#                 dfs(T + 1, sumv)
#                 check_lst[i] = 0
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     n = int(input())
#
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     idx = [i for i in range(1, n+1)]
#
#     result = [0] * len(idx)
#
#     check_lst = [0] * len(idx)
#
#     # max_lst = []
#     # for i in arr:
#     #     for j in range(len(i)):
#     #         if i[j] == max(i):
#     #             max_lst.append(j+1)
#     #             break
#     # print(max_lst)
#     minv = 21e8
#     sumv = 0
#
#     dfs(0, sumv)
#     print(minv)



# # 순열 3
# def permutation(k, sum_a):
#     global min_a
#
#     if sum_a >= min_a:
#         return
#
#
#     if k == n:
#         if min_a > sum_a:
#             min_a = sum_a
#         return
#
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = 1
#             permutation(k + 1, sum_a+arr[k][i])
#             visited[i] = 0
#
#
# T = int(input())
# for tc in range(1, T + 1):
#
#     n = int(input())
#
#     arr = []
#     for _ in range(n):
#         ar = list(map(int, input().split()))
#         arr.append(ar)
#
#     idx = [i for i in range(1, n + 1)]
#
#     result = []
#
#     # 데이터 사용 여분
#     visited = [0] * n
#
#     min_a = 21e8
#     sum_a = 0
#     permutation(0, sum_a)
#
#     print(f'#{tc} {min_a}')


# # 강사님
# def permutation(k):
#     if k == n:
#         sum_v = 0
#         for row in range(n):
#             col = idx[row]
#             sum_v += arr[row][col]
#         return
#
#     for i in range(n):
#         if not visited[i]:
#             idx[k] = i
#             visited[i] = 1
#             permutation(k + 1)
#             visited[i] = 0
#
# T = int(input())
# for tc in range(1, T + 1):
#
#     n = int(input())
#
#     arr = []
#     for _ in range(n):
#         ar = list(map(int, input().split()))
#         arr.append(ar)
#
#     idx = [i for i in range(1, n + 1)]
#
#     result = []
#
#     # 데이터 사용 여분
#     visited = [0] * n
#
#     permutation(0)
#
#     print(f'#{tc} {min_a}')



# 계산기 2
def cal(num1, num2, val):
    if val == '+':
        return num2 + num1
    if val == '-':
        return num2 - num1
    if val == '*':
        return num2 * num1
    if val == '/':
        return int(num2 / num1)

def change(word):
    stack = []
    result = ''
    stack.append(word[0])
    while stack:
        if stack[-1].isdigit():
            result += stack





T = 10
for tc in range(1, T + 1):
    word = list(input())

    stack = []

    result = 0
