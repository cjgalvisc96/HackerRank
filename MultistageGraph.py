def MultiStageGraph(graph, nodes, stages):
    minimun = 0
    list_cost = [0] * (nodes + 1)
    list_d = [0] * (nodes + 1)
    paths = [0] * (nodes + 1)
    list_cost[nodes] = 0
    for i in range((nodes-1), 0, -1):
        minimun = 32767
        for k in range((i + 1), (nodes + 1)):
            if (graph[i][k] != 0) and \
               ((graph[i][k] + list_cost[k]) < minimun):
                minimun = graph[i][k] + list_cost[k]
                list_d[i] = k
        list_cost[i] = minimun
    paths[1] = 1
    paths[stages] = nodes
    for j in range(2, stages):
        paths[j] = list_d[paths[j - 1]]
    return paths


if __name__ == "__main__":
    stages = 4
    nodes = 8
    # graph = [[0]*(nodes + 1) for _ in range(nodes + 1)]
    graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 1, 3, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 3, 0, 0],
             [0, 0, 0, 0, 0, 6, 7, 0, 0],
             [0, 0, 0, 0, 0, 6, 8, 9, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 6],
             [0, 0, 0, 0, 0, 0, 0, 0, 4],
             [0, 0, 0, 0, 0, 0, 0, 0, 5],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print([x for x in MultiStageGraph(graph, nodes, stages) if x != 0])
