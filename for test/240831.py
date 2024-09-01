### 이진 탐색
# def order(idx, val):
#     global v
#     if idx <= N:
#         order(idx*2, val)
#         tree[idx] = v
#         v += 1
#         order(idx*2+1, val)
# 
# T = int(input().strip())
# for tc in range(1, T+1):
#     N = int(input().strip())
#     tree = [0] * (N+1)
#     idx = 1
#     v = 1
#     order(idx,v)
#     print(f'#{tc} {tree[1]} {tree[N//2]}')


# # 써보트링
# def supernova(find):
#     global ans
#     ans += 1
#     for i in tree[find]:
#         supernova(i)
#
# T = int(input().strip())
# for tc in range(1, T+1):
#     E, N = map(int, input().split())
#     ev = list(map(int, input().split()))
#     tree = [[]for _ in range(max(ev)+1)]
#     for s in range(0, E * 2, 2):
#         P, C = ev[s], ev[s+1]
#         tree[P].append(C)
#
#     ans = 0
#
#     supernova(N)
#
#     print(f'#{tc} {ans}')


#### 중위 머시기
# def supernova(order):
#     global result
#     if order <= N:
#         supernova(order * 2)
#         result += tree[order]
#         supernova(order * 2 + 1)
#
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#
#     tree = [''] * (N+1)
#     for i in range(N):
#         info = input().split()
#         index = int(info[0])
#         value = info[1]
#         tree[index] = value
#
#     result = ''
#
#     supernova(1)
#
#     print(f'#{tc} {result}')


# def supernova(find):
#     if find <= N:
#         if tree[find] != 0:
#             return tree[find]
#         tree[find] = supernova(find*2) + supernova(find*2+1)
#         return tree[find]
#     else:
#         return 0
#
#
# from collections import deque
# def superBFS(start):
#     result = 0
#     queue = deque()
#     queue.append(start)
#     result += tree[start]
#     while queue:
#         q = queue.popleft()
#         l = q * 2
#         r = q * 2 + 1
#         if l <= N:
#             queue.append(l)
#             result += tree[l]
#         if r <= N:
#             queue.append(r)
#             result += tree[r]
#
#     return result
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0] * (N+1)
#
#     for i in range(M):
#         idx, val = map(int, input().split())
#         tree[idx] = val
#     r2 = superBFS(L)
#
#     print(f'#{tc} {r2}')


## 트리 어쩌궁 저쩌구
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     tree = [0] * (N+1)
#
#     idx = 1
#
#     for i in lst:
#         tree[idx] = i
#         r = idx
#         while r > 0 and tree[r] < tree[r//2]:
#             tree[r], tree[r//2] = tree[r//2], tree[r]
#             r//=2
#         idx += 1
#
#     # print(tree)
#     result = 0
#     find = N
#     while find > 0:
#         find //= 2
#         result += tree[find]

    # print(f'#{tc} {result}')
    
    
    
# 사칙한 연산
T = int(input())
for tc in range(1, T+1):