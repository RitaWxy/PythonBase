'''
列表解析式
print([i for i in range(11)])

生成器表达式[]改为()
'''
# res = [i for i in range(11)]
# obj = (i for i in range(1,6))
# print(res,type(res))
# print(obj,type(obj),'\n',list(obj))
'''
使用生成器表达式
（1）将联系15中价格大于150的股票构成一个新字典 
（2）将key与value对调
'''

import numpy as np
import pandas as pd
#
myStock = np.array([['MSFT',150,165.51],['FB',50,174.79],['YHOO',320,19.63],['IBM',100,121.15],['GOOG',75,1210.41]])
myStock = pd.DataFrame(myStock,columns=['names','shares','price'])
#
# stocklist = list((i for i in myStock['price'] if float(i) >=150))
# myStock.index = myStock['price']
# namelist = list(myStock.loc[[i for i in stocklist],'names'])
# print(dict(zip(stocklist,namelist)))

stock = {key:val for key,val in tuple(zip(myStock['names'],myStock['price'])) if float(val)>150 }
print(stock)
print({key:val for val,key in stock.items()})