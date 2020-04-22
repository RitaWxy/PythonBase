import re

def numJewInStones(J:str,S:str):
    '''
    区分大小写
    :param J: 拥有的宝石，每个字母都是一种宝石，J中字母不重复
    :param S: 石头堆
    :return: S里拥有的宝石的个数
    '''
    pattern = str([J])
    # pattern = r'[J]' ×错
    return len(re.findall(pattern,S))

print(numJewInStones('aA','aAAAbbb'))
print(numJewInStones('z','ZZZ'))
print(numJewInStones('abcd','AAbCC'))