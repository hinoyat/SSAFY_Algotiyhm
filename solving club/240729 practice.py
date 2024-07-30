# 예제
# n = int(input())
# lst = list(map(int,input().split()))
# max_v =0
# for i in range(n-1):
#     base_l = lst[i]
#     # base_l보다 작은 길이의 갯수를 센다
#     cnt = 0
#     for j in range(i+1, n):
#         if base_l > lst[i]:
#             cnt += 1
#
#     if max_v < cnt:
#         max_v = cnt
# print(max_v)




# # 4828 minmax
# t = int(input())

# for i in range(t):
#     n = int(input())
#     num = list(map(int,input().split()))
#     max = 0
#     min = 10000000000
#     for s in num:
#         if s>=max:
#             max = s
#         if s <= min:
#             min = s
#     print(f'#{i+1} {max-min}')



# # 4835 구간합
# t = int(input())

# for i in range(t):
#     sum_lst = []
#     total_idx, sum_idx = map(int,input().split())
#     num_lst = list(map(int,input().split()))
#     for s in range(0,total_idx-sum_idx+1):
#         value = 0
#         for d in range(sum_idx):
#             value += num_lst[s+d]
#         sum_lst.append(value)

#     sum_lst.sort()
#     max = sum_lst[len(sum_lst)-1]
#     min = sum_lst[0]
#     print(f'#{i+1} {int(max-min)}')

# # 1일차 -Veiw
# test_case = 10
# for i in range(test_case):
#     n = int(input())
#     building = list(map(int, input().split()))
#     sun_good = []
#     for s in range(2, n-2):
#         check_list = building[s-2:s+3]
#         # print(check_list)
#         center_building = check_list.pop(2)
#         # print(check_list)
#         # print(center_building)
#         max = 0
#         for d in check_list:
#             if d >= max:
#                 max = d
#         # print(max)
#         if center_building >= max:
#             sun_good.append(center_building-max)
#     sum_building = 0
#     for num in sun_good:
#         sum_building += num
#
#     print(f'#{i+1} {sum_building}')


# # 4831 전기버스
# t = int(input())
# for i in range(t):
#     k, n, m = map(int, input().split())
#     m = list(map(int, input().split()))
#     first_lst = [0 for _ in range(n)]
#     first_lst[0] = k
#
#     for j in m:
#         first_lst[j] = k
#     print(first_lst)
#     fail_lst = []
#     for d in range(n-k):
#         if sum(first_lst[d:d+k]) == 0:
#             fail_lst.append('0')
#         else:
#             fail_lst.append('1')
#     print(fail_lst)
#     if n % k == 0:
#         run_count = n // k -1
#     else:
#         run_count = n // k
#     if '0' in fail_lst:
#         print(f'#{i+1} 0')
#     else:
#         print(f'#{i+1} {run_count}')
#

# # 전기 버스 2
# t = int(input())
# for i in range(t):
#     k, n, m = map(int, input().split())
#     m = list(map(int, input().split()))
#     first_lst = [0 for _ in range(n)]
#     for j in m:
#         first_lst[j] = k
#     # 정류장에 충전소 할당 만날때마다 k를 리스트의 값 으로 만들어 주기 움직일 때마다 1씩 뺴주기
#     second_lst = first_lst[:]
#     second_lst[0] = k
#     print(first_lst)
#     print(second_lst)
#     for bus in range(n-1):
#         if second_lst[bus] > 1:
#         second_lst[bus+1] = second_lst[bus] - 1    
#         # if second_lst[bus] <= 1:
#         #     second_lst[bus] = first_lst[bus]
#         #     if first_lst[bus] == 0:
#         #         print(0)
                


# # 전기버스 3333333333333333333333
# t = int(input())
# for i in range(t):
#     k, n, m = map(int, input().split())
#     m = list(map(int, input().split()))
#     first_lst = [0 for _ in range(n+1)]
#     for






# # 4831 전기버스
# # 이거는 주말에 다시 집에서 혼자 이 방법 말고 풀어보기
# t = int(input())
# for i in range(t):
#     k, n, m = map(int, input().split())
#     m_lst = list(map(int, input().split()))
#     m_lst.append(n)
#     # 충전해야 하는 횟수
#     cnt = 0
#     # 전기통
#     fuel = k
#     # 1칸씩 버스가 갑니다
#     for s in range(1, n):
#         # 연료가 1씩 빠져요
#         fuel -= 1
#         # 근데 여기서 해당 정류장에 충전소가 있으면
#         if s in m_lst:
#             # 기름이 0보다 적다? 탈락
#             if fuel < 0:
#                 cnt = 0
#             # 다음 정류장 까지의 거리가 현재 갈 수 있는 거리보다 길다?
#             elif m_lst[m_lst.index(s)+1] - s > fuel:
#                 # 전기 충전하고
#                 fuel = k
#                 # 충전 횟수 늘려요
#                 cnt += 1
#     # 쁘린또
#     print(f'#{i+1} {cnt}')





# # 전기 빠스 강사님
# # 첫 번째 방법 갔다 충전소 없으면 뒤로 돌아가기
# def solve():
#     for i in range(M+2-1):
#         if STOPS[i+1] - STOPS[i] > K:
#             return 0
#     cur_pos = 0
#     cnt = 0
#     for i in range(1, M+2):
#         if cur_pos+K < STOPS[i]:
#             cnt += 1
#             cur_pos = STOPS[i-1]
#     return cnt
#
# T = int(input())
# for tc in range(1,T+1):
#     K, N, M = map(int, input().split())
#     STOPS = [0] + list(map(int, input().split()))
#     STOPS.append(N)
#
#     print(f'#{tc} {solve()}')
#     # print(STOPS)
