# # 부분집합
# def backtrack(a, k, n):
#     c = [0] * MAXCANDIDATES
#     if k == n:
#         process_solution(a, k)
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k+1, n)
#
# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end='')
#     print()
#
# def construct_candidates(a, k, n, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
#
# MAXCANDIDATES = 2
# NMAX = 4
# a = [0] * NMAX
# num = [1, 2, 3, 4]
# backtrack(a, 0, 4)


# # 순열
# def backtrack(a, k, n):
#     c = [0] * MAXCANDIDATES
#
#     if k == n:
#         for i in range(0, k):
#             print(a[i], end = ' ')
#         print()
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k+1, n)
#
# def construct_candidates(a, k, n, c):
#     in_perm = [False] * (NMAX +1)
#
#     for i in range(k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1, NMAX + 1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
#
# MAXCANDIDATES = 3
# NMAX = 3
# a = [0] * NMAX
# backtrack(a, 0, 3)



# # 부분집합 구하기
# def f(i, K):    # bit[i] 를 결정하는 함수
#     if i == K: # 모든 원소에 대해 결정하면
#         for j in range(K):
#             if bit[j]:    # bit[j] 가 0이 아니면
#                 print(a[j], end = ' ') # 같은 부분집합의 원소는 한 행에
#         print() # 줄 바꾸기
#     else:
#         bit[i] = 1
#         f(i+1, K)
#         bit[i] = 0
#         f(i+1, K)
# 
# N = 3
# a = [1, 2, 3]   # 주어진 원소의 집합
# bit = [0] * N   # 원소의 포함 여부를 표시하는 배열
# 
# f(0, N) # N개의 원소에 대해 부분집합을 만드는 함수


# # 부분집합의 합 구하기
# def f(i, K):    # bit[i] 를 결정하는 함수
#     if i == K: # 모든 원소에 대해 결정하면
#         s = 0
#         for j in range(K):
#             if bit[j]:    # bit[j] 가 0이 아니면
#                 print(a[j], end = ' ') # 같은 부분집합의 원소는 한 행에
#                 s += a[j]       # 누적 합을 구하는 것
#         print(' : ', s) # 줄 바꾸기
#     else:
#         # bit[i] = 1
#         # f(i+1, K)
#         # bit[i] = 0
#         # f(i+1, K)
#         for j in [1, 0]:
#             bit[i] = j
#             f(i+1, K)
# N = 3
# a = [1, 2, 3]   # 주어진 원소의 집합
# bit = [0] * N   # 원소의 포함 여부를 표시하는 배열
#
# f(0, N) # N개의 원소에 대해 부분집합을 만드는 함수






# def f(i, K, s, t):    # i 원소, 집합ㅂ 크기, i-1까지고려된 합, 목표
#     global cnt
#     global fcnt
#     fcnt += 1
#     if s > t:
#         return
#     elif s == t:
#         cnt += 1
#         return
#     elif i == K:
#         return
#
#
#     else:
#         bit[i] = 1
#         f(i+1, K, s+a[i], t)
#         bit[i] = 0
#         f(i+1, K, s, t)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # 주어진 원소의 집합
# N = 10
# bit = [0] * N   # 원소의 포함 여부를 표시하는 배열
#
# key = 10
# cnt = 0     # 합이 key와 같은 부분집합의 수
# fcnt = 0
# f(0,N,0,key)
# print(cnt, fcnt)




# 빨리빨리
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
def powerset(k):
    if k == N:
        print(c)
        return
    else:
        c[k] = 0
        powerset(k+1)
        c[k] = 1
        powerset(k+1)

# 부분집합
c = [-1] * N
powerset(0)