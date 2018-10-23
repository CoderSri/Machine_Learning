import sys
sys.setrecursionlimit(1000) #递归深度

capacity = [8, 5, 3]
final_state = [4, 4, 0]
step = []
step.append([8, 0, 0])
steps = []
count = 0

def compare(a, b):
    i = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def valid(state, i, j):
    if i == j or state[j] <= 0:
        return False
    return True


def search(state):
    if(compare(state, final_state)):
        steps.append(list(step))
        return

    for i in range(len(state)):
        for j in range(len(state)):
            if not valid(state, i, j):
                continue
            pre_state = list(state)
            if state[i] + state[j] >= capacity[i]:
                delta = capacity[i] - state[i]
                state[i] = capacity[i]
                state[j] = state[j] - delta
            else:
                state[i] = state[i] + state[j]
                state[j] = 0
            if(state not in step):
                step.append(list(state))
                search(state)
                step.pop()
            state = pre_state


if __name__ == '__main__':
    # 初始状态
    state = [8, 0, 0]
    search(state)
    finals = []
    for step in steps:
        if step not in finals: # 去重
            finals.append(step)
    for i, step in enumerate(finals):
        print('suc:', i+1, step, '步数:', len(step))


