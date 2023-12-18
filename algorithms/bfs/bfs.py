from typing import Dict, List


def bfs(
    graph: Dict[int, List[int]],
    source_node: int,
) -> List[int]:
    from collections import deque

    n = len(graph)
    distance = [-1] * n
    distance[source_node] = 0
    queue = deque([source_node])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if -1 == distance[v]:
                distance[v] = distance[u] + 1
                queue.append(v)
    return distance
