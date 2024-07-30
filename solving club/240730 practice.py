# # Flatten
# test_case = 10
#
# for i in range(test_case):
#     n = int(input())
#     box_lst = list(map(int, input().split()))
#     # n 번동안 반복 작업
#     for _ in range(n):
#         # max = 0
#         # min = 1e9
#         # for j in box_lst:
#         #     if j >= max:
#         #         max = j
#         #     if j < min:
#         #         min = j
#         max_val = max(box_lst)
#         min_val = min(box_lst)
#         for d in range(len(box_lst)):
#             if box_lst[d] == min_val:
#                 box_lst[d] += 1
#                 break
#         for s in range(len(box_lst)):
#             if box_lst[s] == max_val:
#                 box_lst[s] -= 1
#                 break
#
#     # print(min_val,max_val)'
#     # print(f'#{i+1} {max_val-min_val}')
#     real_max = max(box_lst)
#     real_min = min(box_lst)
#     print(f'#{i + 1} {real_max - real_min}')


# Flatten 2
# test_case = 10
#
# for i in range(test_case):
#     n = int(input())
#     box_lst = list(map(int, input().split()))
#     # n 번동안 반복 작업
#     for _ in range(n):
#         max_value = 0
#         min_value = 1e9
#         for j in box_lst:
#             if j >= max_value:
#                 max_value = j
#             if j < min_value:
#                 min_value = j
#
#         for d in range(len(box_lst)):
#             if box_lst[d] == min_value:
#                 box_lst[d] += 1
#                 break
#         for s in range(len(box_lst)):
#             if box_lst[s] == max_value:
#                 box_lst[s] -= 1
#                 break
#
#     # print(min_val,max_val)'
#     # print(f'#{i+1} {max_val-min_val}')
#     real_max = max(box_lst)
#     real_min = min(box_lst)
#     print(f'#{i + 1} {real_max - real_min}')


# # 4834 숫자카드
# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input()))
#     counts = [0] * 10
#     # print(a, n)
#     for x in a:
#         counts[x] += 1
#
#     max_num = 0
#     for s in counts:
#         if s >= max_num:
#             max_num = s
#     # print(counts)
#
#     many_num = []
#
#     for num in range(len(counts)):
#         if counts[num] == max_num:
#             many_num.append(num)
#
#     # print(many_num)
#     real_num = many_num[len(many_num)-1]
#     # print(real_num)
#
#     print(f'#{i+1} {real_num} {counts[real_num]}')

# # 9486 연속한 1의 개수
# testcase = int(input())

# for tc in range(1, testcase+1):
#     n = int(input())
#     num_lst = list(map(int,input())) + [0]
#     # print(num_lst)
#     max_1 = []
#     cnt = 0
#     for i in range(n+1):
#         if num_lst[i] == 1:
#             cnt += 1
#         else:
#             max_1.append(cnt)
#             cnt = 0
#     # print(max_1)
#     max_val = 0
#     for val in max_1:
#         if val >= max_val:
#             max_val = val
#     print(f'#{tc} {max_val}')


# # 1945 간단한 소인수 분해


# test_case = int(input())
# num_lst = [2, 3, 5, 7, 11]
# for tc in range(1, test_case+1):
#     num = int(input())

#     val = []
#     num_lst_idx = 0
#     num_val = num
#     cnt = 0

#     while num >0:
#         if num_lst_idx > 4:
#             break
#         if num % num_lst[num_lst_idx] == 0: 
#             num //= num_lst[num_lst_idx]
#             cnt +=1
#         else:
#             val.append(cnt)
#             num_lst_idx += 1
#             cnt = 0
#     print(f'#{tc}', end=' ')
#     print(*val)

# # 6845 삼성시의 빠스 노선
# # Ai <= 버스i <= Bi  각 정류장에 몇개의 노선이 다니는지
# # 정류장은 P개
# # 테스트 케이스 N
# # i번째 줄에 Ai Bi 주어진다(공백)
# # 정수 P가 주어진다
# # P개의 줄의 j번쨰는 Cj
# test_case = int(input())

# for tc in range(1, test_case+1):
#     N = int(input())
#     # 인덱스는 0부터 아니라 1부터 하면ㄷ ㅐ 첫번째는 더미
#     bus_stop = [0] * 5001
#     # 버스 정류장 리스트에 a[0]=> 1 부터 b[0]=> (3 +1) 까지 1추가
#     # 버스 정류장 리스트에 a[1]=> 2 부터 b[1]=> (5 +1) 까지 1추가
#     a_lst = []
#     b_lst = []
#     # 받은 a와 b 값을 각각 a_lst b_lst에 올려준다
#     # 왜냐하면 나중에 for문 돌릴때 한 값으로 처리하기 위해서!
#     for _ in range(N):
#         a, b = map(int,input().split())
#         a_lst.append(a)
#         b_lst.append(b)
#     # 여기서! 한 i 값으로 bus_stop의 인덱스 a ~ b 까지의 값을 늘릴 수 있어요 
#     for i in range(N):
#         for j in range(a_lst[i], b_lst[i]+1):
#             bus_stop[j]+=1
    
#     # print(a_lst,b_lst)
    
#     bus_stop_idx = []
#     # P는 정류장의 인덱스 수
#     P = int(input())
#     for _ in range(P):
#         # s는 정류장의 번호
#         s = int(input())
#         bus_stop_idx.append(s)
#     # print(bus_stop_idx)
#     print(f'#{tc}',end=' ')
#     for bus in bus_stop_idx:
#         print(f'{bus_stop[bus]}',end=' ')
#     # 첫 제출 때 틀렸던 이유가 이 아래 프린트가 없어서인 것 같아요
#     print()