# 바이너리 카운팅

arr = [1, 2, 3]
n = len(arr)
subset_cnt = 1 << n
subsets = []
for i in range(subset_cnt):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])

    subsets.append(subset)
print(subsets)

