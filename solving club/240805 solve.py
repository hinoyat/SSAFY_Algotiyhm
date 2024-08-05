# # 빠르게 강사님
# test = 1
# pattern = 1
# ip = jp = 0
# while ip<len(test) and jp<len(pattern):
#     if test[ip] == pattern[jp]:
#         ip += 1
#         jp += 1
#     else:
#         ip = ip - jp +1
#         jp = 0

#     # if test[ip != pattern
#     #     ip = ip - jp
#     #     jp = -1
#     #
#     # else:
#     #     ip += 1
#     #     jp +=1

# if jp ==len(pattern):





# # 빠르게 입력하기
# test_case = int(input())
# for tc in range(1, test_case+1):
#     A, B = input().split()
#     A = list(A)
#     n = len(B)
#     cnt = 0
#     for i in range(len(A)):
#         if A[i:i+n] == B:
#             cnt +=1
#
#     print(cnt)
#
#     result = len(A) - (len(B) * cnt) + cnt
#     print(f'#{tc} {result}')

# # 빠르게 입력하기
# test_case = int(input())
# for tc in range(1, test_case+1):
#     A, B = input().split()
#     A = list(A)
#     B = list(B)
#     n = len(B)
#     cnt = 0
#     for i in range(len(A)):
#         if A[i:i+n] == B:
#             A[i:i+n] = ''
#             cnt +=1
#     for i in range(len(A)):
#         if A[i:i+n] == B:
#             A[i:i+n] = ''
#             cnt +=1
#     print(A)
#     print(cnt)
#
#     result = len(A) + cnt
#     print(f'#{tc} {result}')




# # 빠르게 입력하기
# test_case = int(input())
# for tc in range(1, test_case+1):
#     A, B = input().split()
#
#     cnt = 0
#     i = 0
#     n = len(B)
#     while i <= len(A)- n:
#         if A[i:i+n] == B:
#             cnt += 1
#             i += n
#
#         else:
#             i += 1
#
#
#     # print(A)
#     # print(cnt)
#
#     result = len(A) - (n * cnt) + cnt
#     print(f'#{tc} {result}')


# 회문 2
# test_case = 10
# for _ in range(test_case):
#     tc = int(input())
#     arr = [[0 for _ in range(100)]for _ in range(100)]
#
#     for i in range(100):
#         ar = input()
#         for j in range(100):
#             arr[i][j] = ar[j]
#
#
#     max_a = 0

# for i in range(100):
#     for j in range(100):
#         abcba = 1
#         n = 1
#         abba = 0
#         m = 0
#
#
#         while 0<= (j - n) and (j+n)<100:
#             if arr[i][j-n] == arr[i][j+n]:
#                 abcba += 2
#             else:
#                 abcba = 1
#                 break
#
#             n += 1
#         if abcba > max_a:
#             max_a = abcba
#
#
#         while 0<= (j - m) and (j+m+1) < 100:
#             if arr[i][j-m] == arr[i][j+m+1]:
#                 abba += 2
#             else:
#                 abba = 0
#                 break
#             m += 1
#         if abba > max_a:
#             max_a = abba
#
#
# for j in range(100):
#     for i in range(100):
#         abcba = 1
#         n = 1
#         abba = 0
#         m = 0
#
#
#         while 0<= (j - n) and (j+n)<100:
#             if arr[j-n][i] == arr[j+n][i]:
#                 abcba += 2
#             else:
#                 abcba = 1
#                 break
#
#             n += 1
#         if abcba > max_a:
#             max_a = abcba
#
#
#         while 0<= (j - m) and (j+m+1) < 100:
#             if arr[j-m][i] == arr[j+m+1][i]:
#                 abba += 2
#             else:
#                 abba = 0
#                 break
#             m += 1
#         if abba > max_a:
#             max_a = abba
#
#

# print(f'#{tc} {max_a}')



# # 회문 2 2222222222222
# test_case = 10
# for _ in range(test_case):
#     tc = int(input())
#     arr = [input() for _ in range(100)]
#
#     max_len = 0
#     # 행
#     for i in range(100):
#         for j in range(100):
#             abcba = 1
#             n = 1
#             # 홀
#             while True:
#                 if 0 <= j-n and j+n < 100:
#                     if arr[i][j-n] == arr[i][j+n]:
#                         abcba +=2
#                         n+=1
#                     else:
#                         break
#                 else:
#                     break
#             if abcba >= max_len:
#                 max_len = abcba
#             abba = 0
#             n = 0
#             # 홀
#             while True:
#                 if 0 <= j-n and j+n+1 < 100:
#                     if arr[i][j-n] == arr[i][j+n+1]:
#                         abba += 2
#                         n += 1
#                     else:
#                         break
#                 else:
#                     break
#             if abba >= max_len:
#                 max_len = abba
#
#     for i in range(100):
#         for j in range(100):
#             abcba = 1
#             n = 1
#             # 홀
#             while True:
#                 if 0 <= j-n and j+n < 100:
#                     if arr[j-n][i] == arr[j+n][i]:
#                         abcba +=2
#                         n+=1
#                     else:
#                         break
#                 else:
#                     break
#             if abcba >= max_len:
#                 max_len = abcba
#             abba = 0
#             n = 0
#             # 홀
#             while True:
#                 if 0 <= j-n and j+n+1 < 100:
#                     if arr[j-n][i] == arr[j+n+1][i]:
#                         abba += 2
#                         n += 1
#                     else:
#                         break
#                 else:
#                     break
#             if abba >= max_len:
#                 max_len = abba
#
#
#
#
#
#     print(f'#{tc} {max_len}')


# # 회문 1
# test_case = int(input())
# for tc in range(1, test_case+1):
#     # M은 펠린드롬
#     lst = []
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]

#     for i in range(N):
#         for j in range(N-M+1):
#             word_r = arr[i][j:j+M]
#             if word_r == word_r[::-1]:
#                 lst.append(word_r)

#     for i in range(N):
#         for j in range(0, N-M+1):
#             word = ''
#             for s in range(M):
#                 word += arr[j+s][i]
            
#             if word == word[::-1]:
#                 lst.append(word)


#     print(f'#{tc}', end=' ')
#     print(*lst)
