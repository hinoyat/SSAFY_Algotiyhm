from pprint import pprint
# # 간선 거리
#     # 노드. 스타트, 노드 수
# def BFS(lst, S, V):
#     # 거리 배열, 방문 확인 배열
#     visited = [0] * (V+1)
#     distance = [0] * (V+1)
#     # 큐 생성
#     queue = []
#     # 시작 지점 표시
#     queue.append(S)
#     visited[S] = 1
#     # 결과 확인
#     result = []
#
#     while queue:
#         t = queue.pop(0)
#         result.append(t)
#         # print(result)
#         for i in lst[t]:
#             # 방문하지 않았다면;;
#             if not visited[i]:
#                 # 큐에 넣고 방문 표시 거리는 전의 거리보다 1 높게
#                 queue.append(i)
#                 visited[i] = 1
#                 distance[i] = distance[t] + 1
#         # print(visited)
#     return result, distance
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     G_lst = [[]for _ in range(V+1)]
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         # 출발지와 도착지 왕복
#         G_lst[v1].append(v2)
#         G_lst[v2].append(v1)
#     S, G = map(int, input().split())
#     # print(G_lst)
#     # print(BFS(G_lst, S, V))
#
#     print(f'#{tc} {BFS(G_lst, S, V)[1][G]}')


# # 미로 1
# def BFS(si, sj, L):
#     visited = [[0]*L for _ in range(L)]
#     que = []
#     que.append([si, sj])
#     visited[si][sj] = 1
#     possible = 0
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     while que:
#         qi, qj = que.pop(0)
#         # print(qi, qj)
#         if arr[qi][qj] == 3:
#             possible = 1
#             break
#         else:
#             for d in range(4):
#                 newi = qi + di[d]
#                 newj = qj + dj[d]
#                 if 0 <= newi < L and 0 <= newj < L and arr[newi][newj] != 1 and visited[newi][newj] == 0:
#                     que.append([newi, newj])
#                     visited[newi][newj] = 1
#     return possible
#
# T = 10
# for _ in range(1, T+1):
#     tc = int(input())
#     L = 16
#     arr = [list(map(int, input())) for _ in range(L)]
#     # pprint(arr)
#     S = [0,0]
#     G = [0,0]
#     for i in range(L):
#         for j in range(L):
#             if arr[i][j] == 2:
#                 S = [i, j]
#             if arr[i][j] == 3:
#                 G = [i, j]
#     si = S[0]
#     sj = S[1]
#
#     print(f'#{tc} {BFS(si, sj, L)}')


# 미로의 거리
def BSF(si, sj, N):
    visited = [[0]*N for _ in range(N)]
    que = []
    que.append([si, sj])
    visited[si][sj] = 1

    dist = 0
    while que:
        qi, qj = que.pop(0)
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        if arr[qi][qj] == 3:
            # print(qi, qj)
            dist = visited[qi][qj] - 2
        else:
            for d in range(4):
                newi = qi + di[d]
                newj = qj + dj[d]
                if 0 <= newi < N and 0 <= newj < N and arr[newi][newj] != 1 and visited[newi][newj] == 0:
                    que.append([newi, newj])
                    visited[newi][newj] = visited[qi][qj] + 1
    return dist

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    S = [0,0]
    G = [0,0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                S = [i, j]
            if arr[i][j] == 3:
                G = [i, j]
    si = S[0]
    sj = S[1]
    result = BSF(si, sj, N)
    print(f'#{tc} {result}')