from pprint import pprint
# 버블 정렬 해보기

# lst = [1, 9, 7, 6, 2, 200, 61, 74, 28, 390]
# n = len(lst)
# for i in range(n-1):
#     for j in range(n-1):
#         if lst[j] >= lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# print(lst)



# # 카운팅 정렬 해보기
#
# lst2 = [0, 1, 1, 0, 5, 3, 2, 4, 2, 3, 6, 5, 4, 1, 2, 0, 0, 0, 2]
# print(f'리스트의 길이 : {len(lst2)}')
# count_lst =[0 for _ in range(7)]
# # 먼저 리스트의 원소의 개수를 리스트에 어팬드
#
# for i in range(7):
#     for j in range(len(lst2)):
#         if lst2[j] == i:
#             count_lst[i] += 1
# # print(f'원소의 개수 : {count_lst}')
#
# for i in range(6):
#     count_lst[i+1] += count_lst[i]
# print(f'누적 합 : {count_lst}')
#
# temp = [0 for _ in range(len(lst2))]
#
# print(f'데이터를 담을 장소 : {temp}')
#
# # lst2 의 마지막  값이 count의 인덱스를 하나 줄인 위치에 lst의 마지막 값을 삽입
#
# for i in range(len(lst2)-1, -1, -1):
#     count_lst[lst2[i]] -=1
#     temp[count_lst[lst2[i]]] = lst2[i]
#
# print(temp)



# # 4835 구간합
# test_case = int(input())

# for tc in range(1, test_case+1):
#     n, m = map(int, input().split())
#     lst = list(map(int, input().split()))
#     l_max = -21e8
#     l_min = 21e8
#     for i in range(n-m+1):
#         val = 0
#         for j in range(m):
#             val += lst[i+j]
#         if val >= l_max:
#             l_max = val
#         if val <= l_min:
#             l_min = val
    
#     print(f'#{tc} {l_max - l_min}')

# # 4834 숫자카드
# test_case = int(input())

# for tc in range(1, test_case+1):
#     n = int(input())
#     num = input()
#     lst = [0]*10
#     for i in range(n):
#         lst[int(num[i])] +=1
#     cnt = -21e8
#     max_num = 0
#     for j in range(len(lst)):
#         if cnt <= lst[j]:
#             cnt = lst[j]
#             max_num = j

#     print(f'#{tc} {max_num} {cnt}')

# # 4831 전기빠쓰

# test_case = int(input())

# for tc in range(1, test_case+1):
#     # K이동 한도 N 총 정류장 M 충전기 정류장 수
#     K, N, M = map(int, input().split())
#     bus_stop = [0] + list(map(int, input().split())) + [N]
    
#     # 가는지 못 가는지
#     possible = True
#     for bus in range(1, len(bus_stop)):
#         if bus_stop[bus] - bus_stop[bus-1] > K:
#             possible = False
#             break
#     k = K
#     cnt = 0
#     for i in range(1,len(bus_stop) -1):
#         print(f'기름{k} 정류장{i+1}')
#         k -= (bus_stop[i+1] - bus_stop[i])
#         if bus_stop[i+1] - bus_stop[i] > k:
#             k = K
#             cnt += 1
#             k -= (bus_stop[i+1] - bus_stop[i])
#         else:
#             pass
        
#     print(cnt)


#     # 수정 버전
#     # 4831 전기빠쓰

# test_case = int(input())

# for tc in range(1, test_case+1):
#     # K이동 한도 N 총 정류장 M 충전기 정류장 수
#     K, N, M = map(int, input().split())
#     bus_stop = [0] + list(map(int, input().split())) + [N]
    
#     # 가는지 못 가는지
#     possible = True
#     for bus in range(1, len(bus_stop)):
#         if bus_stop[bus] - bus_stop[bus-1] > K:
#             possible = False
#             break
#     k = K
#     cnt = 0
#     for i in range(1,len(bus_stop)):
#         # print(f'기름{k} 정류장{i+1}')
#         # k -= (bus_stop[i] - bus_stop[i-1])
#         if bus_stop[i] - bus_stop[i-1] > k:
#             k = K
#             cnt += 1
#         k -= (bus_stop[i] - bus_stop[i-1])

