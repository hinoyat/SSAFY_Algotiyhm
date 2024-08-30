# def change(code):
#     global visited
#     code = code
#     end_point = 8
#     for i in range(len(code)-1, -1, -1):
#         result = []
#         if code[i] != '0' and visited[i] == 0:
#             start_point = i
#             cnt = 0
#             chan = 0
#             ceck = [0, 0, 0]
#             while cnt < end_point:
#                 visited[start_point] = 1
#                 if ceck[1] == 0 and ceck[2] == 0 and code[start_point] == '1':
#                     ceck[0] += 1
#                 elif ceck[0] != 0 and ceck[2] == 0 and code[start_point] == '0':
#                     ceck[1] += 1
#                 elif ceck[0] != 0 and ceck[1] != 0 and code[start_point] == '1':
#                     ceck[2] += 1
#                 elif ceck[2] != 0 and code[start_point] == '0':
#                     for c in range(3):
#                         ceck[c] = ceck[c] // min(ceck)
#                         c = str(ceck)
#                         result.append(dct2[c])
#                         cnt += 1
#                         ceck = [0, 0, 0]
#                 start_point -= 1
#     return result
#
#
#
#
#
#
# dct1 = {'0': '0000',
#         '1': '0001',
#         '2': '0010',
#         '3': '0011',
#         '4': '0100',
#         '5': '0101',
#         '6': '0110',
#         '7': '0111',
#         '8': '1000',
#         '9': '1001',
#         'A': '1010',
#         'B': '1011',
#         'C': '1100',
#         'D': '1101',
#         'E': '1110',
#         'F': '1111'
#         }
# dct2 = {'[2, 1, 1]': 0,
#         '[2, 2, 1]': 1,
#         '[1, 2, 2]': 2,
#         '[4, 1, 1]': 3,
#         '[1, 3, 2]': 4,
#         '[2, 3, 1]': 5,
#         '[1, 1, 4]': 6,
#         '[3, 1, 2]': 7,
#         '[2, 1, 3]': 8,
#         '[1, 1, 2]': 9,
#         }
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(input() for _ in range(N))
#
#     arr = set(arr)
#     arr = list(arr)
#     s = len(arr)
#     arr2 = []
#
#     for i in range(s):
#         if arr[i] != '0'*M:
#             arr2.append(list(arr[i]))
#     print(arr2)
#
#     e_jin = []
#     for i in arr2:
#         r = ''
#         for j in range(len(i)):
#             r += dct1[i[j]]
#         e_jin.append(r)
#
#     sum_val = 0
#
#     print(e_jin)
#     for i in e_jin:
#         visited = [0] * len(i)
#         print(change(i))


# def decode_pattern(code):
#     global visited
#     end_point = 8
#     result = []
#     for i in range(len(code) - 1, -1, -1):
#         if code[i] != '0' and not visited[i]:
#             start_point = i
#             pattern = [0, 0, 0]
#             count = 0
#             while count < end_point and start_point >= 0:
#                 visited[start_point] = True
#                 if pattern[1] == 0 and pattern[2] == 0 and code[start_point] == '1':
#                     pattern[0] += 1
#                 elif pattern[0] != 0 and pattern[2] == 0 and code[start_point] == '0':
#                     pattern[1] += 1
#                 elif pattern[0] != 0 and pattern[1] != 0 and code[start_point] == '1':
#                     pattern[2] += 1
#                 elif pattern[2] != 0 and code[start_point] == '0':
#                     min_value = min(p for p in pattern if p != 0)
#                     normalized_pattern = [p // min_value for p in pattern]
#                     pattern_key = str(normalized_pattern)
#                     if pattern_key in dct2:
#                         result.append(dct2[pattern_key])
#                         count += 1
#                         pattern = [0, 0, 0]
#                 start_point -= 1
#     return result[::-1]  # Reverse the result to get the correct order
#
#
# dct1 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#         '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#         'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
#
# dct2 = {'[2, 1, 1]': 0, '[2, 2, 1]': 1, '[1, 2, 2]': 2, '[4, 1, 1]': 3,
#         '[1, 3, 2]': 4, '[2, 3, 1]': 5, '[1, 1, 4]': 6, '[3, 1, 2]': 7,
#         '[2, 1, 3]': 8, '[1, 1, 2]': 9}
#
#
# def hex_to_binary(hex_string):
#     return ''.join(dct1[char] for char in hex_string)
#
#
# def process_testcase():
#     N, M = map(int, input().split())
#     arr = set(input().strip() for _ in range(N))
#     arr = [row for row in arr if row != '0' * M]
#
#     binary_codes = [hex_to_binary(row) for row in arr]
#
#     results = []
#     for code in binary_codes:
#         global visited
#         visited = [False] * len(code)
#         decoded = decode_pattern(code)
#         if decoded:
#             results.append(sum(decoded))
#
#     return sum(set(results))  # Sum of unique decoded values
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     result = process_testcase()
#     print(f"#{tc} {result}")

