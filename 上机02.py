
road = []

graph = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],  # 1
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],  # 2
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],  # 3
    [0, 0, 1, 1, 0, 2, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 2, 0, 1, 1, 0, 0],  # 5
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],  # 6
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],  # 7
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 9
  #  0  1  2  3  4  5  6  7  8  9
]

args = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

count = 0

def compare(a, b):
    for i in range(10):
        for j in range(10):
            if a[i][j] != b[i][j]:
                return False
    return True


def DFS(v):
    global count
    if compare(graph, args):
        count = count + 1
        print(road)
        return
    for i in range(10):
        if graph[v][i] >= 1 and args[v][i] < graph[v][i]:
            args[v][i] = args[v][i] + 1
            args[i][v] = args[i][v] + 1
            road.append((v+1, i+1))
            DFS(i)
            args[v][i] = args[v][i] - 1
            args[i][v] = args[i][v] - 1
            road.pop()


if __name__ == '__main__':
    DFS(0)
    print(count)