def Tribonacci(signature,n):
    '''
    广义菲波那切数列
    :param signature: 输入数列前三个
    :param n: 数列个数
    :return: 广义菲波那切数列
    '''
    if not signature[0] == signature[1] == signature[2] or n<3: return []
    # Solution 1
    # for i in range(3,n):
    #     signature.append(sum(signature[i-3:i]))
    # return signature

    # Solution 2
    else:[signature.append(sum(signature[-3:])) for i in range(3,n)]
    return signature

print(Tribonacci([1,1,1],10))
print(Tribonacci([300,200,100],10))
print(Tribonacci([0.5,0.5,0.5],30))