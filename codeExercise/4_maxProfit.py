def maxProfit(mystr):
    buy_day = mystr.index(min(mystr))
    if buy_day == (len(mystr)-1): return 0
    buy_val = maxNum = mystr[buy_day]
    for i in range(buy_day+1,len(mystr)):
        if mystr[i] > maxNum: maxNum = mystr[i]
    if maxNum <= buy_val: return 0
    return maxNum - buy_val

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

