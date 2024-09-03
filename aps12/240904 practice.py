# def merge_sort(arr):
#     global cnt
#
#     n = len(arr)
#
#     if n <= 1:
#         return arr
#
#
#     mid = n//2
#     left_arr = arr[:mid]
#     right_arr = arr[mid:]
#
#     left_arr = merge_sort(left_arr)
#     right_arr = merge_sort(right_arr)
#
#     if left_arr[-1] > right_arr[-1]:
#         cnt += 1
#
#     return merge(left_arr, right_arr)
#
#
# def merge(left, right):
#     result = []
#
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#
#     # 왼쪽이 남은 경우
#
#     result.extend(left)
#     result.extend(right)
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     cnt = 0
#     N = int(input())
#     lst = list(map(int, input().split()))
#     result = merge_sort(lst)
#
#     print(f'#{tc} {result[N//2]} {cnt}')
from unittest.mock import right


#
# def merge_sort(arr):
#     global cnt
#
#     n = len(arr)
#
#     if n <= 1:
#         return arr
#
#     mid = n // 2
#     left_arr = arr[:mid]
#     right_arr = arr[mid:]
#
#     left_arr = merge_sort(left_arr)
#     right_arr = merge_sort(right_arr)
#
#     if left_arr[-1] > right_arr[-1]:
#         cnt += 1
#
#     return merge(left_arr, right_arr)
#
#
# def merge(left, right):
#     result = []
#     left_idx, right_idx = 0, 0
#
#     while left_idx < len(left) and right_idx < len(right):
#         if left[left_idx] < right[right_idx]:
#             result.append(left[left_idx])
#             left_idx += 1
#         else:
#             result.append(right[right_idx])
#             right_idx += 1
#
#     # 남아있는 요소 추가
#     result.extend(left[left_idx:])
#     result.extend(right[right_idx:])
#
#     return result
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     cnt = 0
#     N = int(input())
#     lst = list(map(int, input().split()))
#     result = merge_sort(lst)
#
#     print(f'#{tc} {result[N // 2]} {cnt}')


# 퀵 정렬

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
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr,0, len(arr) - 1)
    print(f'#{tc} {arr[N//2]}')
