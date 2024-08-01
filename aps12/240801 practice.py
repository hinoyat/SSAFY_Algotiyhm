# # 순차 검색(정렬 O)
# key = 2
# lst = [4, 9, 11, 23, 2, 19, 7]
# n = len(lst)
# i = 0
# while i < n:
#     if lst[i] == key:
#         print(f'#내가 만든 코드 : {i}')
#         break
#     else:
#         if i == (n-1):
#             print('실패')
#             break
#         else:
#             i += 1
# # 강의 구현
#
# key = 2
# lst = [4, 9, 11, 23, 2, 19, 7]
# n = len(lst)
#
# def seq(lst, n, key):
#     i = 0
#     while i < n and lst[i] != key:
#         i += 1
#     if i < n:
#         return i
#     else:
#         return -1
# print(f'#강의 : {seq(lst,n,key)}')

# 이진 검색 알고리즘
'''
검색 번위의 시작점과 종료점을 이용하여 검색 수행
자료의 삽입 or 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지해야 한다
'''

## 달팽이 연습문제
arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

n = 5
dst = [[0]*5 for _ in range(n)]

row = 0
col = 0

# 델타 잡기
# 우 하 좌 상
dr = [0, 1, 0, -1] # 하 상
dc = [1, 0, -1, 0] # 우 좌

k = 0

for i in range(n*n):
    value = getmin()  # 제일 작은 값을 찾거나 그다음 작은 값을 찾으세여어~
    dst[row][col] = value
    newR = row + dr[k]
    newC = col + dc[k]
    if :   # 변을 만나거나 이미 값이 있으면
        # k+=1
        # if k == 4:
        #     k = 0
        k = (k+1) % 4

    row = row + dr[k]
    col = col + dc[k]