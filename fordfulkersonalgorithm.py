from collections import deque
def ford_fulkerson(graph, source, sink):
    n = len(graph)
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        q = deque([source])
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and graph[u][v] > 0:
                    parent[v] = u
                    q.append(v)
        if parent[sink] == -1:
            break
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    u, v, capacity = map(int, input().split())
    graph[u][v] += capacity

print(ford_fulkerson(graph, 0, V - 1))
