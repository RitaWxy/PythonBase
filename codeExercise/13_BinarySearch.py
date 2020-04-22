'''
二分查找(折半查找)
要求列表中的元素按关键字有序排列
--step1：将表中间位置记录的关键字与查找关键字比较，如果相等则查找成功
--step2：否则利用中间位置记录将表分为前后两部分，若中间位置大于查找关键字，则进一步查找前一部分子列表，否则查后一部分列表
重复上面动作直到查找成功或直到子列表不存在，查找不成功
'''

def searchInsert(num : [int],target : int) -> int:
    '''
    求待插入的位置
    :param num: 搜索的列表
    :param target: 待插入的树
    :return: 待插入的位置
    '''
    # Solution 1
    # num.sort()
    # low = 0
    # high = len(num)-1
    # while low <= high:
    #     mid_index = (low+high)//2
    #     if num[mid_index] == target: return mid_index
    #     if target > num[mid_index]: low = mid_index+1
    #     if target < num[mid_index]: high = mid_index-1
    # return low

    # Solution2
    num_len = len(num)
    if num_len <= 1: return int(num_len == 1 and target > num[0])
    mid_index = num_len // 2
    if target == num[mid_index]: return mid_index
    if target < num[mid_index]: return searchInsert(num[:mid_index],target)
    return mid_index + searchInsert(num[mid_index:],target)

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))
print(searchInsert([1,3,5,6],0))
print(searchInsert([1,3,5,6,9],8))
