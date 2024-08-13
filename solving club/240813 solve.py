# # 240813 Queue
# T = 10
# for _ in range(T):
#     tc = int(input())
#     pw = list(map(int, input().split()))
#
#     i = 1
#     can = True
#     while can == True:
#         pw[0] -= i
#         n = pw.pop(0)
#         pw.append(n)
#         if pw[7] <= 0:
#             can = False
#         i += 1
#         if i == 6:
#             i = 1
#     pw[7] = 0
#     print(f'#{tc}', end=' ')
#     print(*pw)


# # 5097 회전
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     num = list(map(int, input().split()))
#
#     real = M % N
#     i = 1
#     while i <= real:
#         n = num.pop(0)
#         num.append(n)
#         i += 1
#
#     print(f'#{tc}', end=' ')
#     print(num[0])


# # 5099 피자 굽기
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     piz = list(map(int, input().split()))
#     piz_num = [n for n in range(1, M+1)]
#
#     cnt = 0
#     i = 0
#     while len(piz) > 1:
#
#         if len(piz) > N:
#             if i >= N:
#                 i = 0
#         else:
#             if i >= len(piz):
#                 i = 0
#
#         piz[i] //= 2
#         if piz[i] == 0:
#             piz.pop(i)
#             piz_num.pop(i)
#         else:
#             i += 1
#
#         print(piz)
#         print(piz_num)
#         print(i)
#
#     # print(piz)
#     print(piz_num)

# 피자 2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    piz = list(map(int, input().split()))
    piz_num = [n for n in range(1, M+1)]

    que = [0]*N
    que_idx = [0]*N
    i = 0
    while i < M:

        que[0] //= 2
        if que[0] == 0:
            que[0] = piz[i]
            que_idx[0] = piz_num[i]
            i += 1
        else:
            a = que.pop(0)
            que.append(a)
            b = que_idx.pop(0)
            que_idx.append(b)
        # print(que)
        # print(que_idx)
    i = 0
    while len(que_idx) > 1:
        if i >= len(que):
            i = 0

        que[i] //= 2
        if que[i] == 0:
            que.pop(i)
            que_idx.pop(i)
        else:
            i += 1
    print(f'#{tc}', end=' ')
    print(*que_idx)