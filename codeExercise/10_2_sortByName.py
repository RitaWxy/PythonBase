'''
numpy里的排序

'''

import numpy as np

def sort_by_name(dig_list):
    '''
    数字的英文字母排序
    【1，2，3】对应英文【one，two，three】
    按照英文字母排序，函数返回【1，3，2】
    :param dig_list: 输入的范围为0-999，可以重复
    :return: 按照英文字母排序后的数列
    '''

    # Solution 1
    # name_list = [trans_eng(i) for i in dig_list]
    # numdict = dict(zip(name_list,dig_list))
    # name_list = np.sort(name_list)
    # return [numdict[i] for i in name_list]

    # Solution 2
    eng_list = [trans_eng(i) for i in dig_list]
    arr = np.array([eng_list,dig_list]).T
    print(arr)
    arr = sorted(arr,key=lambda x:x[0])
    print(arr)
    return [r[1] for r in arr]



def trans_eng(num:int):

    nameDic1 = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',\
                11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',\
                18:'eighteen',19:'nineteen'}
    nameDic2 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'niney'}

    if num<0 or num>999 or not isinstance(num,int): return 'Error.'
    # 一位数
    if 0<= num <=9 : name = nameDic1[num]
    # 两位数转化
    def trans_twodig(num_2):
        if 10 <= num_2 <= 19: name_2 = nameDic1[num_2]
        if 20<=num_2<=99 : name_2 = nameDic2[num_2//10]+' '+nameDic1[num_2%10] if num_2%10 !=0 else nameDic2[num_2//10]
        return name_2

    if 10<= num <=99: name = trans_twodig(num)

    if 100<= num <=999 : name = nameDic1[num//100]+' hundred' + trans_twodig(num%100)
    return name


print(sort_by_name([1,2,3,4])) #[4,1,3,2]
print(sort_by_name([9,99,999])) #[9,99,999]
print(sort_by_name([8,8,9,9,10,10])) #【8，8，9，9，10，10】