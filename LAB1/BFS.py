from collections import deque


def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
       
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


result = bfs(graph, "A")
print(result)