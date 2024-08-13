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
# def cal(num1, num2, val):
#     if val == '+':
#         return num2 + num1
#     if val == '-':
#         return num2 - num1
#     if val == '*':
#         return num2 * num1
#     if val == '/':
#         return int(num2 / num1)

# def change(word):
#     icp = {'+': 1, '-': 1, '*': 2, '/': 2}
#     isp = {'+': 1, '-': 1, '*': 2, '/': 2}
#     stack = []
#     result = ''

#     for c in word:
#         if c.isdigit():
#             result += c
#         else:
#             if stack and isp[stack[-1]] >= icp[c]:
#                 result += stack.pop()
#             stack.append(c)

#     while stack:
#         result += stack.pop()

#     # print(stack)
#     return result

# def change2(word):
#     stack = []
#     result = 0
#     for i in word:
#         if i.isdigit():
#             stack.append(int(i))
#         else:
#             num1 = stack.pop()
#             num2 = stack.pop()
#             result2 = cal(num1, num2, i)
#             stack.append(result2)
#     return stack

# T = 10
# for tc in range(1, T + 1):
#     n = int(input())
#     word = list(input())

#     r = change(word)
#     r2 = change2(r)
#     print(f'#{tc}', end=' ')
#     print(*r2)


# 4880 토너먼트 카드 게임
# def group_game(group):
#     stack = []
#     while len(group) >1:
#         player1 = group.pop()
#         player2 = group.pop()
#         result = rock_scissors_paper(player1, player2)
#         stack.append(result)

#     if len(group) == 1:
#         stack.append(group[0])
#         return stack
#     if len(stack) >1:
#         group_game(stack)

#     return stack

# def who_is_winner(i, j, group):
#     slice_p = i+j//2
#     stack_a = []
#     stack_b = []
#     a = lst[:slice_p]
#     b = lst[slice_p:]
#     if len(a)>1:
#         stack_a.append(group_game(a))
#     else:
#         stack_a.append(a[0])

#     if len(b)>1:
#         stack_b.append(group_game(b))
#     else:
#         stack_b.append(b[0])

#     return stack_a, stack_b

# def who_is_winner(i, j, group):
    # if len(group) % 2 == 0:
    #     slice_p = (i-1)+j//2
    # else:
    #     slice_p = i+j//2
#     stack_a = []
#     stack_b = []
#     a = group[:slice_p]
#     b = group[slice_p:]
#     if len(a)>1:
#         p1 = a.pop(0)
#         p2 = a.pop(0)
#         r_a = rock_scissors_paper(p1, p2)
#         stack_a.append(r_a)
#     else:
#         stack_a.append(a[0])
        
#     if len(b)>1:
#         p1 = b.pop(0)
#         p2 = b.pop(0)
#         r_b = rock_scissors_paper(p1, p2)
#         stack_b.append(r_b)
#     else:
#         stack_b.append(b[0])
    
#     return stack_a, stack_b



# def rock_scissors_paper(a, b):
#     if (a== 1 and b == 3) or (a==2 and b==1) or (a==3 and b == 2) or (a == b):
#         return a
#     else:
#         return b


# T = int(input())
# for tc in range(T):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     r = who_is_winner(1, N, lst)

#     print(r)
    # group_a = []
    # group_b = []
    # if len(lst) % 2 == 0:
    #     group_a = lst[:N//2]
    #     group_b = lst[N//2:]
    # else:
    #     group_a = lst[:N//2+1]
    #     group_b = lst[N//2+1:]

    # print(group_a, group_b)





# # 가위 바위 보 4트

# def who_is_winner(i, j, group):
#     if len(group) % 2 == 0:
#         slice_p = (i-1)+j//2
#     else:
#         slice_p = i+j//2
#     stack = []

#     a = group[:slice_p]
#     b = group[slice_p:]
#     # print(a, b)
#     if len(a)>1:
#         p1 = a.pop(0)
#         p2 = a.pop(0)
#         r_a = rock_scissors_paper(p1, p2)
#         stack.append(r_a)
#     else:
#         stack.append(a[0])
        
#     if len(b)>1:
#         p1 = b.pop(0)
#         p2 = b.pop(0)
#         r_b = rock_scissors_paper(p1, p2)
#         stack.append(r_b)
#     else:
#         stack.append(b[0])
    
#     # who_is_winner(i, len(stack), stack)
#     if len(a)> 1:
#         r_a = who_is_winner(i, len(a), a)
#     if len(b) > 1:
#         r_b = who_is_winner(b, len(b), b)
    
    
#     return stack, a, b

# def rock_scissors_paper(a, b):
#     if (a== 1 and b == 3) or (a==2 and b==1) or (a==3 and b == 2) or (a == b):
#         return a
#     else:
#         return b


# T = int(input())
# for tc in range(T):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     r = who_is_winner(1, N, lst)

#     print(r)



# # 가위 바위 보 5트

# def who_is_winner(i, j, idx):
#     if len(idx) % 2 == 0:
#         slice_p = (i-1)+j//2
#     else:
#         slice_p = i+j//2


#     if len(idx) == 1:
#         return idx[0]
    
#     stack = []
    
#     if len(idx) > 1:
#         a_g = idx[: slice_p]
#         b_g = idx[slice_p:]
#         if len(a_g) > 1:
#             a1 = a_g.pop(0)
#             a2 = a_g.pop(0)
#             a_r = rock_scissors_paper(a1, a2)
#             stack.append(a_r)
#         else:
#             stack.append(a_g[0])

#         if len(b_g) > 1:
#             b1 = b_g.pop(0)
#             b2 = b_g.pop(0)
#             b_r = rock_scissors_paper(b1, b2)
#             stack.append(b_r)
#         else:
#             stack.append(b_g[0])


#     if len(stack) > 1:
#         who_is_winner(i, len(stack), stack)
#     if len(stack) == 1:
#         return stack


# def rock_scissors_paper(a, b):
#     if (a== 1 and b == 3) or (a==2 and b==1) or (a==3 and b == 2) or (a == b):
#         return a
#     else:
#         return b


# T = int(input())
# for tc in range(T):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     idx = [i for i in range(1, N+1)]

#     r = who_is_winner(1, N, lst)
#     print(r)
#     print(idx)



# 러시아
def cal(wb, bc):
    sumV = 0
    for i in range(0, wb): # white로 변경
        sumV += counts[i][1] + counts[i][2]
    for i in range(wb, br+1):
        sumV += counts[i][0] + counts[i][2] # blue 로 변경
    for i in range(br+1, N):
        sumV += counts[i][0] + counts[i][1] # red로 변경
    return sumV
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    counts = [[0,0,0] for _ in range(N)]
    for i in range(N):
        counts[i][0] = arr[i].count('W')
        counts[i][1] = arr[i].count('B')
        counts[i][2] = arr[i].count('R')
    minV = N * M
    # 3개 중에서 2개를 뽑는 조합
    # 재귀를 안 쓰는 이유는 2개만 하면 되니꺼
    for wb in range(1, N - 1): # 블루의 시작점 : 1 | 뒤에 최소 2개는 있어야 한다
        for br in range(wb, N-1):
            val = cal(wb, br)
            if minV > val:
                minV = val
    print(f'#{tc} {minV}')
