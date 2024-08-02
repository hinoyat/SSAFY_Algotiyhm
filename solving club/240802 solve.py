from pprint import pprint

# # 4864. 문자열 비교
# test_case = int(input())
# for tc in range(1, test_case+1):
#     st1 = input()
#     st2 = input()
#
#     n = len(st1)
#     m = len(st2)
#
#     good = False
#     for i in range(m):
#         if st1 == st2[i:i+n]:
#             good = True
#
#     if good == True:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')


# # GNS
# test_case = int(input())
# for tc in range(1, test_case+1):
#
#     tc_num, tc_len = map(str, input().split())
#     n = int(tc_len)
#
#     GNS = list(input().split())
#     GNS_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
#     GNS_key = list(GNS_dict.keys())
#     GNS_len = len(GNS)
#     for i in GNS:
#         if i in GNS_key:
#             GNS_dict[i] += 1
#
#     # print(GNS_dict)
#     print(f'{tc_num}')
#     for j in GNS_key:
#         for f in range(GNS_dict[j]):
#             print(f'{j}', end=' ')
#         print()
#     print()

# # 카운트 정렬
# test_case = int(input())
#
# for tc in range(1, test_case+1):
#     str1 = input()
#     str2 = input()
#     max = -21e8
#     for i in str1:
#         cnt = 0
#         for j in str2:
#             if i == j:
#                 cnt +=1
#         if cnt >= max:
#             max = cnt
#     print(f'#{tc} {max}')
# # # Version 2 딕셔너리 활용
# test_case = int(input())
#
# for tc in range(1, test_case+1):
#     str1 = input()
#     str2 = input()
#     dict = {}
#     for i in str2:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     # print(dict)
#     max = -21e8
#     for s in str1:
#         if s in dict:
#             if dict[s] >= max:
#                 max = dict[s]
#
#     print(f'#{tc} {max}')











# ################## # 4861 회문  다음주에 해
# test_case = int(input())
# for tc in range(1, test_case+1):
#     n, m = map(int, input().split())
#     arr = [[] for _ in range(n)]
#     for s in range(n):
#         st = input()
#         arr[s] = st
#     # pprint(arr)
#     # 행 열 확인
#
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j:j+m] == arr[i][j:j+m:-1]:
#                 print(arr[i][j:j+m])

