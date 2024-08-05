# 고지식
t = 'TTTTTABC'
p = 'TTA'

N = len(t)
M = len(p)

for i in range(N-M+1):  # 비교 시작위치
    for j in range(M):
        if t[i + j] != p[j]:
            break   # 다음 글자부터 비교 시작
        else:
