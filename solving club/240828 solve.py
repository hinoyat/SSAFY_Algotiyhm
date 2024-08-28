# # #이진 힙
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     tree = [0] * (N+1)

#     n = 1
#     for i in lst:
#         tree[n] = i
#         idx = n
#         while idx > 0 and tree[idx] < tree[idx//2]:
#             tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
#             idx//=2
#         n += 1
#     # print(tree)

#     result = 0
#     s_p = N

#     while s_p > 0:
#         s_p//=2
#         result += tree[s_p]
#     print(f'#{tc} {result}')



# # 사칙연산
# def cal(o, num1, num2):
#     if o == '-':
#         return (num1 - num2)
#     if o == '+':
#         return (num1 + num2)
#     if o == '*':
#         return (num1 * num2)
#     if o == '/':
#         return (num1 // num2)


# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0] * (N+1)
#     dct = {}
#     for i in range(N):
#         order = input().split()
#         node = int(order[0])
#         try:
#             tree[node] = int(order[1])
#         except:
#             tree[node] = order[1]
#             dct[node] = [int(order[2]), int(order[3])]

#     key = list(dct.keys())
#     key.sort(reverse=True)

#     for i in key:
#         a, b = dct[i]
#         r = cal(tree[i], tree[a], tree[b])
#         tree[i] = r
#     print(f'#{tc} {tree[1]}')



# # 노드의 합
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0] * (N+1)
#     for _ in range(M):
#         node, value = map(int, input().split())
#         tree[node] = value
    
#     ans = 0
#     st_node = L
#     que = []
#     que.append(st_node)
#     while que:
#         find = que.pop(0)
#         left = find*2
#         if left <= N:
#             que.append(left)
#             ans += tree[left]
#         right = find*2+1
#         if right <= N:
#             que.append(right)
#             ans += tree[right]
    
#     print(f'#{tc} {ans}')