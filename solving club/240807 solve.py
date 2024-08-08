# # 방식 1 인접 리스트
# def dfs(V, start, end):        # s 시작 정점, V 정점개수 (1번부터인 정점의 마지막 정점)
#     visited = [0] * (V+1)   # 방문한 정점을 표시
#     stack = []
#     stack.append(start)         # 시작 정점 방문표시
#     # 스택 생성
#     visited[start] = 1
#     while stack:
#         cur = stack.pop()
#         if cur == end:
#             return 1
#         for j in lst[cur]:
#             if not visited[j]:
#                 stack.append(j)
#                 visited[j] = 1
#     return  0
#
#
# test_case = int(input())
# for tc in range(1, test_case+1):
#     # V 정점 수 E는 간선
#     V, E = map(int, input().split())
#     lst = [[] for _ in range(V + 1)]
#
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         lst[v1].append(v2)
#     start, end = map(int, input().split())
#
#     result = dfs(V, start, end)
#
#     print(f'#{tc} {result}')


# # 종이 붙이기
#
# def sl_paper(n):
#     if n == 10:
#         return 1
#     elif n == 20:
#         return 3
#     else:
#         return sl_paper(n-10) + sl_paper(n-20) *2
#
# test_case = int(input())
# for tc in range(1, test_case+1):
#     N = int(input())
#     result = sl_paper(N)
#     print(f'#{tc} {result}')


# # D4 길찾기
# def dfs(V, start, end):        # s 시작 정점, V 정점개수 (1번부터인 정점의 마지막 정점)
#     visited = [0] * (V+1)   # 방문한 정점을 표시
#     stack = []
#     stack.append(start)         # 시작 정점 방문표시
#     # 스택 생성
#     visited[start] = 1
#     while stack:
#         cur = stack.pop()
#         if cur == end:
#             return 1
#         for j in lst[cur]:
#             if not visited[j]:
#                 stack.append(j)
#                 visited[j] = 1
#     return 0
#
#
# test_case = 10
# for _ in range(1, test_case+1):
#     start = 0
#     end = 99
#     tc, len_lst = map(int, input().split())
#     lst = [[] for _ in range(101)]
#     # print(lst)
#
#     in_lst = list(map(int, input().split()))
#     for i in range(len_lst):
#         v1, v2 = in_lst[i*2], in_lst[i*2+1]
#         lst[v1].append(v2)
#
#     # print(lst)
#     result = dfs(100, start, end)
#     print(f'#{tc} {result}')


# 강사임이 푸러주는 길 찾기
# def dfs(S):
#     stack = []
#     stack.append(S)
#     visited = [False] * (V+1)
#     visited[S] = True
#     while stack:
#         v = stack.pop()
#         if v == G:
#             return 1
#         for w in graph[v]:
#             if visited[w] != True:
#                 stack.append(w)
#                 visited[w] = True
#     return 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input())
#     graph = [[] for _ in range(V+1)]
#
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#
#     S, G = map(int,input().split())
#     result = dfs(S)
#     print(result)




# # # 백만장자 프로젝트 틀림;';;;;;;;;;;;
# test_case = int(input())
# for tc in range(1, test_case+1):
#     N = int(input())
#     price_lst = list(map(int, input().split()))
#     print(price_lst)
#     max_p = max(price_lst)

#     sell = 0
#     i = 0
#     buy = 0
#     cnt = 0
#     # max 값까지 계속 사기
#     while i <  N:
#         if price_lst[i] == max_p:
#             sell += price_lst[i] * cnt - buy
#             cnt += 1
#             break
#         else:
#             buy += price_lst[i]
#             cnt += 1
#         i += 1
    
#     for _ in range(cnt):
#         price_lst.pop(0)
    
#     buy = 0
#     cnt = 0
#     # 이제 끝날 때 까지 해보자
#     while len(price_lst) > 1:
#         v = price_lst.pop(0)
#         max_p = max(price_lst)
#         if len(price_lst) == 1:
#             if v >= price_lst[0]:
#                 break
#             else:
#                 cnt += 1
#                 buy += v
#                 sell += (price_lst[0] * cnt) - buy
#         if len(price_lst)>1:
#             if v < max_p:
#                 buy += v
#                 cnt += 1
#             elif v == max_p:
#                 sell += price_lst[0] * cnt - buy
#                 cnt += 1
#                 buy = 0
#             else:
#                 pass
                
