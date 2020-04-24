'''
heapq 模块提供了堆排序算法的实现
-堆是二叉树，最大堆中父节点大于或等于两个子节点，最小堆父节点小于或等于两个子节点
heappush(heap,x) 将x压入堆中
heappop(heap) 从堆中弹出最小元素
heapify(heap) 让列表具有堆特性
heapreplace(heap,x) 弹出最小元素，并将x压入堆中
nlargest(n,iter) 返回iter中n个最大元素
nsmallest(n,iter)
'''
# import heapq
# nums = [12,8,10,5,36,4,32]
# heapq.heapify(nums)
# print(nums)
'''
使用堆序列对已经买入的股票进行统计
- 输出股价最高的两只股票
- 输出买入shares最多的两只股票
'''
import pandas as pd
import heapq
import numpy as np

def stock_analy(stock_info):
    maxprice = heapq.nlargest(2,list(map(float,stock_info['price'])))
    maxshare = heapq.nlargest(2,list(map(int,stock_info['shares'])))
    print(maxprice,maxshare)

    stock_info.index = stock_info['price']
    maxprice_comp = '、'.join(list(stock_info.loc[[str(p) for p in maxprice],'names']))
    print('股价最高的两只股票是：{}'.format(maxprice_comp))

    stock_info.index = stock_info['shares']
    maxshare_comp = '、'.join(list(stock_info.loc[[str(s) for s in maxshare],'names']))
    print('买入shares最多的两只股票是：{}'.format(maxshare_comp))

myStock = np.array([['MSFT',150,165.51],['FB',50,174.79],['YHOO',320,19.63],['IBM',100,121.15],['GOOG',75,1210.41]])
myStock = pd.DataFrame(myStock,columns=['names','shares','price'])

print(myStock)
stock_analy(myStock)