#     if possible == True:
#         print(f'#{tc} {cnt}')
#     else:
#         print(f'#{tc} 0')



# 4825 min max

# test_case = int(input())

# for tc in range(1, test_case+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
    
#     ## 버블 쏘뜨
#     for i in range(N-1,0,-1):
#         for j in range(N-1):
#             if lst[j] >= lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j] 
#     # print(lst)

#     print(f'#{tc} {lst[N-1] - lst[0]}')

#     def min_max(lst):


# # 4825 min max version 2
# def min_max(lst):
#     for i in range(N-1,0,-1):
#         for j in range(N-1):
#             if lst[j] >= lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j] 
#     value = lst[N-1] - lst[0]
#     return value


# test_case = int(input())

# for tc in range(1, test_case+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     val = min_max(lst)
#     print(f'#{tc} {val}')



# # 9836 연속한 1의 개수

# test_case = int(input())

# for tc in range(1, test_case+1):
#     N = int(input())
#     num = input()+'0'
#     one_max = -21e8
#     cnt = 0
#     n = 0
#     while n < N:
#         if num[n] == '1':
#             cnt += 1
#             if one_max <= cnt :
#                 one_max = cnt
#         else:
#             if one_max <= cnt :
#                 one_max = cnt
#                 cnt = 0
#         n += 1

#     print(f'#{tc} {one_max}')



# # 삼성시의 버스 노선 dict 버존

# test_case = int(input())

# for tc in range(1, test_case+1):
#     N = int(input())
#     station = {}
#     for i in range(N):
#         a, b = map(int,input().split())
#         for j in range(a,b+1):
#             if j in station:
#                 station[j] += 1
#             else:
#                 station[j] = 1
#     # print(station)
#     st_lst = []
#     P = int(input())
#     for _ in range(P):
#         st_num = int(input())
#         st_lst.append(st_num)
#     # print(st_lst)
#     print(f'#{tc}',end=' ')
#     for i in st_lst:
#         print(station.get(i,0), end=' ')
#     print()


# # 1945 간단한 소인수 분해

# N = [2, 3, 5, 7, 11]

# test_case = int(input())

# for tc in range(1, test_case+1):
#     cnt = []
#     num = int(input())
#     for i in N:
#         count = 0
#         while num % i == 0:
#             num //= i
#             count += 1
#         cnt.append(count)
#     print(f'#{tc}', end=' ')
#     print(*cnt)


# Flatten
# test_case = 10

# for tc in range(1, test_case+1):
#     dump = int(input())
#     box = list(map(int, input().split()))
#     for i in range(len(box)-1):
#         for j in range(len(box) -1):
#             if box[j] >= box[j+1]:
#                 box[j], box[j+1] = box[j+1], box[j]
#     # print(len(box))
#     for d in range(dump):
#         box[0] += 1
#         box[99] -= 1
        
#         for i in range(len(box)-1, 0, -1):
#             for j in range(len(box) -1):
#                 if box[j] >= box[j+1]:
#                     box[j], box[j+1] = box[j+1], box[j]

#         if box[99] - box[0] == 1 or box[99] - box[0] == 0:
#             break

#     print(f'#{tc} {(box[99]) - (box[0])}')
#     # print(box)


# # View
# test_case = 10

# for tc in range(1, test_case+1):
#     N = int(input())
#     buil = list(map(int,input().split()))
#     sun = 0
#     for s in range(2, N-2):
#         # 5개 중에 max
#         b_lst = buil[s-2:s+3]
#         for i in range(len(b_lst)-1, 0, -1):
#             for j in range(len(b_lst)-1):
#                 if b_lst[j] >= b_lst[j+1]:
#                     b_lst[j], b_lst[j+1] = b_lst[j+1], b_lst[j]
#         if buil[s] >= b_lst[3]:
#             sun += buil[s] - b_lst[3]
#     print(f'#{tc} {sun}')

