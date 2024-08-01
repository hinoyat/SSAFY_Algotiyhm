# 1210 Ladder1
from pprint import pprint

'''
시작지점이 주어진다
배열의 크기는 100 X 100
도착지점의 X좌표값 == 해당 행의 인덱스 번호
진행 방향은 기본으로 열의 인덱스를 증가시킨다

문제 풀 때 기본으로 좌우를 확인하고 없으면 아래로 가는 것이 좋을 듯?
좌 또는 우로 계속 가다가 아래를 만나면 아래로 가다가(계속 좌우 확인)
좌 또는 우로 갈 수 있으면 또 직진

구현 순서
1. 배열 생성
2. 입력값 받기
3. 배열에 입력값 넣기
4. 시작 지점 지정하기
5. 좌 or 우로 진행 확인
    5 - 1 좌 or 우로 못가면 아래로
    5 - 2 한간 갈때마다 확인은 defauiylt
'''
#
# test_case = 10
# for _ in range(1, test_case + 1):
#     tc = int(input())
#     base = [[0 for _ in range(100)] for _ in range(100)]
#     for p1 in range(100):
#         point = list(map(int, input().split()))
#         for p2 in range(100):
#             base[p1][p2] = point[p2]
#
#     # x 좌표 찾기 x = [99][x]
#     x = 0
#     for i in range(100):
#         if base[99][i] == 2:
#             x = i
#     print(x)
#     pnt = 99
#
#
#     while pnt != 0:
#         # 시작 지점 base[pnt][x]
#         # 좌우 확인 base[pnt][x+1] base[pnt][x-1]
#         if x > 0 and x < 99:
#             if base[pnt][x-1] == 0 and base[pnt][x+1] == 0:
#                 pnt -= 1
#
#             else:
#                 if base[pnt][x-1] == 1:
#                     while base[pnt][x-1] == 1:
#                         x -= 1
#                     pnt -= 1
#
#                 if base[pnt][x+1] == 1:
#                     while base[pnt][x+1] == 1:
#                         x += 1
#                     pnt -= 1
#
#
#         if x == 0:
#             if base[pnt][x + 1] == 1:
#                 while base[pnt][x + 1] == 1:
#                     x += 1
#                 pnt -= 1
#             else:
#                 pnt -= 1
#
#         if x == 99:
#             if base[pnt][x - 1] == 1:
#                 while base[pnt][x - 1] == 1:
#                     x -= 1
#                 pnt -= 1
#             else:
#                 pnt -= 1
#
#         print(pnt, x)


#
#
# test_case = 10
# for _ in range(1, test_case + 1):
#     tc = int(input())
#     base = [[0 for _ in range(100)] for _ in range(100)]
#     for p1 in range(100):
#         point = list(map(int, input().split()))
#         for p2 in range(100):
#             base[p1][p2] = point[p2]
#
#     # x 좌표 찾기 x = [99][x]
#     x = 0
#     for i in range(100):
#         if base[99][i] == 2:
#             x = i
#     # print(x)
#     pnt = 99
#
#
#     while pnt != 0:
#         # 시작 지점 base[pnt][x]
#         # 좌우 확인 base[pnt][x+1] base[pnt][x-1]
#         if x > 0 and x < 99:
#             if base[pnt][x-1] == 0 and base[pnt][x+1] == 0:
#                 pnt -= 1
#
#             else:
#                 if base[pnt][x-1] == 1:
#                     while (x+1) > 0 and base[pnt][x-1] == 1:
#                         x -= 1
#                     pnt -= 1
#                     if x-1 == 0 and base[pnt][x-1] == 1:
#                         x -= 1
#
#                 if base[pnt][x+1] == 1:
#                     while (x+1) < 99 and base[pnt][x+1] == 1:
#                         x += 1
#                     pnt -= 1
#                     if x+1 == 99 and base[pnt][x+1] == 1:
#                         x += 1
#
#
#         if x == 0:
#             if base[pnt][x + 1] == 1:
#                 while base[pnt][x + 1] == 1:
#                     x += 1
#                 pnt -= 1
#             else:
#                 pnt -= 1
#
#         if x == 99:
#             if base[pnt][x - 1] == 1:
#                 while base[pnt][x - 1] == 1:
#                     x -= 1
#                 pnt -= 1
#             else:
#                 pnt -= 1
#
#     print(f'#{tc} {x}')

# ## 달팽이 숫자
# test_case = int(input())
#
# for tc in range(1, test_case +1):
#     # 우 하 좌 상
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     N = int(input())
#     arr = [[0 for _ in range(N)]for _ in range(N)]
#
#     i = 0
#     j = 0
#     num = 0
#
#     k = 0
#
#     for s in range(N*N):
#
#         num += 1
#
#         arr[i][j] = num
#
#         new_i = i + di[k]
#         new_j = j + dj[k]
#
#         # 조건에 인덱스부터 확인해야 이거 단축평가때 배웠던 것
#         # 앞에서 True 뜨면 뒤에 안봐버림
#
#         if new_i < 0 or new_i > (N-1) or new_j < 0 or new_j > (N-1) or arr[new_i][new_j] != 0:
#             k += 1
#             if k == 4:
#                 k = 0
#
#         i = i + di[k]
#         j = j + dj[k]
#
#     # print(arr)
#     print(f'#{tc}')
#     for num in arr:
#         for i in range(N):
#             print(f'{num[i]}',end=' ')
#         print()



# 4839 이진탐색

# 이진검색 기본형
test_case = int(input())

for tc in range(1, test_case+1):
    P, page_A, page_B = map(int, input().split())
    book = []
    for i in range(P):
        book.append(i+1)

    # A가 몇 번 하는지
    # print(len(book))
    start = 1
    end = P
    cnt_A = 0
    mid = 0
    while mid != page_A:
        mid = (start + end)// 2
        if book[mid] == page_A:
            cnt_A += 1
            break
        else:
            cnt_A += 1
            if page_A > book[mid]:
                start = mid
            else:
                end = mid
    start = 1
    end = P
    cnt_B = 0
    mid = 0
    while mid != page_B:
        mid = (start + end) // 2
        if book[mid] == page_B:
            cnt_B += 1
            break
        else:
            cnt_B += 1
            if page_B > book[mid]:
                start = mid
            else:
                end = mid

    print(cnt_A)
    print(cnt_B)

    if cnt_A < cnt_B:
        print(f'#{tc} A')
    elif cnt_A > cnt_B:
        print(f'#{tc} B')
    elif cnt_A == cnt_B:
        print(f'#{tc} 0')