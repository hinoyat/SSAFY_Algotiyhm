# def change(N):
#     r = ''
#     target = 0
#     try:
#         target = int(N)
#     except:
#         target = ord(N) - 55
#
#     for i in range(3, 0, -1):
#         if target // (2**i) == 1:
#             r += '1'
#             target %= (2**i)
#         else:
#             r += '0'
#
#     if target == 0:
#         r += '0'
#     else:
#         r += '1'
#
#     return r
#
# T = int(input())
# for tc in range(1, T + 1):
#     num_len, num = input().split()
#     result = []
#     for n in num:
#         result.append(change(n))
#     print(f'#{tc} {"".join(result)}')

# def change(num):
#     t = num
#     result = ''
#     zin = 1
#     while t != 0:
#         if t < 2 ** (-zin):
#             result += '0'
#         else:
#             t -= 2**(-zin)
#             result += '1'
#         if len(result) > 13:
#             return 'overflow'
#         zin += 1
#     return result
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     target = float(input())
#     r = change(target)
#     print(f'#{tc} {r}')



def cal(num_lst):
    odd = 0
    even = 0

    for i in range(0, len(num_lst), 2):
        odd += num_lst[i]
    for j in range(1, len(num_lst), 2):
        even += num_lst[j]

    result = odd + even
    if (odd*3 + even) % 10 == 0:
        return result
    else:
        return 0



def change(code):
    code_lst = []
    for i in range(0,len(code),7):
        code_lst.append(code[i:i+7])

    check = {'0001101':0,
             '0011001': 1,
             '0010011': 2,
             '0111101': 3,
             '0100011': 4,
             '0110001': 5,
             '0101111': 6,
             '0111011': 7,
             '0110111': 8,
             '0001011': 9
             }

    num_lst = [0] * 8
    for i in range(len(code_lst)):
        num_lst[i] = check[code_lst[i]]

    return cal(num_lst)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    end_p = 0
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == "1":
                end_p = arr[i][j-55 : j+1]
                break
        if end_p != 0:
            break
    # print(end_p)
    print(f'#{tc} {change(end_p)}')
