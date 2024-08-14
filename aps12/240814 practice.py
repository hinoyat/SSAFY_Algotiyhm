# def BFS(G, v, n):
#     visited = [0] * (n+1)
#     queue = []
#     queue.append(v)
#     visited[v] = 1
#     result = []
#
#     distance = [0] * (n+1)
#     distance[v] = 0
#
#     while queue:
#         t = queue.pop(0)
#         result.append(t)
#         # print(result)
#         for i in G[t]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = 1
#                 distance[i] = distance[t] + 1
#         print(visited)
#     return result, distance
#
# lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# G = [[]for _ in range(8)]
# for i in range(len(lst)//2):
#     v1, v2 = lst[i*2], lst[i*2+1]
#     G[v1].append(v2)
# print(G)
# v = 1
# n = 7
# print(BFS(G, v, n))

# 미로
def BFS(i, j, N):
    visited = [[0] * N for _ in range(N)]
    distance = [0] * (N+1)
    que = []
    que.append([i, j])
    visited[i][j] = 1
    while que:
        ti, tj = que.pop(0) # 디큐
        if not maze[ti][tj] == 3:
            return visited[ti][tj] -1 -1 # 경로의 빈칸 수, -1
        for di, dj in[[0, 1], [1, 0], [0, -1], [-1, 0]]: # 미로 내부, 인접 벽
            wi, wj = ti + dj, tj + dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] != 1:
                que.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
sti, stj = find_start(N)
ans = BFS(sti, stj, N)