from typing import Dict, List


def strongly_connected_components_search(
    graph: Dict[int, List[int]],
) -> List[List[int]]:
    n = len(graph)
    visited = [False] * n

    condensation_order = []

    def compute_order(node: int):
        nonlocal visited, condensation_order
        visited[node] = True
        for neighbour in graph[node]:
            if False == visited[neighbour]:
                compute_order(neighbour)
        condensation_order.append(node)

    for i in range(n):
        if False == visited[i]:
            compute_order(i)

    transposed_graph: Dict[int, List[int]] = {i: [] for i in range(n)}
    for i in range(n):
        for j in graph[i]:
            transposed_graph[j].append(i)

    visited = [False] * n

    strongly_connected_component = []

    def compute_strongly_connected_component(node: int):
        nonlocal visited, transposed_graph, strongly_connected_component
        visited[node] = True
        strongly_connected_component.append(node)
        for neighbour in transposed_graph[node]:
            if False == visited[neighbour]:
                compute_strongly_connected_component(neighbour)

    result: List[List[int]] = []
    for i in range(n - 1, -1, -1):
        node = condensation_order[i]
        if False == visited[node]:
            compute_strongly_connected_component(node)
            result.append(strongly_connected_component[:])
            strongly_connected_component.clear()

    return result
