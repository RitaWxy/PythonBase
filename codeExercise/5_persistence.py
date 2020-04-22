 #def persistence(ipnum):
#         numLen = len(list(ipnum))
#         count = 0
#         while True:
#                 if numLen == 1:
#                         break
#                 num = 1
#                 for i in range(numLen):
#                        num = (lambda x:x*int(ipnum[i]))(num)
#                 count += 1
#                 ipnum = list(str(num))
#                 numLen = len(ipnum)
#         return count
# while True:
#         myNum = input('Please input a number:')
#         con = persistence(myNum)
#         print('{}-->{}'.format(myNum,con))
#         qui = input("If Quit,press 'Y':")
#         if qui == 'Y':
#                 break

def persistence(num,count=0):
        '''
        数字相乘的次数，eg. 39--> 3*9=27 --> 2*7=14 -->1*4=4, count = 3
        :param num: a positive num
        :param count: times of mulplication
        :return:
        '''
        if num<10:
                return count
        last_dig = 1
        while num:
                last_dig *= num % 10 # 从后往前取，先取出末尾相乘
                num = num // 10 # 除末尾以外
        count += 1
        return persistence(last_dig,count)

print('{}-->{}'.format(39,persistence(39)))
print('{}-->{}'.format(999,persistence(999)))
print('{}-->{}'.format(4,persistence(4)))
print('{}-->{}'.format(28,persistence(28)))