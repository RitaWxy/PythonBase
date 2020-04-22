'''
queue模块是对栈和队列的封装
'''
# import queue
# class MovingAverage():
#     '''
#     给定一个整数数据流和一个窗口大小，根据滑动窗口大小计算所有整数的移动平均值
#     '''
#     def __init__(self,size:int):
#         '''
#         :param size: initial queqe size
#         '''
#         self.q = queue.Queue(maxsize= size)
#
#     def next(self,val:int) ->float:
#         if self.q.full(): self.q.get()
#         self.q.put(val)
#         return sum(self.q.queue)/self.q.qsize()
#
# m = MovingAverage(3)
# print(m.next(1)) # 1/1 = 1
# print(m.next(10)) # (1+10)/2
# print(m.next(5)) # (1+10+5)/3
# print(m.next(6)) # (10+5+6)/3

'''
queue 模块补充
'''
from queue import Queue,LifoQueue,PriorityQueue,deque
# 先进先出队列FIFO
q = Queue(maxsize=5)

# 后进先出 栈 LIFO
lq = LifoQueue(maxsize = 6)

# 优先级队列
pq = PriorityQueue(maxsize = 5)

for i in range(5):
     q.put(i)
     lq.put(i)
     pq.put(i)

#q.put(i for i in range(5))

print("先进先出队列：{}   是否为空：{} 多大：{}  是否满：{}".format(q.queue,q.empty(),q.qsize(),q.full()))
print("后进先出队列：{}   是否为空：{} 多大：{}  是否满：{}".format(lq.queue,lq.empty(),lq.qsize(),lq.full()))
print("优先级队列：{}   是否为空：{} 多大：{}  是否满：{}".format(pq.queue,pq.empty(),pq.qsize(),pq.full()))

print(q.get(),lq.get(),pq.get())

print("先进先出队列：{}   是否为空：{} 多大：{}  是否满：{}".format(q.queue,q.empty(),q.qsize(),q.full()))
print("后进先出队列：{}   是否为空：{} 多大：{}  是否满：{}".format(lq.queue,lq.empty(),lq.qsize(),lq.full()))
print("优先级队列：{}   是否为空：{} 多大：{}  是否满：{}".format(pq.queue,pq.empty(),pq.qsize(),pq.full()))

# 双边队列deque
dq = deque([1,2,3])
dq.append(4)
print(dq,'\n')
print(dq.pop())
print(dq,'\n')
print(dq.popleft())
print(dq,'\n')
print(dq.appendleft(5))
print(dq)
print(len(dq))