# # 축약 버전
# test_case = 10

# for tc in range(1, test_case + 1):
#     N = int(input())
#     buil = list(map(int, input().split()))
#     sun = 0
#     for s in range(2, N - 2):
#         b_lst = sorted(buil[s - 2:s + 3])
#         if buil[s] > b_lst[3]:
#             sun += buil[s] - b_lst[3]
#     print(f'#{tc} {sun}')


# # 4837 부분집합의 합
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     A = [num for num in range(1, 13)]
#     # N은 원소의 수 K는 원소의 합
#     N, K = map(int,input().split())
#     print(A)
#     cnt = 0
#     for i in range(2**len(A)):
#         sum_val = 0
#         lst = []
#         for j in range(len(A)):
#             if i & (1<<j):
#                 sum_val += A[j]
#                 lst.append(A[j])
#         if len(lst) == N:
#             if sum_val == K:
#                 cnt += 1
#     print(f'#{tc} {cnt}')



# # 4836 색칠하기 # 숫자로 계산
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     arr = [[0 for _ in range(10)]for _ in range(10)]
#     for n in range(N):
#         # r1, c1, r2, c2, color
#         r1, c1, r2, c2, color = map(int, input().split())
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 arr[i][j] += color
#     cnt = 0
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == 3:
#                 cnt += 1
#     print(f'#{tc} {cnt}')
#     # pprint(arr)

# # 4836 색칠하기 # 리스트로 계산
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     arr = [[[]for _ in range(10)]for _ in range(10)]
#     for n in range(N):
#             # r1, c1, r2, c2, color
#             r1, c1, r2, c2, color = list(map(int, input().split()))
#             for i in range(r1, r2+1):
#                 for j in range(c1, c2+1):
#                     arr[i][j].append(color)
#     cnt = 0
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == [1, 2] or arr[i][j] == [2,1]:
#                 cnt += 1
#     print(f'#{tc} {cnt}')


# # 파리 퇴치
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N, M = map(int,input().split())
#     fly_lst = []
#     for f in range(N):
#         fly = list(map(int, input().split()))
#         fly_lst.append(fly)
    
#     kill_max = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             kill = 0
#             for s in range(M):
#                 for d in range(M):
#                     kill += fly_lst[i+s][j+d]

#             if kill_max < kill:
#                 kill_max = kill

#     print(f'#{tc} {kill_max}')


# # 어디에 단어가 들어가냐

# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N, K = map(int, input().split())
#     puz_lst = []
#     for _ in range(N):
#         puz = list(map(int, input().split())) + [0]
#         puz_lst.append(puz)
#     puz_lst.append([0]*(N+1))
#     # pprint(puz_lst)
#     cnt = 0
#     for i in range(0, N+1):
#         c_len = 0
#         r_len = 0
#         for j in range(0, N+1):
#             if puz_lst[i][j] == 1:
#                 c_len += 1
#             else:
#                 if c_len == K:
#                     cnt +=1
#                     c_len = 0
#                 else:
#                     c_len = 0
#             if puz_lst[j][i] == 1:
#                 r_len += 1
#             else:
#                 if r_len == K:
#                     cnt +=1
#                     r_len = 0
#                 else:
#                     r_len = 0
#     print(f'#{tc} {cnt}')


# # Version 222

# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N, K = map(int, input().split())
#     puz_lst = []
#     for _ in range(N):
#         puz = list(map(int, input().split())) + [0]
#         puz_lst.append(puz)
#     puz_lst.append([0]*(N+1))
#     # pprint(puz_lst)
#     cnt = 0
#     row = 0
#     for i in range(N+1):
#         s = 0
#         i_val = 0
#         j_val = 0
#         while s < N+1:
#             if puz_lst[i][s] == 1:
#                 i_val += 1
#             else:
#                 if i_val == K:
#                     i_val = 0
#                     cnt += 1
#                 else:
#                     i_val = 0
          
