'''
寻找输入字符串的最长回文字符串
'''

# Solution 1
# def is_palindrome(substr):
#     i = 0
#     j = len(substr) - 1
#     while i <= j:
#         if substr[i] != substr[j]: return False
#         i += 1
#         j -= 1
#     return True
#
# def longest_palindrome(str):
#     pald = {}
#     for i in range(len(str)):
#         j = str.find(str[i],i+1)
#         if j == -1: continue
#         substr = str[i:j+1]
#         if not is_palindrome(substr): continue
#         pald[substr] = len(substr)
#     if pald == {} : return 1
#     return max(list(pald.values()))

# Solution 2 [::-1]方法
# def longest_palindrome(s):
#     res = 1
#     for i in range(len(s)):
#         # for j in range(i,len(s)):
#         #     temp1 = s[i:j+1]
#         #     temp2 = temp1[::-1]
#         #     if temp1 == temp2 and len(temp1)>res:
#         #         res = len(temp1)
#         j = s.find(s[i],i+1)
#         if j == -1: continue
#         temp = s[i:j+1]
#         if temp == temp[::-1]: res = max(res,len(temp))
#     return res

# print(longest_palindrome('ab'))
# print(longest_palindrome('aa'))
# print(longest_palindrome('baa'))
# print(longest_palindrome('aab'))
# print(longest_palindrome('abcdefghba'))
# print(longest_palindrome('baablkj12345432133d'))

# Solution 3
def is_palidrom(string): return (string == string[::-1] and string)

def longest_palindrome_from_begin(string):
    for i in range(len(string)):
        if is_palidrom(string[:len(string)-i]): return string[:len(string)-i]
    return ' '

def longest_palindrome(string):
    return max([longest_palindrome_from_begin(string[i:]) for i in range(len(string))], key=len)

assert is_palidrom('a')
assert not is_palidrom('')
assert is_palidrom('aba')
assert not is_palidrom('abad')
assert longest_palindrome_from_begin('abc') == 'a'
assert longest_palindrome_from_begin('aba') == 'aba'
# print(longest_palindrome('ab'))
# print(longest_palindrome('aa'))
# print(longest_palindrome('baa'))
# print(longest_palindrome('aab'))
# print(longest_palindrome('abcdefghba'))
# print(longest_palindrome('baablkj12345432133d'))










