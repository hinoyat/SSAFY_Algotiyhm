# def Run(lst):
#     result = 0
#     idx = 1
#     while idx <= 8:
#         if lst[idx-1] > 0 and lst[idx] > 0 and lst[idx+1] > 0:
#             result += 1
#             lst[idx-1] -= 1
#             lst[idx] -= 1
#             lst[idx+1] -= 1
#             idx = 1
#         idx += 1
#     return result
#
# def triplet(lst):
#     result = 0
#     idx = 0
#
#     while idx <= 9:
#         if lst[idx] >= 3:
#             result += 1
#             lst[idx] -= 3
#             idx = 0
#         idx += 1
#     return result
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     cards = list(map(int, input().split()))
#     ans = '0'
#     p1count = [0] * 10
#     p2count = [0] * 10
#     for i in range(12):
#         if i % 2 == 0:
#             p1count[cards[i]] += 1
#         else:
#             p2count[cards[i]] += 1
#         if i >= 5:
#             p1point = Run(p1count) + triplet(p1count)
#             p2point = Run(p2count) + triplet(p2count)
#             if p1point > p2point:
#                 ans = '1'
#                 break
#             elif p1point < p2point:
#                 ans = '2'
#                 break
#     print(f'#{tc} {ans}')


# T = int(input().strip())
# for tc in range(1, T+1):
#     c, t = map(int, input().split())
#     container = list(map(int, input().split()))
#     truck = list(map(int, input().split()))
#
#     container_visit = [0] * c
#     truck_visit = [0] * t
#
#     ans = 0
#
#     container.sort(reverse=True)
#     truck.sort(reverse=True)
#
#     # print(container)
#     # print(truck)
#
#     cnt = 0
#
#     for i in range(t):
#         for j in range(c):
#             if container_visit[j] == 0 and truck[i] >= container[j]:
#                 ans += container[j]
#                 container_visit[j] = 1
#                 cnt += 1
#                 break
#         if cnt == (max(t, c)):
#             break
#
#     print(f'#{tc} {ans}')



# T = int(input().strip())
# for tc in range(1, T+1):
#     N = int(input())
#     work = []
#     ans = 0
#     for i in range(N):
#         w = list(map(int, input().split()))
#         work.append(w)
#
#     # print(work)
#
#     work.sort(key= lambda x : x[1])
#     # print(work)
#     point = work[0][0]
#     for i in range(N):
#         if work[i][0] >= point:
#             ans += 1
#             point = work[i][1]
#     print(f'#{tc} {ans}')
