def reverW(s):
    '''
    逐个翻转字符
    :param s: string
    :return: reversed string
    '''
    s.strip()
    start = end = 0
    res = []
    while end < len(s):
            while end<len(s) and s[end] != ' ':
                    end += 1
                    continue
            res.insert(0,s[start:end])
            start = end = end+1

    return ' '.join(res)

# def reverseWords(s):
#     ‘'‘
#     给定一个字符串，逐个翻转字符串中的每个单词
#     '‘’
#     s = s.strip()
#     i = j = len(s) - 1
#     res = []
#     while i(res) >= 0:
#         while i  and s[i] != ' ': i -= 1
#         res.append(s[i + 1: j + 1])
#         while s[i] == ' ': i -= 1
#         j = i
#     return ' '.join
print(reverW('the sky is blue'))