#             if puz_lst[s][i] == 1:
#                 j_val += 1
#             else:
#                 if j_val == K:
#                     j_val = 0
#                     cnt += 1
#                 else:
#                     j_val = 0
          
          
#             s += 1


#     print(f'#{tc} {cnt}')


# # 스도쿠 검증
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     arr = []
#     for _ in range(9):
#         a = list(map(int, input().split()))
#         arr.append(a)

#     possible = 1
#     # pprint(arr)
#         # 상 하 좌 우 왼위 오위 좌아 우아

#     num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
#     for i in range(9):
#         check_col = []
#         check_row = []
#         for j in range(9):
#             check_col.append(arr[i][j])
#             check_row.append(arr[j][i])
#         if len(set(check_col)) != 9:
#             possible = 0
        
#         if len(set(check_row)) != 9:
#             possible = 0

#         # print(check_col)
#         # print(check_row)



#     di = [0, -1, 1, 0, 0, -1, -1, 1, 1]
#     dj = [0, 0, 0, -1, 1, -1, 1, -1, 1]
    
#     for i in range(1, 9, 3):
#         ij = 0
#         for j in range(1, 9, 3):
#             check_lst = []
#             for d in range(9):
#                 check_lst.append(arr[i+di[d]][j+dj[d]])
#             set_c = set(check_lst)
#             if len(set_c) != 9:
#                 possible = 0

#             # print(check_lst)

#     print(f'#{tc} {possible}')


# # 정기고 sum
# test_case = 10
# for _ in range(1, test_case + 1):
#     tc = int(input())
#     arr = []
#     for _ in range(100):
#         ar = list(map(int, input().split()))
#         arr.append(ar)
#     n = len(arr)
   
#    # 행 열
#     arr_max = 0
#     for i in range(n):
#         sum_row = 0
#         sum_col = 0
#         for j in range(n):
#             sum_row += arr[i][j]
#             sum_col += arr[j][i]

#         if arr_max <= sum_row:
#             arr_max = sum_row

#         if arr_max <= sum_col:
#             arr_max = sum_col

#     # \ 대각선
#     sum_a = 0
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 sum_a += arr[i][j]
#         if arr_max <= sum_a:
#             arr_max = sum_a
    
#     sum_b = 0
#     for i in range(0, n, -1):
#         for j in range(n):
#             if n - i - 1 == j:
#                 sum_b += arr[i][j]
#         if arr_max <= sum_b:
#             arr_max = sum_b

#     print(f'#{tc} {arr_max}')


# # 풍선팡 2
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N, M = map(int, input().split())
#     arr = []
#     for a in range(N):
#         ar = list(map(int, input().split()))
#         arr.append(ar)
#     # pprint(arr)
#         # 우 하 좌 상
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]

#     pop_max = 0
#     for i in range(N):
#         for j in range(M):
#             pop_sum = 0
#             pop_sum += arr[i][j]
#             for b in range(4):
#                 new_r = i + dr[b]
#                 new_c = j + dc[b]
#                 if new_r >= 0 and new_r < N and new_c >= 0 and new_c < M :
#                     pop_sum += arr[new_r][new_c]
#             if pop_max <= pop_sum:
#                 pop_max = pop_sum

#     print(f'#{tc} {pop_max}')


# # 풍선팡 1
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N, M = map(int, input().split())
#     arr = []
#     for a in range(N):
#         ar = list(map(int, input().split()))
#         arr.append(ar)
    
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
    
#     pop_max = 0
#     for i in range(N):
#         for j in range(M):
#             pop_cnt = arr[i][j]
#             pop_sum = arr[i][j]
#             for p in range(1, pop_cnt+1):
#                 for d in range(4):
#                     newr = i + dr[d] * p
#                     newc = j + dc[d] * p
#                     if 0 <= newr < N and 0 <= newc < M:
#                         pop_sum += arr[newr][newc]
#             if pop_max <= pop_sum:
#                 pop_max = pop_sum

