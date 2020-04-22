import random
from pprint import pprint

ans = random.randint(1,100)
count = 0
while True:
    num = int(input('Please input your number X∈【1，100】:'))
    count += 1
    if not 1 <= num <= 100:
        print('Error of your input.')
        break
    if num == ans:
        print('Congratulations! You\'ve guessed it {} times'.format(count))
        break

    value = 'small' if num < ans else 'big'
    print('X is too {}, please input again'.format(value))
