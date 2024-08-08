# # 백트래킹 - 미로찾기
# test_case = int(input())
#
# for tc in range(1, test_case + 1):
#     N = int(input())
#     maze = [[0 for _ in range(N)]for _ in range(N)]
#     for i in range(N):
#         m = input()
#         for j in range(N):
#             maze[i][j] = int(m[j])
#     print(maze)
#     s_p = []
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 3:
#                 s_p.append(i)
#                 s_p.append(j)
#
#     stack = []
#     print(s_p)
#     possible = True
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     i = s_p[0]
#     j = s_p[1]
#     k = 0
#
#     while True:
#         new_I = i + di[k]
#         new_J = j + dj[k]
#         if 0 <= new_I < N and 0 <= new_J < N and maze[new_I][new_J] != 1 and maze[new_I][new_J] == 0:
#             maze[new_I][new_J] = 1
#             stack.append([new_I][new_J])

# # 백트래킹 - 미로찾기
# test_case = int(input())
#
# for tc in range(1, test_case + 1):
#     N = int(input())
#     maze = [[0 for _ in range(N)]for _ in range(N)]
#     for i in range(N):
#         m = input()
#         for j in range(N):
#             maze[i][j] = int(m[j])
#     print(maze)
#     s_p = []
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 3:
#                 s_p.append(i)
#                 s_p.append(j)
#
#     stack = []
#     print(s_p)
#     possible = True
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     i = s_p[0]
#     j = s_p[1]
#     k = 0
#
#     while True:
#         new_I = i + di[k]
#         new_J = j + dj[k]


# # 계산기 1
# def cal(num1, num2, i):
#     if i == '+':
#         return num2 + num1
#
#
# test_case = 10
# for tc in range(1, test_case + 1):
#     N = int(input())
#     wow = input()
#
#     icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
#     isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
#     stack = []
#     result1 = ''
#     for c in wow:
#         if c.isdigit():
#             result1 += c
#         elif c == '+':
#             if stack and isp[stack[-1]] >= icp[c]:
#                 result1 += stack.pop()
#             stack.append(c)
#     while stack:
#         result1 += stack.pop()
#
#
#     # print(result1)
#
#     stack2 = []
#     result2 = ''
#     for i in result1:
#         if i.isdigit():
#             stack2.append(int(i))
#         else:
#             num1 = stack2.pop()
#             num2 = stack2.pop()
#             result = cal(num1, num2, i)
#             stack2.append(result)
#
#     print(f'#{tc} {stack2.pop()}')




# # forth
# def cal(num1, num2, i):
#     if i == '+':
#         return num2 + num1
#     if i == '-':
#         return num2 - num1
#     if i == '*':
#         return num2 * num1
#     if i == '/':
#         return int(num2 / num1)


# test_case = int(input())
# for tc in range(1, test_case + 1):
#     wow = input().strip().split()
#     stack = []
#     result = ''
#     d_cnt = 0
#     e_cnt = 0
#     for i in wow:
#         if i.isdigit():
#             stack.append(int(i))
#         elif i != '.' and len(stack)>=2:
#             num1 = stack.pop()
#             num2 = stack.pop()
#             result = cal(num1, num2, i)
#             stack.append(result)


#     for i in wow:
#         if i != '.':
#             if i.isdigit():
#                 d_cnt += 1
#             else:
#                 e_cnt += 1

#     print(f'#{tc} {result}')



# # 미로 강사님

# # 3인 곳에 도달할 수 있으면 1 아니면 0 리턴
# def dfs(stR, stC):
#     stack = []
#     visited = [[False] *N for _ in range(N)]
#     stack.append((stR, stC))
#     visited[stR][stC] = True
#     while stack:
#         (vr, vc) = stack.pop()
#         if arr[vr][vc] ==3:
#             return 1
#         for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#             wr = vr + dr
#             wc = vc + dc
#             if 0<= wr < N and 0<=wc<N and arr[wr][wc] != 1:
#                 if not visited[wr][wc]:
#                     stack.append((wr, wc))
#                     visited[wr][wc] = True
#     return 0
#
#
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     arr = [list(map(int, input().strip()))for _ in range(N)]
#
#     # for row in range(N):
#     #     for col in range(N):
#     #         if arr[row][col] == 2:
#     #             stR = row
#     #             stC = col
#
#     for row in range(N):
#         if arr[row].count(2):
#             stR = row
#             stC = arr[row].index(2)
#             break
#
#
#     print(f'#{tc} {dfs(stR, stC)}')




# # # 미로 강사님
# # 재귀
# # v에서 goal(3) 까지 갈 수 있으면 1 없으면 0
#
# def dfs_r(vr, vc):
#     if arr[vr][vc] == 3:
#         return 1
#     visited[vr][vc] = True
#
#     for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#         wr = vr + dr
#         wc = vc + dc
#         # if 0<= wr<N and 0<=wc<N:
#         #     if visited[wr][wc]:
#         #        continue
#         if 0<= wr<N and 0<=wc<N and not visited[wr][wc] and arr[wr][wc]!=1:
#             if visited[wr][wc]:
#                continue
#             if dfs_r(wr, wc)==1:
#                 return 1
#     return 0
#
# # 3인 곳에 도달할 수 있으면 1 아니면 0 리턴
# # def dfs(stR, stC):
# #     stack = []
# #     visited = [[False] *N for _ in range(N)]
# #     stack.append((stR, stC))
# #     visited[stR][stC] = True
# #     while stack:
# #         (vr, vc) = stack.pop()
# #         if arr[vr][vc] ==3:
# #             return 1
# #         for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
# #             wr = vr + dr
# #             wc = vc + dc
# #             if 0<= wr < N and 0<=wc<N and arr[wr][wc] != 1:
# #                 if not visited[wr][wc]:
# #                     stack.append((wr, wc))
# #                     visited[wr][wc] = True
# #     return 0
#
#
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     arr = [list(map(int, input().strip()))for _ in range(N)]
#
#     for row in range(N):
#         if arr[row].count(2):
#             stR = row
#             stC = arr[row].index(2)
#             break
#
#     visited = [[False] * N for _ in range(N)]
#     print(f'#{tc} {dfs_r(stR, stC)}')


# # 로봇
# T = int(input())
# for tc in range(T):
#     input_lst = input().split()


#     pos_o = 1
#     pos_b = 1

#     pre_robot = input_lst[i]

#     oposite_time = 0
#     total = 0

#     for i in range(1, len(input_lst), 2):
#         robot = input_lst[i]
#         no = input_lst[i+1]

#         if robot == 'B':
#             pass
#         else:
#             pass
#         if pre_robot == robot:
#             pass
#         else:
#             pass
#         pre_robot = robot

# 로봇 my ver
T = int(input())
for tc in range(T):
    lst = input().split()
    print(lst)
    B_lst = 0:   
    
    cnt_B = 0
    cnt_O = 0
    i = 1
    while i < len(lst):
        if lst[i] == 'B':
            pass

        
        else:
            pass