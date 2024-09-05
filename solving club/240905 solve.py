# def supernova(idx, val, level):
#     global min_v
#
#     if val >= min_v:
#         return
#
#     if level == N:
#         min_v = min(val, min_v)
#
#
#     for i in range(N):
#         if visited[i]: continue
#         visited[i] = 1
#         supernova(idx + 1, val + arr[idx][i], level + 1)
#         visited[i] = 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min_v = 0xffffffff
#     visited = [0] * N
#     supernova(0, 0, 0)
#     print(f'#{tc} {min_v}')



#
# def supernova(gas, cnt, level):
#     global min_cnt
#
#     # 움직였는데 기름이 없으면 리턴 // 가지치기
#     if gas < 0:
#         # print(f'{gas, cnt, level} 돌아가유 !')
#         return
#
#     # 이미 최솟값 넘었으면 리턴 // 가지치기
#     if cnt >= min_cnt:
#         return
#
#     # 마지막까지 왔으면 # 최소 계산
#     if lst[level] == -999:
#         min_cnt = min(min_cnt, cnt)
#
#     # print(gas, cnt, level)
#     # 기름 넣지 않고 가보기
#     supernova(gas - 1, cnt, level + 1)
#     # 기름 넣고 가보기 함수 호출은 무조건 앞으로 가기 때문에 -1 을 해줘야 해요
#     supernova(lst[level] - 1, cnt + 1, level + 1)

# T = int(input())
# for tc in range(1, T+1):
#     # 마지막 도착지점 추가 해주기
#     lst = list(map(int, input().split())) + [-999]
#     # print(lst)
#     # 첫번쨰는 필요 없는 값
#     N = lst.pop(0)
#     # print(lst)
#     min_cnt = 0xffffff
#     supernova(lst[0] - 1, 0, 1)
#     print(f'#{tc} {min_cnt}')



# 동철이
def supernova(idx, val, level):
    global max_v
    
    # 메모이제이션 이용
    if (idx, level) in memo and memo[(idx,level)] >= val * 100:
        return
    # 메모 하기
    memo[(idx, level)] = val * 100

    # //가지치기 작다면 리턴
    if val * 100 <= max_v:
        return

    # 잘 왔다면 최댓값 업데이트
    if level == N :
        val *= 100
        max_v = max(max_v, val)

    # 재귀 돌리기
    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        supernova(idx + 1, val * arr[idx][i], level + 1)
        visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)
    # 저장할 때 소수로 해주기
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100
    visited = [0] * N
    max_v = -21e8
    # 메모이제이션
    memo = {}
    # 0에서 곱하면 0이기 때문에 1에서 시작
    supernova(0, 1, 0)
    print(f'#{tc} {max_v:6f}')