# # # 진짜 정답
# import sys
# sys.stdin = open("input.txt", "r")
# 
# dct1 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#         '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#         'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
# 
# dct2 = {'[2, 1, 1]': 0, '[2, 2, 1]': 1, '[1, 2, 2]': 2, '[4, 1, 1]': 3,
#         '[1, 3, 2]': 4, '[2, 3, 1]': 5, '[1, 1, 4]': 6, '[3, 1, 2]': 7,
#         '[2, 1, 3]': 8, '[1, 1, 2]': 9}
# 
# T = int(input().strip())
# for tc in range(1, T+1):
#     N, M = map(int, input().strip().split())
#     arr = list(input().strip() for _ in range(N))
# 
#     arr = set(arr)
#     arr = list(arr)
#     s = len(arr)
#     arr2 = []
# 
#     for i in range(s):
#         if arr[i] != '0'*M:
#             arr2.append(list(arr[i]))
#     # print(arr2)
# 
#     e_jin = []
#     for i in arr2:
#         r = ''
#         for j in range(len(i)):
#             r += dct1[i[j]]
#         e_jin.append(r)
# 
#     sum_val = 0
#     result = []
#     for i in e_jin:
#         c1 = 0
#         c2 = 0
#         c3 = 0
#         for j in range(len(i)-1, -1, -1):
#             # print(c1, c2, c3)
#             if c2 == 0 and c3 == 0 and i[j] == '1':
#                 c1 += 1
#             elif c1 != 0 and c3 == 0 and i[j] == '0':
#                 c2 += 1
#             elif c1 != 0 and c2 != 0 and i[j] == '1':
#                 c3 += 1
#             elif c3 != 0 and i[j] == '0':
#                 ceck = [c3, c2, c1]
#                 s = min(ceck)
#                 for c in range(3):
#                     ceck[c] = ceck[c] // s
#                 c = str(ceck)
#                 # print(c)
#                 result.append(dct2[c])
#                 c1 = 0
#                 c2 = 0
#                 c3 = 0
#     result.reverse()
#     # print(result)
#     # print(e_jin)
#     real_result = []
#     check = []
#     for r in range(0, len(result), 8):
#         code = str(result[r]) + str(result[r+2]) + str(result[r+4]) + str(result[r+6]) + str(result[r+1]) + str(result[r+3]) + str(result[r+5]) + str(result[r+7])
#         if code in check:
#             pass
#         else:
#             check.append(code)
#             if (((result[r] + result[r+2] + result[r+4] + result[r+6]) * 3) + (result[r+1] + result[r+3] + result[r+5] + result[r+7])) % 10 == 0:
#                 real_result.append(result[r] + result[r+2] + result[r+4] + result[r+6] + result[r+1] + result[r+3] + result[r+5] + result[r+7])
# 
# 
#     print(f'#{tc} {sum(real_result)}')
#     # print(result)














# '''
# i번쨰 2진수 값을 0을 1로 1을 0으로
# b[i] = (b[i] + 1) % 2
#
#
# i번쨰 3진수 값을
# 0 -> 1, 2
# 1 -> 2, 0
# 2 -> 0, 1
# t[i] = t[i]+1 % 3
# '''
# # 정식이의 은행업무
#
#
# def change2(lst):
#     result = 0
#     for i in range(len(lst)-1, -1, -1):
#         result += (2**((len(lst) - i - 1))*lst[i])
#     return result
#
# def change3(lst):
#     result = 0
#     for i in range(len(lst)-1, -1, -1):
#         result += (3**((len(lst) - i - 1))*lst[i])
#     return result
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     ezin = list(map(int, input()))
#     samzin = list(map(int, input()))
#     # print(ezin)
#     # print(samzin)
#
#     result = 0
#     for i in range(len(ezin)):
#
#         ezin[i] = (1 + ezin[i]) % 2
#         check_e = change2(ezin)
#
#         for j in range(len(samzin)):
#             for _ in range(2):
#                 samzin[j] = (samzin[j] + 1) % 3
#                 check_sam = change3(samzin)
#                 # print(samzin)
#             # 원복
#
#                 if check_e == check_sam:
#                     result = check_sam
#                     break
#             samzin[j] = (samzin[j] + 1) % 3
#             if result != 0:
#                 break
#         if result != 0:
#             break
#
#         # 원복
#         ezin[i] = (1 + ezin[i]) % 2
#
#     print(f'#{tc} {result}')


# 이진수 표현
def Turn(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'

    if num % 2 == 0:
        return Turn(num//2) + '0'
    else:
        return Turn(num//2) + '1'


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ezin = Turn(int(M))
    pos = 'ON'
    cnt = 0
    if len(ezin) < N:
        pos = 'OFF'
    else:
        for i in range(len(ezin)-1, -1, -1):
            cnt += 1
            if cnt > N:
                break
            else:
                if ezin[i] == '0':
                    pos = 'OFF'


    print(f'#{tc} {pos}')