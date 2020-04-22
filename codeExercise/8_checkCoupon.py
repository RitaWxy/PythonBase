'''
time datatime
'''
from datetime import datetime

def checkCoupon(entered_code,correct_code,current_time,expiration_time):
    '''
    查看优惠券是否有效
    :param entered_code: 输入的兑换码
    :param correct_code: 正确的兑换码
    :param current_time: 现在的时间
    :param expiration_time: 优惠券过期的时间
    :return: bool 是否有效
    '''

    current_ = datetime.strptime(current_time,'%B %d,%Y')
    expiration_ = datetime.strptime(expiration_time,'%B %d,%Y')
    return (entered_code == correct_code) and (current_ < expiration_)

print(checkCoupon('123','123','September 5,2014','October 1,2014'))
print(checkCoupon('123','12','September 5,2014','October 1,2014'))
print(checkCoupon('123','123','July 9,2015','July 2,2015'))