# def supernova(si, sj, result):
#     global ans
#     global visited
#
#     if result > ans:
#         return
#
#     if si == N-1 and sj == N-1:
#         if result < ans:
#             ans = result
#         return
#
#     visited[si][sj] = 1
#
#     for di, dj in [[0, 1], [1, 0]]:
#         ni = si + di
#         nj = sj + dj
#         if 0<= ni < N and 0<= nj < N and visited[ni][nj] == 0:
#             supernova(ni, nj, result + arr[ni][nj])
#     visited[si][sj] = 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(arr)
#     ans = 10000
#     visited = [[0]*N for _ in range(N)]
#     supernova(0, 0, arr[0][0])
#     print(ans)
#



# def supernova(idx, result):
#     global ans
#     if result > ans:
#         return
#
#     if 0 not in visited:
#         if result < ans:
#             ans = result
#         return
#     for i in range(len(arr[idx])):
#         if arr[idx][i] != 0 and visited[i] == 0 and visited2[idx] == 0:
#             visited[i] = 1
#             visited2[idx] = 1
#             supernova(i, result +arr[idx][i])
#             visited[i] = 0
#             visited2[idx] = 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     visited2 = [0] * N
#     ans = 10000
#     supernova(0, 0)
#     print(f'#{tc} {ans}')
