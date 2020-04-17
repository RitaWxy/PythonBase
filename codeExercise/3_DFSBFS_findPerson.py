import networkx as nx
from matplotlib import pylab as plt

social_network = {
    '小张': ['小刘', '小王', '小红'],
    '小王': ['六六', '娇娇', '小曲'],
    '娇娇': ['宝宝', '花花', '喵喵'],
    '六六': ['小罗', '奥巴马']
}
social_graph = nx.Graph(social_network)
plt.rcParams['font.sans-serif'] = ['SimHei']
nx.draw(social_graph,with_labels=True)

plt.show()

def find_all_persons(connection_grap,someome_knew,expand_position):
    '''
    从某个人开始找到所有能够扩展出来的联系人
    '''

    need_to_check = [someome_knew]
    # already_knew = []
    already_knew = []
    while need_to_check:
        # case1：广度优先BFS 先进去的先访问，FIFO 队列
        # person = need_to_check.pop(0) # 从第一个开始搜索，一层一层搜索
        # case2: 深度优先DFS 现金取得后访问 FILO 栈
        # person = need_to_check.pop(-1) # 从加进去的最后一个往下搜索
        person = need_to_check.pop(expand_position)
        if person in already_knew : continue
        new_expand = connection_grap.get(person,[])
        need_to_check += new_expand
        already_knew.append(person)
        print('hh,我通过{}找到了{}'.format(person,new_expand))
    return already_knew

def dfs(group,start): return find_all_persons(group,start,expand_position=-1)
def bfs(group,start): return find_all_persons(group,start,expand_position=0)

print(dfs(social_network,'小张'))
