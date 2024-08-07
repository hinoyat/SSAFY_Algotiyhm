# # 방식 1 인접 리스트
# def dfs(V, start, end):        # s 시작 정점, V 정점개수 (1번부터인 정점의 마지막 정점)
#     visited = [0] * (V+1)   # 방문한 정점을 표시
#     stack = []
#     stack.append(start)         # 시작 정점 방문표시
#     # 스택 생성
#     visited[start] = 1
#     while stack:
#         cur = stack.pop()
#         if cur == end:
#             return 1
#         for j in lst[cur]:
#             if not visited[j]:
#                 stack.append(j)
#                 visited[j] = 1
#     return  0
#
#
# test_case = int(input())
# for tc in range(1, test_case+1):
#     # V 정점 수 E는 간선
#     V, E = map(int, input().split())
#     lst = [[] for _ in range(V + 1)]
#
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         lst[v1].append(v2)
#     start, end = map(int, input().split())
#
#     result = dfs(V, start, end)
#
#     print(f'#{tc} {result}')


# # 종이 붙이기
#
# def sl_paper(n):
#     if n == 10:
#         return 1
#     elif n == 20:
#         return 3
#     else:
#         return sl_paper(n-10) + sl_paper(n-20) *2
#
# test_case = int(input())
# for tc in range(1, test_case+1):
#     N = int(input())
#     result = sl_paper(N)
#     print(f'#{tc} {result}')


# # D4 길찾기
# def dfs(V, start, end):        # s 시작 정점, V 정점개수 (1번부터인 정점의 마지막 정점)
#     visited = [0] * (V+1)   # 방문한 정점을 표시
#     stack = []
#     stack.append(start)         # 시작 정점 방문표시
#     # 스택 생성
#     visited[start] = 1
#     while stack:
#         cur = stack.pop()
#         if cur == end:
#             return 1
#         for j in lst[cur]:
#             if not visited[j]:
#                 stack.append(j)
#                 visited[j] = 1
#     return 0
#
#
# test_case = 10
# for _ in range(1, test_case+1):
#     start = 0
#     end = 99
#     tc, len_lst = map(int, input().split())
#     lst = [[] for _ in range(101)]
#     # print(lst)
#
#     in_lst = list(map(int, input().split()))
#     for i in range(len_lst):
#         v1, v2 = in_lst[i*2], in_lst[i*2+1]
#         lst[v1].append(v2)
#
#     # print(lst)
#     result = dfs(100, start, end)
#     print(f'#{tc} {result}')


# 강사임이 푸러주는 길 찾기
# def dfs(S):
#     stack = []
#     stack.append(S)
#     visited = [False] * (V+1)
#     visited[S] = True
#     while stack:
#         v = stack.pop()
#         if v == G:
#             return 1
#         for w in graph[v]:
#             if visited[w] != True:
#                 stack.append(w)
#                 visited[w] = True
#     return 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input())
#     graph = [[] for _ in range(V+1)]
#
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#
#     S, G = map(int,input().split())
#     result = dfs(S)
#     print(result)




# # 백만장자 프로젝트
test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())
    price = list(map(int, input().split()))
    print(price)