#     print(f'번 돈{sell} 인덱스{i} 구매한 가격{buy}  판매 수{cnt}')



# ## 백만장자 2
# test_case = int(input())
# for tc in range(1, test_case+1):
#     N = int(input())
#     price_lst = list(map(int, input().split()))
#     # print(price_lst)

#     sell = 0
#     i = 0
#     buy = 0
#     cnt = 0
#     # max 값까지 계속 사기
#     while i <  N:
#         max_p = max(price_lst[i:])
#         if price_lst[i] < max_p:
#             buy += price_lst[i]
#             cnt += 1

#         if price_lst[i] == max_p:
#             sell += price_lst[i] * cnt - buy
#             cnt += 1
#             buy = 0
#             cnt = 0
#         i += 1
#     # print(f'번 돈{sell} 인덱스{i} 구매한 가격{buy} 판매 수{cnt}')
#     print(f'#{tc} {sell}')        

# # 백만장자 뒤에서부터
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     price_lst = list(map(int, input().split()))
#     max_i = N-1
#     sell = 0
#     max_p = price_lst[max_i]
#     for i in range(N - 2, -1, -1):
#         if price_lst[i] > max_p:
#             max_p = price_lst[i]
#         sell += max_p - price_lst[i]
        
#     print(f'#{tc} {sell}')




# # 붕어빵 팔기
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     # N명의 사람 # M 붕어빤 시간 # K개 붕어빵
#     N, M, K = map(int, input().split())
#     pep = list(map(int, input().split()))
#     dct = {}
#     dct[0] = 0
#     pep.sort()
#     for i in pep:
#         if i not in dct:
#             dct[i] = 1
#         else:
#             dct[i] += 1
#     a = [0] + list(dct.keys())
#     can = False
#     time = -1
#     i = 1
#     while time != max(pep) and i < len(a):
#         time+=1
#         fish = (time // M) * K
#         if time == a[i]:
#             if fish >= dct[a[i-1]]:
#                 can = True
#                 dct[a[i]] += dct[a[i-1]]
#                 i += 1
#             else:
#                 can = False
#                 break
#     print(f'#{tc} {can}')


# #붕어빵 찾기
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     # N명의 사람 # M 붕어빤 시간 # K개 붕어빵
#     N, M, K = map(int, input().split())
#     people = list(map(int, input().split()))
#     people.sort()


#     fish = 0
#     time = 0
#     total_time = 0
#     i = 0

#     possible = 'Possible'
#     while i < len(people):
#         if time > 0:
#             if time % M == 0:
#                 fish += K


#         if time == people[i]:
#             fish -= 1
#             if fish < 0:
#                 possible = 'Impossible'
#                 break
#             else:
#                 i += 1
#         time +=1

#     print(f'{tc} {possible}')



#붕빵어 찾기
test_case = int(input())
for tc in range(1, test_case + 1):
    # N명의 사람 # M 붕어빤 시간 # K개 붕어빵
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))

    people.sort()

    # 붕어빵 저장소
    fish = 0
    # 흘러 가버린 시간
    time = 0
    # 사람들 오는 시간 리스트의 인덱스
    i = 0

    # 기본 값은 가능!
    possible = 'Possible'

    # 사람들이 다 올 동안에
    while i < len(people):

        # 내가 만든 붕어빵 구하기
        # 조건이 0보다 큰 경우로 잡은 이유 : 시간이 0일때는 붕어빵을 못 만들어요
        # 시간이 1보다 클 때 만들 수 있어요
        if time > 0:
            # 붕어빵을 만드는데 걸리는 시간이 M이니까
            # 시간이 M만큼 지나갔을 때 만들 수 있어요
            # 나머지가 0인 경우가 M만큼 지나간 경우
            if time % M == 0:
                fish += K

        # 이 사람이 온 시간이 되면
        # 이때까지는 붕어빵을 계속 만들 거에요 시간 늘리면서
        # 시간이 될 때까지 time 늘려요 if 문에 걸릴 때까지
        if time >= people[i]:
            # 붕어빵 하나 팔기
            fish -= 1
            # 팔았는데 붕어빵이 0개보다 적다?
            if fish < 0:
                # 탈락
                possible = 'Impossible'
                break
            # 붕어빵이 0개 이거나 남았다?
            else: 
                # 다음사람 받을 준비
                i += 1
        # 아무일도 없다? 시간 늘려
        time += 1

    print(f'#{tc} {possible}')