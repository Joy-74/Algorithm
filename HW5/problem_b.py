# encoding=utf8
from queue import Queue


def process_text(line_text):
    s = line_text
    s = s[1:len(s) - 2]
    s = s.replace(',', '').replace('[', '').replace('(', '').replace(')', '')
    string_list = s.split(']')
    result = []
    for x in string_list:
        a = list(map(int, x.split()))
        pair_list = []
        for i in range(0, len(a), 2):
            pair = (a[i], a[i + 1])
            pair_list.append(pair)
        result.append(pair_list)
    return result


def dfs(source, sink):
    for i in range(m):
        pre[i] = float('inf')

    def real_dfs(source, progress, sink):
        if (progress == sink):
            return
        for i in range(m):
            if ((i == progress) | (i == source)):
                continue
            if ((residual[progress][i] > 0) & (pre[i] == float('inf'))):
                pre[i] = progress
                flow[i] = min(flow[progress], residual[progress][i])
                real_dfs(source, i, sink)

    real_dfs(source, source, sink)
    if (pre[sink] != float('inf')):
        return flow[sink]
    else:
        return -1


def maxflow(source, sink):
    sumflow = 0  # 记录最大流，一直累加
    augmentflow = 0  # 当前寻找到的增广路径的最小通过流量
    flow[source] = float('inf')
    while (True):
        augmentflow = dfs(source, sink)
        if (augmentflow == -1):
            break  # 返回-1说明已没有增广路径
        k = sink
        while (k != source):  # k回溯到起点，停止
            prev = pre[k]  # 走的方向是从prev到k
            maxflowgraph[prev][k] += augmentflow
            residual[prev][k] -= augmentflow  # 前进方向消耗掉了
            residual[k][prev] += augmentflow  # 反向边
            k = prev
        sumflow += augmentflow
    return sumflow


def max_flow(intput_data):
    global m
    m = len(input_data)
    global residual
    residual = [[0 for i in range(m)] for j in range(m)]
    global maxflowgraph
    maxflowgraph = [[0 for i in range(m)] for j in range(m)]
    global flow
    flow = [0 for i in range(m)]
    global pre
    pre = [float('inf') for i in range(m)]
    global q
    q = Queue()
    for arr_i in range(m):
        for tup in intput_data[arr_i]:
            residual[arr_i][tup[0]] = tup[1]
    result = maxflow(0, 1)
    return result

in_file = open("./data_b.txt", "r")
out_file = open("submission_b.txt", "w")
for line in in_file.readlines():
    input_data = process_text(line)
    out_file.write(str(max_flow(input_data)) + '\n')
in_file.close()
out_file.close()
