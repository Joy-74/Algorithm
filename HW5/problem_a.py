def cycle_or_toposort(g):
    global toposort, ch
    toposort = 1
    ch = -1
    visited = [0 for i in range(len(g))]
    result = []

    def top_sort(G):
        n = len(G)
        stack = list(range(n))
        result = []
        while stack:
            i = stack.pop()
            if i not in result:
                if all(j in result for j in G[i]):
                    result.append(i)
                else:
                    stack = stack + [i] + G[i]
        return result

    def dfs(x):
        global toposort, ch
        if not toposort:
            return
        visited[x] = 2
        for v in g[x]:
            if visited[v] == 0:
                dfs(v)
            elif visited[v] == 2:
                toposort = 0
                ch = v
                return
        if not toposort:
            return
        visited[x] = 1
        result.append(x)

    for u in range(len(g)):
        if not visited[u]:
            dfs(u)

    def dfs2(x):
        visited[x] = 3
        result.append(x)
        for v in g[x]:
            if visited[v] == 2:
                dfs2(v)

    if not toposort:
        result = []
        for i in range(len(g)):
            if visited[i] == 2:
                # print(vis)
                dfs2(i)
                break
    i = 0
    while i <= (len(result) - 1):
        check = 0
        for j in range(len(g[result[len(result) - 1]])):
            if result[i] == g[result[len(result) - 1]][j]:
                check = 1
        if check == 1:
            break
        else:
            result.pop(0)

    if not toposort:
        return "cycle", result
    return "toposort", top_sort(g)


with open("data_a.txt", "r") as f:
    with open("submission_a.txt", "w") as w:
        for l in f.readlines():
            result = cycle_or_toposort(eval(l))
            w.write(str(result) + "\n")
