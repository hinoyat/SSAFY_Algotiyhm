T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dct = {}
    lst = list(map(int, input().split()))
    for i in range(N):
        dct[lst[i]] = lst[i*2]

    # print(dct)

    for i in range(0, N-1):
        left = lst[i]
        right = lst[i+1]
        print(left)
        print(right)
        mid = (left + right)/2
        while left - right > 1/(10**12):
            pass    