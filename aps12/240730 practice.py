# # 버블 정령 시간 복잡도 O(n2)
# lst_a = list(map(int, input().split()))
# N = len(lst_a)
#
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if lst_a[j] > lst_a[j+1]:
#             lst_a[j], lst_a[j+1] = lst_a[j+1], lst_a[j]
#
# print(lst_a)

# 4835 구간합 문제에서 음수도 있다면




# #카운팅 정렬
# n = int(input('최댓값을 입력하시오'))  # n은 최댓값 입력
# data = list(map(int, input().split()))
# counts = [0] * (n+1)
#
# # print(counts)
# # 1 단계 0부터 n까지 데이터를 돌면서 몇 개 있는지 센다
# for i in range(n+1):
#     for j in data:
#         if i == j:
#             counts[i] += 1
#
# print(counts)
# # 요기까지 각 수가 몇개씩 있는지
#
# # 2 단계 누적 합
# for s in range(1, len(counts)):
#     counts[s] += counts[s-1]
#
# print(counts)
#
# temp = [0] * len(data)
#
# # 정렬하기 ;;
#
# print(temp)
# for i in range (len(temp)-1, -1, -1):
#     counts[data[i]] -= 1
#     temp[counts[data[i]]] = data[i]
#
# print(temp)

# # 카운팅 정렬 (강사님)
# data = [0, 4, 1, 3, 1, 2, 4, 1]
# counts = [0] * 5
#
# n = len(data)
# temp = [0] * n
#
# # 1단계 : data 원소 별 개수 세기
# for x in data:
#     counts[x] += 1
#
# # 2단계 : 각 숫자까지의 누적 개수 구하기
# for i in range(1,5):
#     counts[i] = counts[i-1]+counts[i]
#
# # 3단계 data의 맨 뒤부터 temp에 자리잡기
# for i in range(n-1, -1, -1):
#     counts[data[i]] -= 1
#     temp[counts[data[i]]] = data[i]
# print(temp)



# #baby-gin 완전검색 내가 푸는 것
# t = input()
# 
# num_lst = []
# for i in t:
#     s = int(i)
#     num_lst.append(i)
# print(num_lst)
# 
# # n = len(num_lst)
#
# for i in range(n-1, 0, -1):
#     for j in range(i):
#         if num_lst[j] > num_lst[j+1]:
#             num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]

# baby-gin
data = list(map(int, input()))
print(data)
n = len(data)
counts = [0] * 12
for i in data:
    counts[i] += 1
print(counts)

a = 0
baby_gin = 0
while a < 10:
    if counts[a] >= 3:
        counts[a] -= 3
        baby_gin += 1
        continue

    if counts[a] >= 1 and counts[a+1] >= 1 and counts[a+2] >= 1:
        counts[a] -= 1
        counts[a+1] -= 1
        counts[a+2] -= 1
        baby_gin += 1
        continue
    a += 1
if baby_gin >= 2:
    print('babygin')
else:
    print('not gin')







# 탐욕 알고리즘