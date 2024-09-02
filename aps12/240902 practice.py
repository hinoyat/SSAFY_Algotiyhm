# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     dct = {}
#     lst = list(map(int, input().split()))
#     for i in range(N):
#         dct[lst[i]] = lst[i*2]
#
#     # print(dct)
#
#     for i in range(0, N-1):
#         left = lst[i]
#         right = lst[i+1]
#         print(left)
#         print(right)
#         mid = (left + right)/2
#         while left - right > 1/(10**12):
#             pass



# 주사위
# def KFC(cnt, result):
#     global ans
#     if result > 10:
#         return
#     if cnt == 3:
#         if result <= 10:
#             ans += 1
#         return
#     for i in range(1,  7):
#         KFC(cnt + 1, result + i)
#
#
# ans = 0
#
# KFC(0, 0)
# print(ans)


# # 순열
# def KFC(cnt, result):
#     if cnt == 5:
#         print(result)
#         return
#
#     for i in range(1, 5):
#         KFC(cnt + 1, result + str(i) +' ')
#
# KFC(0, '')



# # 카드 뽑기
# def counting(cards):
#     if cards[0] == cards[1] == cards[2]:
#         return 1
#     elif cards[1] == cards[2] == cards[3]:
#         return 1
#     elif cards[2] == cards[3] == cards[4]:
#         return 1
#     return 0
#
#
# def KFC(cnt, result):
#     global ans
#
#     if cnt == 5:
#         print(result)
#         ans += counting(result)
#         return
#
#     for i in range(len(lst)):
#         KFC(cnt + 1, result + lst[i])
#
# lst = ['A', "J", "Q", "K"]
# ans = 0
# KFC(0, '')
# print(ans)



def baby():
    pass

def gin():
    pass


T = list(map(int, input()))
ctlst = [0] * 10
print(T)

for i in T:
    ctlst[i] += 1

print(ctlst)
