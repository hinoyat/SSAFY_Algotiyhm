def hextobin(c):
    if c.isdigit():
        value = int(c)
    else:
        value = ord(c) - ord('A') + 10

    result = ''
    for i in range(4):
        if (value >> i) & 1:
            result = '1' + result
        else:
            result = '0' + result
    return result

def bintodec(s):

    value = 0
    for c in s:
        value = value*2 + int(c)
    return value


'''
i번쨰 2진수 값을 0을 1로 1을 0으로
b[i] = (b[i] + 1) % 2


i번쨰 3진수 값을
0 -> 1, 2
1 -> 2, 0
2 -> 0, 1
t[i] = t[i]+1 % 3
'''