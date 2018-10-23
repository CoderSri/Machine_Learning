from queue import Queue

capacity = [8, 5, 3]  # 三个瓶子的容量
final_state = [4, 4, 0]  # 目标装态
step = []  # 用以记录入过队列的所有状态
road = [0 for i in range(20)]  # 存放新转态的前一状态
real_road = []  # 用以存放真实路径
real_road.append(final_state)  # 加入
count = 0


# 比较两个数组的所有的对应下标的值是否都相等，若是，返回True, 否则返回False
def compare(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def valid(state, i, j):
    if i == j or state[i] <= 0:
        return False
    return True


# 得到真实路径
def get_road(road, i):
    # print(step[road[i]])
    real_road.append(step[road[i]])
    if compare(step[road[i]], [8, 0, 0]):
        return
    get_road(road, road[i])


def search(state):
    global real_road
    qu = Queue()  # 定义一个队列
    qu.put(state)  # 初始转态入队列
    step.append(list(state))  # 将初始转态记录在step中
    while not qu.empty():  # 队列不空
        cur_state = qu.get()  # 出队列
        # 存储当前转态的所有可能状态
        for i in range(len(cur_state)):
            for j in range(len(cur_state)):
                if valid(cur_state, i, j):  # 判断是否能倒水
                    next_state = list(cur_state)  # 初始化新状态
                    if cur_state[i] + cur_state[j] >= capacity[j]:  # 生成新状态
                        delta = capacity[j] - cur_state[j]
                        next_state[j] = capacity[j]
                        next_state[i] = cur_state[i] - delta
                    else:
                        next_state[j] = cur_state[i] + cur_state[j]
                        next_state[i] = 0
                    if next_state not in step:  # 若生成的新状态在队列中从未存在过
                        step.append(list(next_state))  # 记录加入到队列的新状态
                        road[step.index(next_state)] = step.index(cur_state)  # 记录新装态的前一状态,方便回溯打印路径
                        if compare(next_state, final_state):  # 若当前状态为最终状态
                            print('search success')  # 查找成功
                            get_road(road, step.index(next_state))  # 在road中回溯得到最终路径
                            print(real_road[::-1])  # 反转数组后输出
                            step[step.index(next_state)] = [0, 0, 0]
                            real_road = []  # 清空real_road
                            real_road.append(final_state)
                            # return
                        else:
                            qu.put(next_state)  # 将生成的新状态加入队列


if __name__ == '__main__':
    state = [8, 0, 0]   # 初始状态
    search(state)


