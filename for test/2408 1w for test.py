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
