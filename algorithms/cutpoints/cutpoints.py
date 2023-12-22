from typing import Dict, List, Tuple


def cutpoints_search(graph: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    n = len(graph)
    visited = [False] * n
    entry_time = [-1] * n
    lowpoint = [-1] * n
    timer = 0

    cutpoints = []

    def dfs(node: int, parent: int = -1):
        nonlocal visited, entry_time, lowpoint, timer, cutpoints
        visited[node] = True
        entry_time[node] = timer
        lowpoint[node] = timer
        timer += 1

        children_count = 0
        for neighbour in graph[node]:
            if neighbour == parent:
                continue

            if visited[neighbour]:
                lowpoint[node] = min(
                    lowpoint[node],
                    entry_time[neighbour],
                )
            else:
                dfs(neighbour, parent=node)
                lowpoint[node] = min(
                    lowpoint[node],
                    lowpoint[neighbour],
                )
                if lowpoint[neighbour] >= entry_time[node] and -1 != parent:
                    cutpoints.append(node)
                children_count += 1
        if -1 == parent and children_count > 1:
            cutpoints.append(node)

    for node in range(len(graph)):
        if False == visited[node]:
            dfs(node)

    return cutpoints
