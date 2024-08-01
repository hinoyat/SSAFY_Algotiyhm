from pprint import pprint


# 1210 Ladder1

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
# test_case = int(input())

# for tc in range(1, test_case+1):
#     P, page_A, page_B = map(int, input().split())
#     book = []
#     for i in range(P):
#         book.append(i+1)

#     # A가 몇 번 하는지
#     # print(len(book))
#     start = 1
#     end = P
#     cnt_A = 0
#     mid = 0
#     while mid != page_A:
#         mid = (start + end)// 2
#         if book[mid] == page_A:
#             cnt_A += 1
#             break
#         else:
#             cnt_A += 1
#             if page_A > book[mid]:
#                 start = mid
#             else:
#                 end = mid
#     start = 1
#     end = P
#     cnt_B = 0
#     mid = 0
#     while mid != page_B:
#         mid = (start + end) // 2
#         if book[mid] == page_B:
#             cnt_B += 1
#             break
#         else:
#             cnt_B += 1
#             if page_B > book[mid]:
#                 start = mid
#             else:
#                 end = mid

#     print(cnt_A)
#     print(cnt_B)

#     if cnt_A < cnt_B:
#         print(f'#{tc} A')
#     elif cnt_A > cnt_B:
#         print(f'#{tc} B')
#     elif cnt_A == cnt_B:
#         print(f'#{tc} 0')


## 수정본
# test_case = int(input())

# for tc in range(1, test_case+1):
#     P, page_A, page_B = map(int, input().split())

#     # A가 몇 번 하는지
#     # print(len(book))
#     start = 1
#     end = P
#     cnt_A = 0
#     mid = 0
#     while mid != page_A:
#         mid = (start+end)//2
#         if mid == page_A:
#             cnt_A += 1
#         elif mid > page_A:
#             end = mid
#         else:
#             start = mid
#         cnt_A += 1

#     start = 1
#     end = P
#     cnt_B = 0
#     mid = 0
#     while mid != page_B:
#         mid = (start+end)//2
#         if mid == page_B:
#             cnt_B += 1
#         elif mid > page_B:
#             end = mid
#         else:
#             start = mid
#         cnt_B += 1

#     # print(cnt_A)
#     # print(cnt_B)

#     if cnt_A < cnt_B:
#         print(f'#{tc} A')
#     elif cnt_A > cnt_B:
#         print(f'#{tc} B')
#     elif cnt_A == cnt_B:
#         print(f'#{tc} 0')

# # 4843 턱별한 정렬
# test_case = int(input())

# for tc in range(1, test_case+1):
#     n = int(input())
#     num = list(map(int,input().split()))
    
#     # pprint(num)

#     lst= []
#     ## min 값 찾고 append max값 찾고 append
#     ## min 값 max 값 초기화
#     lst2 = num[:]
#     while len(lst2) != 0:
#         max_num = -21e8
#         min_num = 21e8
#         for i in range(len(lst2)):
#             if lst2[i] >= max_num:
#                 max_num = lst2[i]
#             if lst2[i] <= min_num:
#                 min_num = lst2[i]

#         for max in range(len(lst2)):
#             if lst2[max] == max_num:
#                 lst.append(lst2[max])
#                 lst2.pop(max)
#                 break
        
#         for min in range(len(lst2)):
#             if lst2[min] == min_num:
#                 lst.append(lst2[min])
#                 lst2.pop(min)
#                 break
            
#     print(f'#{tc}',end=' ')
#     for out in range(10):
#         print(lst[out], end=' ')
#     print()



# # 풍선팡 1
# test_case = int(input())

# for tc in range(1, test_case + 1):
#     # n 행 m 열
#     n, m = map(int, input().split())
#     arr = [[0 for _ in range(m)]for _ in range(n)]
#     for bl1 in range(n):
#         bl_lst = list(map(int, input().split()))
#         for bl2 in range(m):
#             arr[bl1][bl2] = bl_lst[bl2]

#         #우 하 좌 상
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     k = 0

#     # pprint(arr)
#     max = -21e8
#     for i in range(n):
#         for j in range(m):
#             sum = 0
#             sum += arr[i][j]
#             for d in range(4):
#                 new_i = i + di[d]
#                 new_j = j + dj[d]
#                 if 0 <= new_i <n and 0 <= new_j <m:
#                     sum += arr[new_i][new_j]
#             if sum >= max:
#                 max =sum
                
            
#     print(f'#{tc} {max}')

# 풍선팡 2

test_case = int(input())

for tc in range(1, test_case + 1):
    # n 행 m 열
    n, m = map(int, input().split())
    arr = [[0 for _ in range(m)]for _ in range(n)]
    for bl1 in range(n):
        bl_lst = list(map(int, input().split()))
        for bl2 in range(m):
            arr[bl1][bl2] = bl_lst[bl2]
#         #우 하 좌 상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    k = 0

    # pprint(arr)
    max = -21e8
    for i in range(n):
        for j in range(m):
            sum = 0
            sum += arr[i][j]
            # 4 방향 잡기
            for d in range(4):
                new_i = i + di[d]
                new_j = j + dj[d]
                for plus in range(arr[i][j]):
                    if 0<= new_i<n and 0<= new_j<m:
                        sum += arr[new_i][new_j]
                        if d == 0:
                            new_j += 1
                        if d == 1:
                            new_i += 1
                        if d == 2:
                            new_j += -1
                        if d == 3:
                            new_i += -1
                
            if sum >= max:
                max = sum
    print(f'#{tc} {max}')
                # while 0<= new_i <n and 0<= new_j <m:
                #     sum += arr[new_i][new_j]
                #     if d == 0:
                #         new_j += 1
                #     if d == 1:
                #         new_i += 1
                #     if d == 2:
                #         new_j += -1
                #     if d == 3:
                #         new_i += -1
                #     print(sum)