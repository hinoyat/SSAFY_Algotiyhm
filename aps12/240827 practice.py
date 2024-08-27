
# def inorder(root_index):
#     global v
#     if root_index <= N:
#         inorder(root_index*2)
#         TREE_V[TREE[root_index]] = v
#         v += 1
#         # print(TREE[root_index])
#         inorder(root_index*2+1)

# T = int(input())
# for tc in range(1, T+1):       
#     N = int(input())
#     arr = [i for i in range(1, N+1)]

#     TREE = [0]*(N+1)
#     for i in range(len(arr)):
#         TREE[i+1] = arr[i]

#     TREE_V = [0] * (N+1)
#     v = 1
#     inorder(v)
#     # print(TREE)
#     print(f'#{tc} {TREE_V[1]} {TREE_V[N//2]}')


# def DFS(start):
#     stack = []
#     visited = [0] * (max(lst)+1)
#     stack.append(start)
#     visited[start] = 1
#     cnt = 0

#     while stack:
#         p = stack.pop()
#         cnt += 1
#         for i in V[p]:
#             if visited[i] == 0:
#                 stack.append(i)
#                 visited[i] = 1

#     return cnt

# T = int(input())
# for tc in range(1, T + 1):
#     E, N = map(int, input().split())
#     lst = list(map(int, input().split()))

#     V = [[] for _ in range(max(lst) + 1)]
#     for i in range(0, len(lst), 2):
#         v1, v2 = lst[i], lst[i + 1]
#         V[v1].append(v2)

#     print(f'#{tc} {DFS(N)}')

# def inorder(idx):
#     global result
#     if idx <= N:
#         inorder(idx*2)
#         result.append(TREE[idx])
#         inorder(idx*2+1)


# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     TREE = [0] * (N+1)
#     for n in range(N):
#         a = list(map(str, input().split()))
#         a1 = int(a[0])
#         a2 = a[1]
#         TREE[a1] = a2
#     result = []
#     inorder(1)
#     print(f'#{tc} {"".join(result)}')
    
'''
6
ABCDEF
'''
def preorder(root_index):
    if root_index <= N:
    # if TREE[root_index]:
        print(TREE[root_index])
        preorder(root_index*2)
        preorder(root_index*2+1)

def inorder(root_index):
    if root_index <= N:
        inorder(root_index*2)
        print(TREE[root_index])
        inorder(root_index*2+1)

def postorder(root_index):
    if root_index <= N:
        postorder(root_index*2)
        postorder(root_index*2+1)
        print(TREE[root_index])

N = int(input())
arr = input()

TREE = [0]*(N+1)
for i in range(len(arr)):
    TREE[i+1] = arr[i]

print(TREE)