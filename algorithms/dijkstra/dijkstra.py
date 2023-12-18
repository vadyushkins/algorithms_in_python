from typing import Dict, List, Tuple


def dijkstra(
    graph: Dict[int, List[Tuple[int, int]]],
    source_node: int,
) -> List[int]:
    n = len(graph)
    distance = [-1] * n
    relaxed = [False] * n

    distance[source_node] = 0
    for i in range(n):
        u = -1
        for j in range(n):
            if relaxed[j] == False and (
                u == -1 or (distance[j] != -1 and distance[j] < distance[u])
            ):
                u = j
        if u == -1:
            break
        for v, w in graph[u]:
            if distance[v] == -1 or distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
        relaxed[u] = True

    return distance
