from typing import Dict, List


def dfs(
    graph: Dict[int, List[int]],
    reachable: Dict[int, bool],
    node: int,
) -> Dict[int, bool]:
    reachable[node] = True
    for neighbour in graph[node]:
        if False == reachable[neighbour]:
            dfs(graph, reachable, neighbour)
    return reachable
