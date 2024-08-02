# #r강사님이 보여주는 것
# import sys
# a = ''
# b = 'a'
# c = 'ab'
# d = 'abc'
#
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))


# s1 = list(input())
# s2 = input()
#
# print(s1)
# print(s2)


# # 문자열 비교
# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'

# print(chr(ord('A')))

# int 함수 만들기
# def atpoi(string):
#     i = 0
#     for x in string:
#         i = i*10 + ord(x) - ord('0')
#     return i
# 
# a = '132456'
# print(atpoi(a))
# print(type(atpoi(a)))

# itoa() 만들기
'''
힌드 a를 10으로 나눈 나머지 a//10  a%10 이용
'''

# def itoa(num):
#     result = ''
#     while num >0:
#         re = num % 10
#         re = chr(re + ord('0'))
#         num = num // 10
#         result = re + result
#     return result

    # return str(num)



number = 4567
number_s = itoa(number)
print(number_s)







# atoi잇
# def atoi(num):
#     result = 0
#     for c in num:
#         num = ord(c) - ord('0')
#         result = result * 10 * num
#     return result
#
# number_s = '4567'
# number = atoi(number_s)



# # 문자를 숫자로
# t = '1'
# newT = ord(t) - ord('0')
# print(newT, type(newT))
#
# # 숫자를 문자로
#
# newT2 = chr(newT+ord('0'))
# print(newT2, type(newT2))
#
#
# s = 'Reverse this strings'
#
# newS = ''
# for c in s:
#     newS = c+ newS
#
# for i in range(len(s)-1, -1, -1):
#     newS = newS +s[i]
# print(newS)
# newS = list(s)
# newS.reverse()
# newS = ' '.join(s)


# 문자열 비표 함수
'''
str1이 str2보다 사전 순서상 앞서면 -1 리턴
str1이 str2보다 사전 순서상 나중이면 1 리턴
'''
# def strcmp(st1, str2):
#     if st1 < str2:
#         return -1
#     else:
#         return  1
#
# print(strcmp('a','aa'))
# print(strcmp('aac','ab'))
# print(strcmp('aac','abc'))


# print('a'<'aa')
# print('a'>'ab')
