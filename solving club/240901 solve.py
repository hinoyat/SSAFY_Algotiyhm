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

# def supernova(idx, sum_v):
#     global min_v
    
#     if 0 not in visited1:
#         if sum_v < min_v:
#             min_v = sum_v
#         return

#     for i in range(len(arr[idx])):
#         if visited1[idx] == 0 and visited2[i] == 0 and arr[idx][i] != 0:
#             visited1[idx] = 1
#             visited2[i] = 1
#             supernova(i, sum_v + arr[idx][i])
#             visited1[idx] = 0
#             visited2[i] = 0
            


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     min_v = 21e8

#     visited1 = [0] * N
#     visited2 = [0] * N

#     supernova(0, 0)
#     print(f'{tc} {min_v}')



# def supernova(ri, rj, result):
#     global min_v
#     if result > min_v:
#         return

#     if ri == N-1 and rj == N-1:
#         if result < min_v:
#             min_v = result
#         return
    
#     for di, dj in [[0, 1], [1, 0]]:
#         ni = ri + di
#         nj = rj + dj
#         if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
#             visited[ni][nj] = 1
#             supernova(ni, nj, result + arr[ni][nj])
#             visited[ni][nj] = 0
    

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     min_v = 21e8

#     visited = [[0]*N for _ in range(N)]

#     supernova(0, 0, arr[0][0])

#     print(f'#{tc} {min_v}')




# def supernova(lst, cnt):
#     global ans
#
#     r = int(''.join(lst))
#     if cnt == S:
#         if r > ans:
#             ans = r
#         return
#
#     for i in range(len(lst)):
#         max_idx = 0
#         for j in range(len(lst)):
#             if lst[i] <= lst[j]:
#                 max_idx = j
#         if max_idx != 0:
#             lst[i], lst[max_idx] = lst[max_idx], lst[i]
#             supernova(lst, cnt + 1)
#             lst[i], lst[max_idx] = lst[max_idx], lst[i]
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, S = map(str, input().split())
#     lst = list(N)
#     S = int(S)//2+1
#     ans = 0
#     supernova(lst, 0)
#     print(f'#{tc} {ans}')


#
# def se(cnt):
#     if cnt == form:
#         print(*result)
#         return
#
#     for i in range(1, 3):
#         result.append(i)
#         se(cnt + 1)
#         result.pop()
#
# result = []
# form = 2
# se(0)



# def supernova(lst, cnt):
#     global ans
#     r = int(''.join(lst))
#     if r == ans:
#          if (cnt + 2) <= S:
#              supernova(lst, cnt + 2)
#
#
#     if cnt == S:
#         if r > ans:
#             ans = r
#         return
#
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if i != j:
#                 if lst[i] != max(lst) and lst[j] != min(lst) and lst[i] < lst[j]:
#                     lst[i], lst[j] = lst[j], lst[i]
#                     supernova(lst, cnt + 1)
#                     lst[i], lst[j] = lst[j], lst[i]
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, S = map(str, input().split())
#     lst = list(N)
#     S = int(S)
#     # print(lst)
#     check = set()
#     ra = ''.join(lst)
#     ans = 0
#     supernova(lst, 0)
#     print(f'#{tc} {ans}')



