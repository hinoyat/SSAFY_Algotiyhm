# def merge_sort(arr):
#
#     n = len(arr)
#
#     if n <= 1:
#         return arr
#
#     mid = n // 2
#
#     left_arr = arr[:mid]
#     right_arr = arr[mid:]
#     print(f' 분할 전: {left_arr, right_arr}')
#
#     left_arr = merge_sort(left_arr)
#     right_arr = merge_sort(right_arr)
#
#     print(f' 분할 후: {left_arr, right_arr}')
#
#     return merge(left_arr, right_arr)
#
#
# def merge(left, right):
#     result = []
#     left_idx, right_idx = 0, 0
#     # print(left, right)
#     while left_idx < len(left) and right_idx < len(right):
#         if left[left_idx] < right[right_idx]:
#             result.append(left[left_idx])
#             left_idx += 1
#         else:
#             result.append(right[right_idx])
#             right_idx += 1
#
#     result.extend(left[left_idx:])
#     result.extend(right[right_idx:])
#     print(result)
#
#     return result
#
# lst = [1, 3, 4, 2, 6, 9]
# result = merge_sort(lst)

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     A.sort()
#     ans = 0
#     for i in range(M):
#         key = B[i]
#         start = 0
#         end = N - 1
#         moving = 0
#         find = False
#
#         while start <= end:
#             mid = (start + end) //2
#             if A[mid] == key:
#                 ans += 1
#                 break
#
#             elif A[mid] < key:
#                 if moving == 1:
#                     break
#                 else:
#                     moving = 1
#                     start = mid + 1
#
#             elif A[mid] > key:
#                 if moving == 2:
#                     break
#                 else:
#                     end = mid - 1
#                     moving = 2
#     print(f'#{tc} {ans}')

def quick_sort(arr, start, end):
    # start <= end 이면 배열의 길이가 0이거나 1이라는 소리 == 필요 없다
    if start < end: # len(arr) > 1
        pivot = partition(arr, start, end)

        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    # 피벗은 가장 왼쪽
    pivot = arr[start]
    left = start + 1
    right = end
    while True:
        # left는 피벗보다 큰 값을 탐지해야 한다
        # 작은 값을 만나면 앞으로 보낸다
        while left <= end and arr[left] < pivot:
            left += 1

        while right > start and arr[right] >= pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[start], arr[right] = arr[right], arr[start]

    return right

# import sys
# sys.stdin = open("input.txt", "r")

arr = list(map(int, input().split()))

quick_sort(arr, 0, len(arr) - 1)
print(arr[500000])