#     print(f'#{tc} {pop_max}')


# # 달팽이
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     arr = [[0 for _ in range(N)]for _ in range(N)]

#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
    
#     num = 1
#     i = 0
#     j = 0

#     idx = 0
#     for s in range(N*N):
#         arr[i][j] = num
#         num += 1
#         newr = i + dr[idx]
#         newc = j + dc[idx]
#         if not(0 <= newr < N) or not(0 <= newc < N) or arr[newr][newc] != 0:
#             idx += 1
#             if idx == 4:
#                 idx =0
#         else:
#             pass
#         i = i + dr[idx]
#         j = j + dc[idx]

#     print(f'#{tc}')                
#     for ar in arr:
#         print(*ar)


# # 특별한 정렬
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))

#     for i in range(N-1):

#         if i % 2 == 0:
#             max_i = i
#             for j in range(i+1, N):
#                 if lst[max_i] < lst[j]:
#                     max_i = j
#             lst[i], lst[max_i] = lst[max_i], lst[i]
        
#         else:
#             min_i = i
#             for j in range(i+1, N):
#                 if lst[min_i] > lst[j]:
#                     min_i = j
#             lst[i], lst[min_i] = lst[min_i], lst[i]

#     print(f'#{tc}',end=' ')
#     print(*lst[0:10])

# # 이진탐샠
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     P, A, B = map(int, input().split()) 
    
#     start = 1
#     end = P
#     cnt_a = 0
#     while start <= end:
#         cen = int((start + end)/2)
#         cnt_a += 1
#         if cen == A:
#             break
#         elif cen > A:
#             end = cen
#         else:
#             start = cen
    
#     start = 1
#     end = P
#     cnt_b = 0
#     while start <= end:
#         cen = int((start + end)/2)
#         cnt_b += 1
#         if cen == B:
#             break
#         elif cen > B:
#             end = cen
#         else: 
#             start = cen
    
#     winner = None

#     if cnt_a > cnt_b:
#         winner = 'B'
#     elif cnt_a < cnt_b:
#         winner = 'A'
#     else:
#         winner = 0
#     print(f'#{tc} {winner}')

# # # 이진 Ver.2
# def who_is_winner(page):
#     start = 1
#     end = P
#     cnt = 0
#     while start <= end:
#         cen = int((start + end)/2)
#         cnt += 1
#         if cen == page:
#             break
#         elif cen > page:
#             end = cen
#         else:
#             start = cen
#     return cnt

# test_case = int(input())
# for tc in range(1, test_case + 1):
#     P, A, B = map(int, input().split()) 
    
#     a = who_is_winner(A)
#     b = who_is_winner(B)

#     winner = None

#     if a > b:
#         winner = 'B'
#     elif a < b:
#         winner = 'A'
#     else:
#         winner = 0

#     print(f'#{tc} {winner}')

# # 고대유적
# test_case = int(input())
# for tc in range(1, test_case + 1):
#     N, M = map(int, input().split())
#     arr = [[0 for _ in range(M)]for _ in range(N)]
#     for a in range(N):
#         lst = list(map(int, input().split()))
#         for b in range(M):
#             arr[a][b] = lst[b]
    
#     max_len = 0

#     for i in range(N):
#         r_len = 0
#         for j in range(M):
#             if arr[i][j] == 1:
#                 r_len += 1
#                 if r_len > max_len:
#                     max_len = r_len
#             else:
#                 r_len = 0

#     for i in range(M):
#         c_len = 0
#         for j in range(N):
#             if arr[j][i] == 1:
#                 c_len += 1
#                 if c_len > max_len:
#                     max_len = c_len
#             else:
#                 c_len = 0
#     print(f'#{tc} {max_len}')

