# #  피보나치 메모이제이숀
# def fibo(n):
#     global memo
#     if n >= 2 and memo[n] == 0:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]
#
# n = 100
# memo = [0] * (n+1)
# memo[0] = 0
#      memo[1] = 1
#
# print(fibo(100))

# DFS 깊이
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# # 방식 1 인접 리스트
# def dfs(s, V):        # s 시작 정점, V 정점개수 (1번부터인 정점의 마지막 정점)
#     visited = [0] * (V+1) # 방문한 정점을 표시
#     stack = []                      # 스택 생성
#     visited[s] = 1                  # 시작 정점 방문표시
#     print(s)
#     v = s
#     while True:
#         for w in adjl[v]:           # v에 인접하고 방문 안 한 w가 있으면
#             if visited[w] == 0:
#                 stack.append(v)     # push(v) 현재 정점을 push하고
#                 v = w               # w에 방문
#                 print(v)
#                 visited[w] = 1      # w에 방문 표시
#                 break               # for w에 대한 브레이크 v 부터 다시 탐색
#         else:                       # 남은 인접정점이 없어서 break가 걸리지 않은 경우
#             if stack:           # 이전 갈림길을 스택에서 꺼내서 if top > -1
#                 v = stack.pop()
#             else:               # 비어있음 : 되돌아갈 곳이 없으면, 남은 갈림길이 없으면
#                 break           # while True: 한루프에 빠지지 않고 돈다
#
# test_case = 1
# for _ in range(test_case):
#     # V 정점 수 E는 간선
#     V, E = map(int, input().split())
#     adjl = [[] for _ in range(V + 1)]
#     arr = list(map(int, input().split()))
#     for i in range(E):
#         v1, v2 = arr[i*2], arr[i*2+1]
#         #정점이 많지 않아 append
#         adjl[v1].append(v2)
#         adjl[v2].append(v1)
#
#     print(adjl)
#
#     dfs(1, V)


# # 인접행렬 버전
# # 장점 거리를 표현할 수 이써
# graph = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]


# # 인접 리스트
# def dfs(s):
#     stack = []
#     stack.append(s)         # while 문이 돌아가게 하나 넣어줌
#     visited = [False] * (N+1)
#
#     while stack:            # 스택에 데이터가 있는 동안
#         v = stack.pop()     # 마지막 녀석 pop
#         if not visited[v]:
#             print(v)
#             visited[v] = True
#             for w in graph[v]:
#                 stack.append(w)


# visited = [False] * (N + 1)
# def dfs_r(v):
#     print(v)
#     visited[v] = True
#
#     for w in graph[v]:
#         if not visited[w]:
#             dfs_r(w)


#
# N = 7
# graph = [[] for _ in range(N+1)]
# # graph = [0*(N+1) for _ in range(N+1)]
# s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# numbers = list(map(int, s.split()))
# for i in range(0, len(numbers), 2):
#     v1 = numbers[i]
#     v2 = numbers[i+1]
#     graph[v1].append(v2)
#     graph[v2].append(v1)
# print(graph)
# dfs(1)
